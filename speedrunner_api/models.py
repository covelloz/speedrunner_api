
import logging
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

    def insert_record(self, table, new_record_obj):
        conn = self.make_connection()
        new_record = new_record_obj.serialize()
        new_record['create_date'] = datetime.now()
        new_record['modify_date'] = datetime.now()
        conn.execute(table.insert(), new_record)
        self.destroy_connection(conn)


class Game(Database):
    def __init__(self, game):
        super().__init__()
        self.game = game

    @property
    def game_id(self):
        conn = super().make_connection()
        sql = 'SELECT game_id FROM Games WHERE game=%s;'
        result = conn.execute(sql, self.game).fetchall()
        super().destroy_connection(conn)
        game_id = result[0][0] if result else None
        return game_id

    def insert_record(self):
        if self.game_id is None:
            super().insert_record(self.games_table, self)
            message = 'Record successfully added: game_id = {}'\
                .format(self.game_id)
            logging.info(message)
        else:
            message = 'Record attempted but exists: game_id = {}'\
                .format(self.game_id)
            logging.info(message)

    def serialize(self):
        return {'game': self.game}


class Category(Database):
    def __init__(self, category):
        super().__init__()
        self.category = category

    @property
    def category_id(self):
        conn = super().make_connection()
        sql = 'SELECT category_id FROM Categories WHERE category=%s;'
        result = conn.execute(sql, self.category).fetchall()
        super().destroy_connection(conn)
        category_id = result[0][0] if result else None
        return category_id

    def insert_record(self):
        if self.category_id is None:
            super().insert_record(self.categories_table, self)
            message = 'Record successfully added: category_id = {}'\
                .format(self.category_id)
            logging.info(message)
        else:
            message = 'Record attempted but exists: category_id = {}'\
                .format(self.category_id)
            logging.info(message)

    def serialize(self):
        return {'category': self.category}


class Player(Database):
    def __init__(self, player):
        super().__init__()
        self.player = player

    @property
    def player_id(self):
        conn = super().make_connection()
        sql = 'SELECT player_id FROM Players WHERE player=%s;'
        result = conn.execute(sql, self.player).fetchall()
        super().destroy_connection(conn)
        player_id = result[0][0] if result else None
        return player_id

    def insert_record(self):
        if self.player_id is None:
            super().insert_record(self.players_table, self)
            message = 'Record successfully added: player_id = {}'\
                .format(self.player_id)
            logging.info(message)
        else:
            message = 'Record attempted but exists: player_id = {}'\
                .format(self.player_id)
            logging.info(message)

    def serialize(self):
        return {'player': self.player}


class GameCategoryMap(Database):
    def __init__(self, game, category):
        self.game = Game(game)
        self.category = Category(category)

    @property
    def gamecategorymap_id(self):
        conn = super().make_connection()
        sql = '''
            SELECT gamecategorymap_id
            FROM GameCategoryMap
            WHERE game_id = %s AND category_id = %s;'''
        result = conn.execute(sql, [
            self.game.game_id,
            self.category.category_id
        ]).fetchall()
        super().destroy_connection(conn)
        gamecategorymap_id = result[0][0] if result else None
        return gamecategorymap_id

    def _validate_record(self):
        game = self.game.game
        cateogry = self.category.category
        if self.game.game_id is None:
            return 'no existing Game record for: {}'.format(game)
        elif self.category.category_id is None:
            return 'no existing Category record for: {}'.format(cateogry)
        else:
            return 'valid'

    def insert_record(self):
        validate = self._validate_record()

        if self.gamecategorymap_id is None and validate == 'valid':
            super().insert_record(self.gamecategorymap_table, self)
            message = 'Record successfully added: gamecategorymap_id = {}'\
                .format(self.gamecategorymap_id)
            logging.info(message)
        elif validate != 'valid':
            message = 'Record attempted but {}'\
                .format(validate)
            logging.info(message)
        else:
            message = 'Record attempted but exists: gamecategorymap_id = {}'\
                .format(self.gamecategorymap_id)
            logging.info(message)

    def serialize(self):
        return {
            'game_id': self.game.game_id,
            'category_id': self.category.category_id
        }


class SpeedRun(Database):
    def __init__(self, game, player, duration):
        self.game = Game(game)
        self.player = Player(player)
        self.duration = duration

    @property
    def speedrun_id(self):
        conn = super().make_connection()
        sql = '''
            SELECT speedrun_id
            FROM SpeedRuns
            WHERE game_id = %s
                AND player_id = %s
                AND duration = %s;
        '''
        result = conn.execute(sql, [
            self.game.game_id,
            self.player.player_id,
            self.duration
        ]).fetchall()
        super().destroy_connection(conn)
        speedrun_id = result[0][0] if result else None
        return speedrun_id

    def _validate_record(self):
        game = self.game.game
        player = self.player.player
        if self.game.game_id is None:
            return 'no existing Game record for: {}'.format(game)
        elif self.player.player_id is None:
            return 'no existing Player record for: {}'.format(player)
        else:
            return 'valid'

    def insert_record(self):
        validate = self._validate_record()

        if self.speedrun_id is None and validate == 'valid':
            super().insert_record(self.speedruns_table, self)
            message = 'Record successfully added: speedrun_id = {}'\
                .format(self.speedrun_id)
            logging.info(message)
        elif validate != 'valid':
            message = 'Record attempted but {}'\
                .format(validate)
            logging.info(message)
        else:
            message = 'Record attempted but exists: speedrun_id = {}'\
                .format(self.speedrun_id)
            logging.info(message)

    def serialize(self):
        return {
            'game_id': self.game.game_id,
            'player_id': self.player.player_id,
            'duration': self.duration
        }
