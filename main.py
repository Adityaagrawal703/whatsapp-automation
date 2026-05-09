"""
1-twilio client setup
2-user inputs
3-sheduling logic 
4-send message
"""
"if you run the code "
#step 1
from twilio.rest import Client
from datetime import datetime
import time

account_sid = "your_sid of twilio"
auth_token = "you_token of twilio"

client = Client(account_sid, auth_token)

def send_whatsapp_message(recipient_number, message_body):
    try:
        message = client.messages.create(
            from_='whatsapp:______',
            body=message_body,
            to=f'whatsapp:{recipient_number}',
        )

        print(f'Message sent successfully! Message SID: {message.sid}')

    except Exception as e:
        print("An error occurred:", e)

name = input("Enter the recipient name: ")

recipient_number = input(
    "Enter recipient WhatsApp number with country code: "
)

message_body = input(
    f'Enter the message you want to send to {name}: '
)

date_str = input(
    "Enter the date to send message (YYYY-MM-DD): "
)

time_str = input(
    "Enter time (HH:MM in 24-hour format): "
)

schedule_datetime = datetime.strptime(
    f'{date_str} {time_str}',
    "%Y-%m-%d %H:%M"
)

current_datetime = datetime.now()

time_difference = schedule_datetime - current_datetime

delay_seconds = time_difference.total_seconds()

if delay_seconds <= 0:
    print("The specified time is in the past.")
else:
    print(
        f'Message scheduled for {name} at {schedule_datetime}'
    )

    time.sleep(delay_seconds)

    send_whatsapp_message(
        recipient_number,
        message_body
    )
