- **Complete 1base.sh install\setup from infrastructure_project.**

```
cd ~/dev/infrastructure_project
sudo ./9install_webserver.sh lighttpd
cd ~/dev
git clone https://github.com/dmarsh19/flask_twilio.git flask_twilio_project
cd flask_twilio_project
```

- Update the required settings.py values
  - ACCOUNT_SID
  - AUTH_TOKEN
  - TO_NUMBER
  - FROM_NUMBER
> twilio account configurations:
> https://www.twilio.com/console/sms/dev-tools/twiml-apps
> https://www.twilio.com/console/phone-numbers/incoming

```
sudo ./install.sh "flask_twilio" "/twilio"
```

**If you have already deployed a separate flask project on this machine, subsequent deploys will not write the apporpriate server config in lighttpd.conf.**

