- **Complete 1base.sh install\setup from infrastructure_project.**

```
cd ~/dev
sudo ./infrastructure_project/9install_lighttpd.sh
git clone https://github.com/dmarsh19/flask_twilio.git flask_twilio_project
cd flask_twilio_project
```

- Update the project name and url extension in install.sh
- Update the required settings.py values
  - ACCOUNT_SID
  - AUTH_TOKEN
  - TO_NUMBER
  - FROM_NUMBER
> twilio account configurations:
> https://www.twilio.com/console/sms/dev-tools/twiml-apps
> https://www.twilio.com/console/phone-numbers/incoming

```
sudo ./install.sh
```

