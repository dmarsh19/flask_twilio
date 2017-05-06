#!/usr/bin/env python3
"""
Send SMS only to a verified twilio number:
https://www.twilio.com/console/phone-numbers/verified
"""
from twilio.rest import Client

from flask_twiml import app

# Find these values at https://twilio.com/user/account
# now in settings.py
#account_sid = ""
#auth_token = ""

# also in settings.py
#to_number = ""
#from_number = ""

msg = 'Hello from flask_twiml rest client'

if __name__ == '__main__':
    client = Client(app.config['ACCOUNT_SID'], app.config['AUTH_TOKEN'])

    message = client.api.account.messages.create(to=app.config['TO_NUMBER'],
                                                 from_=app.config['FROM_NUMBER'],
                                                 body=msg)