import smtplib
import imaplib
import email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import plyer


def send_email(sender_email, sender_password, recipient_email, subject, body):
            # Create message container
    print("sender")
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    # Add body to email
    msg.attach(MIMEText(body, 'plain'))
    print("attach")
    print("hi")
    try:

        # Connect to SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        # Login to SMTP server
        server.login(sender_email, sender_password)
        # Send email
        server.sendmail(sender_email, recipient_email, msg.as_string())

        # Close connection
        server.quit()
        print("Email sent successfully")
    except smtplib.SMTPException as e:
        print("SMTP Error:", e)
        print("E")
    except Exception as e:
        print("Error:", e)


def receive_email(email_address, password):
    try:
        # Connect to Gmail's IMAP server
        mail = imaplib.IMAP4_SSL('imap.gmail.com', 993)

        # Login to IMAP server
        mail.login(email_address, password)

        # Select inbox
        mail.select('inbox')

        # Search for latest email
        result, data = mail.search(None, 'ALL')
        latest_email_id = data[0].split()[-1]

        # Fetch latest email
        result, data = mail.fetch(latest_email_id, '(RFC822)')
        raw_email = data[0][1]
        msg = email.message_from_bytes(raw_email)

        # Print email body
        print(msg.get_payload())
        print( f"From: {msg['From']}\nSubject: {msg['Subject']}")
        # Show notification
        notification_title = "New Email Received"
        notification_message = f"From: {msg['From']}\nSubject: {msg['Subject']}"
        plyer.notification.notify(
            title=notification_title,
            message=notification_message,
            timeout=10
        )

        # Close connection
        mail.close()
        mail.logout()
    except Exception as e:
        print("Error:", e)



# Test sending email
send_email("nwspring94@gmail.com", "kbfe gguf unuc xiwe", "nwspring94@gmail.com", "Test Subject", "hi.")

# # Test receiving email
receive_email("nwspring94@gmail.com", "kbfe gguf unuc xiwe")
