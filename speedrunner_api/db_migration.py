import sqlalchemy
from speedrunner_api.config import config

ENGINE = sqlalchemy.create_engine(
    "mysql+pymysql://{}:{}@localhost/{}".format(
        config.admin_usr,
        config.admin_pwd,
        config.database
    )
)


def make_connection():
    conn = ENGINE.connect()
    print(conn)
    conn.close()
