import pathlib

BASE = pathlib.Path(__file__).parent


class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + \
                              str(BASE / "data" / "fin_app.sqlite3?check_same_thread=False")
    # SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:tatiana@localhost:5432' \
    #                           '/fin_management'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'tatiana'
