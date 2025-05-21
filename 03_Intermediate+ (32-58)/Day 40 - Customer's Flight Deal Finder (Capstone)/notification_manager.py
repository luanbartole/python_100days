from twilio.rest import Client
import smtplib
import os

# Email credentials stored as environment variables for security
BOT_EMAIL = os.environ.get("PYTHON_EMAIL")
BOT_PASSWORD = os.environ.get("PYTHON_EMAIL_PASSWORD")

class NotificationManager:
    """Sends notifications (SMS and email) containing flight deal details."""

    def __init__(self, twilio_sid, twilio_token, twilio_phone_a, twilio_phone_b):
        """
        Initializes the NotificationManager with Twilio credentials and phone numbers.

        Args:
            twilio_sid (str): Twilio Account SID.
            twilio_token (str): Twilio Auth Token.
            twilio_phone_a (str): Sender phone number (Twilio).
            twilio_phone_b (str): Recipient phone number.
        """
        self.account_sid = twilio_sid
        self.auth_token = twilio_token
        self.phone_a = twilio_phone_a
        self.phone_b = twilio_phone_b

    def send_sms(self, text: str):
        """
        Sends an SMS with the provided text message via Twilio.

        Args:
            text (str): The message body to send via SMS.
        """
        client = Client(self.account_sid, self.auth_token)
        message = client.messages.create(
            body=text,
            from_=self.phone_a,
            to=self.phone_b
        )
        print(message.status)  # Log the message status (e.g., 'queued', 'sent')

    def send_emails(self, emails: list, message: str, google_flight_link: str):
        """
        Sends an email with flight deal details to a list of user emails.

        Args:
            emails (list): A list of recipient email addresses.
            message (str): The body of the email message.
            google_flight_link (str): A URL to the Google Flights search for the deal.
        """
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()  # Secure the connection
            connection.login(BOT_EMAIL, BOT_PASSWORD)  # Login with bot email credentials
            for email in emails:
                connection.sendmail(
                    from_addr=BOT_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}\n{google_flight_link}".encode('utf-8')
                )
