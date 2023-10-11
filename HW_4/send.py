import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import datetime as DT


# Функция для отправки сообщения на электронную почту
def send_to_email(sender_email, recipient_email, password, filename):
    # Получение текущего времени
    now = DT.datetime.now(DT.timezone.utc).astimezone()
    time_format = "%Y-%m-%d %H:%M:%S"
    subject = f"report {now:{time_format}}"
    message_body = 'Здесь ваш текст с отчетом о тестировании.'

    # Создание объекта MIMEMultipart
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    # Добавление текста сообщения
    msg.attach(MIMEText(message_body, 'plain'))

    # Добавляем файл во вложение
    with open(filename, 'rb') as f:
        attach = MIMEBase('application', 'octet-stream')
        attach.set_payload(f.read())
        encoders.encode_base64(attach)
        attach.add_header('Content-Disposition', f'attachment; filename= {filename}')
        msg.attach(attach)

    # Настройка SMTP-сервера Mail.ru
    smtp_server = 'smtp.mail.ru'
    smtp_port = 587  # Порт для шифрованного соединения (TLS)

    try:
        # Создание объекта SMTP и установка соединения
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Включение шифрованного соединения

        # Вход в почтовый аккаунт
        server.login(sender_email, password)

        # Отправка сообщения
        server.send_message(msg)

        print("Email sent successfully!")

    except smtplib.SMTPException as e:
        print(f"Failed to send email: {e}")

    finally:
        # Закрытие соединения с SMTP-сервером
        server.quit()
