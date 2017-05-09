-spin up new aws instance (ubuntu server)
  -security group to Flask-Default-Web-Server
  -existing key pair (ec2-zeromq**)
-From local machine, grab public dns from AWS console
-Update putty hostname
-when opening, may need to login as user "ubuntu", no password

mkdir ~/dev
cd ~/dev
git clone https://github.com/dmarsh19/infrastructure.git infrastructure_project
sudo ./infrastructure_project/1install_base.sh
./infrastructure_project/2setup_base.sh
source ~/.bashrc
sudo ./infrastructure_project/9install_lighttpd.sh
cd /var/www
### THIS IS BAD!!
## will install as root, needs permissions set for a web user (www-data?)
# and installed that way
### /var/www is owned by root
sudo git clone https://github.com/dmarsh19/flask_twiml.git flask_twiml_project
sudo python3 -m pip install -r flask_twiml_project/requirements.txt
touch flask_twiml_project/settings.py
sudo nano /etc/lighttpd/lighttpd.conf
#add below lines to /etc/lighttpd/lighttpd.conf
# twilio account configurations:
# https://www.twilio.com/console/sms/dev-tools/twiml-apps
# https://www.twilio.com/console/phone-numbers/incoming
sudo service lighttpd restart
navigate to the url


requires python3

This is still a dev webserver.
For production:
    write log to /var/log
    run under low permission user
# rename local dir in /var/www from git clone to the url? (i.e. twiml.admrsh.com)

#chmod 775 flask_lighttpd.fcgi
#chmod 775 runserver.py

# may need to change python path in these files:
runserver.fcgi (2 locations)
runserver.py
settings.py (APP_LOGFILE)
below for bin-path in lighttpd.conf, fcgi

# in /etc/lighttpd/lighttpd.conf, add the following line in the server.modules array:
        "mod_fastcgi",

# and append the following lines at the end (CHANGE username in bin-path):
#### lighttpd_core ####
#debug.log-request-header = "enable"
#debug.log-response-header = "enable"
debug.log-request-handling = "enable"
debug.log-condition-handling = "enable"

#### mod_fastcgi ####
fastcgi.debug = 1
fastcgi.server = (
  "/" => ( (
    "socket" => "/tmp/runserver-fcgi.socket",
    "bin-path" => "/var/www/flask_twiml_project/runserver.fcgi",
    "check-local" => "disable",
    "max-procs" => 1
  ) )
)
