import os
from dotenv import load_dotenv
load_dotenv()
class Config(object):
    SQLALCHEMY_DATABASE_URI = f'postgresql://{os.getenv("POSTGRES_USERNAME")}:{os.getenv("POSTGRES_PASSWORD")}@{os.getenv("POSTGRES_SERVER_DEV")}/{os.getenv("POSTGRES_DBNAME")}'