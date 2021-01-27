import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class config:
    SECRET_KEY = os.environ.get(
        'SECRET_KEY') or 'nhfhBBB54GDs%^%$#86G&^%4fttfdd^$'


class DevelopementConfig(config):
    DEBUG = True
    EMAIL_BACKEND = "django.core.mail.backends.filebased.EmailBackend"
    EMAIL_FILE_PATH = os.path.join(BASE_DIR, "sent_mails")
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }


class TestingConfig(config):
    TESTING = True
    DATABASES = {
        'default': {

            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
            'ENGINE': 'django.db.backends.mysql',


        }
    }


# class ProductionConfig(config):
#     DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': os.environ['DBNAME'],
#         'USER': os.environ['DBUSERNAME'],
#         'PASSWORD': os.environ['DBPASSWORD'],
#         'HOST': os.environ['DBHOST'],
#         'PORT': '5432',
#     }
# }
#     EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
#     EMAIL_HOST="smtp.gmail.com"
#     EMAIl_PORT = int(os.environ.get('MAIL_PORT', '587'))
#     EMAIL_USER = os.environ.get('MAIL_USERNAME')
#     EMAIL_HOST_PASSWORD = os.environ.get('MAIL_PASSWORD')
#     EMAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'true').lower() in ['true', 'on', '1']


config = {
    'developement': DevelopementConfig,
    'testing': TestingConfig,
    # 'production': ProductionConfig,
    'default': DevelopementConfig
}
