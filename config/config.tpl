# Statement for enabling the development environment
DEBUG = True
APP_HOST = '192.168.1.7'
APP_PORT = 5000
# Define the application directory
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
BASE_ROOT = os.path.abspath(os.path.join(os.path.split(__file__)[0], '..'))
TEMPLATE_ROOT = os.path.join(BASE_ROOT, 'templates/')
STATIC_ROOT = os.path.join(BASE_ROOT, 'static/')

# Define the database - we are working with MySQL
MYSQL_DB = "test"
MYSQL_USER = "root"
MYSQL_PORT = 3306
MYSQL_PASSWORD = "12345678"
MYSQL_HOST = "192.168.1.86"
MYSQL_CHARSET = "utf-8"

# elasticSearch Server
ELASTIC_HOST = "http://192.168.1.86"
ELASTIC_PORT = 9200

# logs
# log level:
#   0: all log (this is default)
#   10: debug, info, warning, error log
#   20: info, warning, error log
#   30: warning, error log
#   40: only error log
#   50: nothing
LOG_LEVEL = 0
LOG_FILE = 'logs/application.log'