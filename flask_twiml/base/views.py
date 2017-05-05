"""
"""
from flask import render_template
from twilio.twiml.messaging_response import MessagingResponse

from . import base


@base.route('/')
#@base.route('/main')
def main():
    return render_template('base.html')


@base.route('/twilio', methods=['GET', 'POST'])
def twilio():
    """Respond to SMS with SMS"""
    resp = MessagingResponse().message("Hello from flask_twiml!")
    return str(resp)
