# DevTodayTest
DevTodayTest is a Django REST framework API used to create news board with comment section

### Technologies
* python-3.8.3
* django-3.1
* postgresql - 12
* celery - 4.4.7

### Installation
PostgreSQL
```
# install
$ sudo apt-get install postgresql postgresql-contrib

# create user and database
$ sudo -i -u postgres
postgres=# CREATE USER <db_user> PASSWORD '<db_password>'";
postgres=# CREATE DATABASE <db_name> OWNER <db_user>;
postgres=# ALTER USER <db_user> CREATEDB;
```
RabbitMQ
```
# install
$ sudo apt-get install -y erlang
$ sudo apt-get install rabbitmq-server

# enable and start
$ systemctl enable rabbitmq-server
$ systemctl start rabbitmq-server

# check status
$ systemctl status rabbitmq-server
```

### Project configuration

   1. Clone this repository.
   2. Activate virtual environment.
   3. Go to the folder ```requirements.txt``` and run command to install required dependencies: 
   ```pip install -r requirements.txt```
   4.Create localsettings.py in DevelopsTodayTest/DevelopsTodayTest/ with following settings: 
   ```
   # Database settings
      DATABASES = {
          'default': {
             'ENGINE': 'django.db.backends.postgresql_psycopg2',
             'HOST': 'localhost',
             'USER': '<db_user>',
             'PASSWORD': '<db_password>',
             'NAME': '<db_name>',
          }
   }```
