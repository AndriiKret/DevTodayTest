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
