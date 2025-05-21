from twilio.rest import Client

class NotificationManager:
    """Sends SMS notifications containing flight deal details using Twilio."""

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
        Sends an SMS with the provided text message.

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
