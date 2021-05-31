from twilio.rest import Client
import smtplib

TWILLIO_SID = "Your twillio sid"
TWILLIO_AUTH_TOKEN = "Your twillio auth"
TWILIO_VIRTUAL_NUMBER = "your registered virtual number"
TWILIO_VERIFIED_NUMBER = "target phone"
MY_EMAIL = "your email"
MY_PASSWORD = "password for email"
SMTP_ADRESS = "smtp.gmail.com"



class NotificationManager:

    def __init__(self):
        self.client = Client(TWILLIO_SID, TWILLIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER
        )

        print(message.sid)

    def send_emails(self, emails, message, google_flight_link):
        with smtplib.SMTP(SMTP_ADRESS) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price flight!\n\n"
                        f"{message}\n{google_flight_link}".encode("utf-8")
                )