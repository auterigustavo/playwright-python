import smtplib
import os

ENV_MAIL = 'auterigustavo@gmail.com'
ENV_PASS = os.environ.get('EMAIL_PASS')

def get_connection(email, password):
    server = smtplib.SMTP(host='smtp.gmail.com', port=587)
    server.ehlo()
    server.starttls()
    server.login(user=email, password=password)
    return server

def get_last_product_list():
    carpeta = 'reports'
    reportes = os.listdir(carpeta)
    reportes_txt = [reporte for reporte in reportes]
    reportes_txt.sort(key=lambda x: os.path.getmtime(os.path.join(carpeta, x)))
    if reportes_txt:
        ultimo = reportes_txt[-1]
        path_txt = os.path.join(carpeta, ultimo)
        with open(path_txt, 'r') as file:
            contenido = file.read()
    return contenido

def send_mail_to_address(email):
    smtp_server = get_connection(ENV_MAIL, ENV_PASS)
    content = get_last_product_list()
    text = f'\n{content}\n'
    message = f'Subject: Lista de precios Carrefour\n\n {text}'
    mailBody = message.encode('utf-8')
    smtp_server.sendmail(from_addr=ENV_MAIL, to_addrs=email, msg=mailBody)
    smtp_server.quit()