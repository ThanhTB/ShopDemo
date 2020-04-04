class Config:
    SECRET_KEY = 'b7f4add9ed214d35bc3ecf609e1f360f'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    EMAIL_SERVER = 'smtp.googlemail.com'
    EMAIL_PORT = 587
    EMAIL_USER_TLS = True
    EMAIL_USERNAME = 'test-mail@gmail.com'
    EMAIL_PASSWORD = 'password'

    # SECRET_KEY = os.environ.get('SECRET_KEY')
    # SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')