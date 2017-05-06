"""
"""
from flask import render_template, request, redirect, url_for
from twilio.twiml.messaging_response import MessagingResponse

from . import base


@base.route('/')
#@base.route('/main')
def main():
    return render_template('base.html')


@base.route('/twilio', methods=['GET', 'POST'])
def twilio():
    """Respond to SMS with SMS"""
    body = request.values.get('Body', None)
    if 'HELLO' in str(body).upper():
        return redirect(url_for('.hello'))

    resp = MessagingResponse().message("Hello from flask_twiml!")
    return str(resp)


@base.route('/hello', methods=['GET', 'POST'])
def hello():
    """redirect here if twilio response includes 'hello'"""
    resp = MessagingResponse().message("You were redirected to hello!")
    return str(resp)

