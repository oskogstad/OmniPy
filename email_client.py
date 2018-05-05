from smtplib import SMTP_SSL as SMTP, SMTPHeloError, SMTPAuthenticationError, SMTPException
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email(to_email, from_email, password, subject, content, smtp_address, smtp_port):
    msg = MIMEMultipart()
    msg['From'] = 'OmniPy'
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(content))

    server_connected = False
    try:
        smtp_server = SMTP(smtp_address, smtp_port)
        smtp_server.login(from_email, password)
        server_connected = True
    except SMTPHeloError as e:
        print("Server did not reply")
    except SMTPAuthenticationError as e:
        print("Incorrect username/password combination. \nIf you are using Gmail, you need to use an app password: "
              "https://myaccount.google.com/apppasswords")
    except SMTPException as e:
        print("Authentication failed")

    if server_connected:
        try:
            smtp_server.sendmail(from_email, to_email, msg.as_string())
            print("Successfully sent email")
        except SMTPException as e:
            print("Error: unable to send email", e)
        finally:
            smtp_server.close()
