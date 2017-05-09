"""
"""
from flask import render_template, request, redirect, url_for, make_response
from twilio.twiml.messaging_response import MessagingResponse

from . import base


@base.route('/')
#@base.route('/main')
def main():
    return render_template('base.html')


@base.route('/twilio', methods=['GET', 'POST'])
def twilio():
    """Respond to SMS with SMS"""
    met_before = request.cookies.get('flask_twiml_metbefore', False)
    if met_before:
        # this is ugly, but you can't store a bool in cookies so its converting str to bool
        if met_before.upper() == 'TRUE':
            return redirect(url_for('.met_before'))
    #TODO: set cookie always
    # for now, this will only set the cookie if the user doesn't send 'hello'
    # because I don't want to write the code twice to attach the cookie to a response
    # (this function response and the hello() redirect response).
    # potentially i could use a Flask after_request callback to always try and
    # set the cookie. Or look at deferred request callbacks (not recommended)
    body = request.values.get('Body', None)
    if 'HELLO' in str(body).upper():
        return redirect(url_for('.hello'))

    twml = MessagingResponse().message("Hello from flask_twiml!")
    resp = make_response(str(twml))
    resp.set_cookie('flask_twiml_metbefore', value='TRUE')
    return str(resp)


@base.route('/hello', methods=['GET', 'POST'])
def hello():
    """redirect here if twilio response includes 'hello'"""
    resp = MessagingResponse().message("You were redirected to hello!")
    return str(resp)


@base.route('/met_before', methods=['GET', 'POST'])
def met_before():
    """redirect here if incoming twilio SMS has a cookie"""
    resp = MessagingResponse().message("We meet again!")
    return str(resp)
