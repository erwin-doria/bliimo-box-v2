DB_USERNAME = 'bliimo'
DB_PASSWORD = 'root'
DB_HOST = 'localhost'
DB_NAME = 'bliimov2'
SECRET_KEY = 'b11m0123'
PORT = 7836
SQLALCHEMY_DATABASE_URI = 'mysql://{}:{}@{}/{}'.format(DB_USERNAME,DB_PASSWORD,DB_HOST,DB_NAME)
API_BASE_URL = 'https://dev2.bliimo.net/api'
ENVIRONMENT = 'development'