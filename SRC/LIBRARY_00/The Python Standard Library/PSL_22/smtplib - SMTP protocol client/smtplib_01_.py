#------------------------------------------
# _01_ ():
#------------------------------------------
def _01_ ():
    """_01_"""
#beginfunction
    print (f'#-----------------------------')
    print (f'# {_01_.__name__}')
    print (f'#-----------------------------')

    # https://t.me/pythonercode/1920
    # ✈️smtplib — это стандартная библиотека Python для отправки
    # электронных писем через SMTP-серверы. Она позволяет легко
    # отправлять сообщения, включая текст, файлы и HTML-контент.
    # Отправка email может быть полезна для автоматических
    # уведомлений, напоминаний или регулярных отчетов.
    #
    # ➡️Пример отправки простого email:
    # import smtplib
    # from email.mime.text import MIMEText
    # from email.mime.multipart import MIMEMultipart
    #
    # # Настройки отправителя
    # sender_email = "your_email@gmail.com"
    # receiver_email = "recipient_email@example.com"
    # password = "your_password"  # Введите пароль или токен
    # приложения
    #
    # # Создание сообщения
    # message = MIMEMultipart()
    # message['From'] = sender_email
    # message['To'] = receiver_email
    # message['Subject'] = "Тестовое сообщение из Python"
    #
    # # Текст письма
    # body = "Привет! Это тестовое сообщение, отправленное с
    # помощью Python."
    # message.attach(MIMEText(body, 'plain'))
    #
    # # Подключение к SMTP-серверу Gmail
    # try:
    #     server = smtplib.SMTP('smtp.gmail.com', 587)
    #     server.starttls()  # Шифрование соединения
    #     server.login(sender_email, password)  # Авторизация
    #
    #     # Отправка письма
    #     text = message.as_string()
    #     server.sendmail(sender_email, receiver_email, text)
    #     print("Сообщение успешно отправлено!")
    # except Exception as e:
    #     print(f"Ошибка отправки: {e}")
    # finally:
    #     server.quit()
    #
    # 💡Важно: Для работы с Gmail необходимо использовать токен
    # приложения вместо обычного пароля (включите двухфакторную
    # аутентификацию и сгенерируйте токен).
    #
    # ➡️Пример отправки email с вложением:
    # from email.mime.base import MIMEBase
    # from email import encoders
    #
    # # Добавляем вложение
    # filename = "example.txt"
    # with open(filename, "rb") as attachment:
    #     part = MIMEBase("application", "octet-stream")
    #     part.set_payload(attachment.read())
    #
    # encoders.encode_base64(part)
    # part.add_header(
    #     "Content-Disposition",
    #     f"attachment; filename= {filename}",
    # )
    #
    # message.attach(part)
    #
    # # Отправляем письмо как раньше
    # server.sendmail(sender_email, receiver_email,
    # message.as_string())
    # print("Сообщение с вложением успешно отправлено!")
    #
    # ➡️Основные функции библиотеки:
    #
    # 1. Создание SMTP-объекта - для подключения к почтовому
    # серверу.
    # 2. Аутентификация - возможность входа с использованием
    # логина и пароля.
    # 3. Отправка почты - метод для отправки электронных писем с
    # указанным содержимым.
    #
    # 📖 Официальная документация smtplib (https://docs.python.org/3/library/smtplib.html?spm=5aebb161.6817d428.0.0.6ab77245Oyijgt)

#endfunction

#------------------------------------------
#
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    _01_ ()
#endif

#endmodule
