
from sqlalchemy import MetaData
from sqlalchemy import create_engine
from speedrunner_api.config import config


class Database(object):
    def __init__(self):
        # Reflection
        self.engine = create_engine(
            "mysql+pymysql://{}:{}@localhost/{}".format(
                config.admin_usr,
                config.admin_pwd,
                config.database
            )
        )
        meta = MetaData()
        meta.reflect(bind=self.engine)

        # Tables
        self.games_table = meta.tables['Games']
        self.categories_table = meta.tables['Categories']
        self.players_table = meta.tables['Players']
        self.gamecategorymap_table = meta.tables['GameCategoryMap']

    def make_connection(self):
        return self.engine.connect()

    def destroy_connection(self, conn):
        conn.close()


class Game(Database):
    def __init__(self, game):
        super().__init__()
        self.game = game

    @property
    def game_id(self):
        conn = super().make_connection()
        sql = 'SELECT game_id FROM Games WHERE game=%s'
        game_id = conn.execute(sql, self.game).fetchall()[0][0]
        super().destroy_connection(conn)
        return game_id


class Category(Database):

    def __init__(self, category):
        super().__init__()
        self.category = category

    @property
    def category_id(self):
        conn = super().make_connection()
        sql = 'SELECT category_id FROM Categories WHERE category=%s'
        category_id = conn.execute(sql, self.category).fetchall()[0][0]
        super().destroy_connection(conn)
        return category_id
