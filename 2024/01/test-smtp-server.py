import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def test_smtp_server():
    try:
        # Get credentials from environment variables
        smtp_server = os.environ.get("SMTP_SERVER")
        smtp_port = int(os.environ.get("SMTP_PORT", 587))  # Default to 587
        username = os.environ.get("SMTP_USERNAME")
        password = os.environ.get("SMTP_PASSWORD")
        sender_email = os.environ.get("SENDER_EMAIL")
        recipient_email = os.environ.get("RECIPIENT_EMAIL")

        # Connect to the SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.set_debuglevel(1)  # Enable debug output
        server.starttls()

        # Log in to the account
        server.login(username, password)

        # Send a test email
        subject = "Test email"
        body = "This is a test email."
        message = MIMEMultipart()
        message.attach(MIMEText(body, "plain"))
        message["Subject"] = subject
        message["From"] = sender_email
        message["To"] = recipient_email

        server.sendmail(sender_email, recipient_email, message.as_string())
        print("Test email sent successfully.")

    except smtplib.SMTPException as e:
        print(f"SMTP Error: {e}")
    except Exception as e:
        print(f"General Error: {e}")
    finally:
        # Close the connection
        try:
            server.quit()
        except Exception as e:
            print(f"Error in closing the connection: {e}")

# Call the function to test
test_smtp_server()
