import os
class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SQLALCHEMY_DATABASE_URI = r'sqlite:///brainstormed.db?check_same_thread=False'
    SECRET_KEY = os.getenv("SECRET_KEY")
    TEMPLATES_AUTO_RELOAD = True
    SEND_FILE_MAX_AGE_DEFAULT = 0
    CLIENT_TXT = "usertmpfiles/"
