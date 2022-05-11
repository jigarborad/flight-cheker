from twilio.rest import Client

TWILIO_SID = "AC424a51e79399b615b41ad2da94d446f9"
TWILIO_AUTH_TOKEN = "2419fbe477dfa79ac1edc84f4427af05"
TWILIO_NUMBER = '+18482855433'
MY_NUMBER = '+49 17686072127'


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_NUMBER,
            to=MY_NUMBER
        )
        print("hhhhh")
        print(message.sid)
