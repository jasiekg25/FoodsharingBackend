class Config:
    DEBUG=True
    SECRET_KEY = 'dev'
    SQLALCHEMY_DATABASE_URI = "postgresql://user:password@localhost/spaceshipDB" # TODO

    # Real config example:
    # SECRET_KEY = os.environ.get('SECRET_KEY')
    # SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')