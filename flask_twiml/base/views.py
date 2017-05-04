"""
"""
from flask import render_template
from twilio import twiml

from . import base


@base.route('/')
#@base.route('/main')
def main():
    return render_template('base.html')


@base.route('/twilio', methods = ['GET', 'POST'])
def twilio():
    """Respond to SMS with SMS"""
    resp = twiml.Response()
    resp.message("Hello from flask_twiml!")
    return str(resp)
