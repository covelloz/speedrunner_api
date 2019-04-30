
from datetime import datetime
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
        self.speedruns_table = meta.tables['SpeedRuns']

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

    def serialize(self):
        return {'game': self.game}


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

    def serialize(self):
        return {'category': self.category}


class Player(Database):
    def __init__(self, player):
        super().__init__()
        self.player = player

    @property
    def player_id(self):
        conn = super().make_connection()
        sql = 'SELECT player_id FROM Players WHERE player=%s'
        player_id = conn.execute(sql, self.player).fetchall()[0][0]
        super().destroy_connection(conn)
        return player_id

    def serialize(self):
        return {'player': self.player}


class GameCategoryMap(object):
    def __init__(self, game, category):
        self.game = Game(game)
        self.category = Category(category)

    def serialize(self):
        return {
            'game_id': self.game.game_id,
            'category_id': self.category.category_id
        }


class SpeedRun(object):
    def __init__(self, game, player, duration):
        self.game = Game(game)
        self.player = Player(player)
        self.duration = duration

    def serialize(self):
        return {
            'game_id': self.game.game_id,
            'player_id': self.player.player_id,
            'duration': self.duration
        }
