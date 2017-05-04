requires infrastructure_project/9install_lighttpd.sh
requires python3
clone into /var/www

This is still a dev webserver.
For production:
    write log to /var/log
    run under low permission user


#chmod 775 flask_lighttpd.fcgi
#chmod 775 runserver.py

# may need to change python path in these files:
runserver.fcgi (2 locations)
runserver.py
settings.py (APP_LOGFILE)


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



sudo service lighttpd restart
navigate to the url