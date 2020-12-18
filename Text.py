# Written by Richard Zins for PIDS
# we import the Twilio client from the dependency we just installed
from twilio.rest import Client
# the following line needs your Twilio Account SID and Auth Token
client = Client("ACbf928b9edd5290ec0c9d6e9d67340e6d", "a61bd8fb49cfc3318e258fdbc9c50478")
msg = 'ALERT: PIDS has detected an intrusion! Please check your surveillance dashboard!'
# change the "from_" number to your Twilio number and the "to" number
# to the phone number you signed up for Twilio with, or upgrade your
# account to send SMS to any phone number
def send():
    file = open('/var/www/html/phone.txt', 'r')
    text = file.read()
    client.messages.create(to=text, from_="+12513561984", body=msg)

