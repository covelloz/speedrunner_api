import csv
from datetime import datetime
from sqlalchemy import MetaData
from sqlalchemy import create_engine
from speedrunner_api.config import config


class Migration(object):
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

    def _csv_to_obj(self):
        """Converts CSV data into object

        Returns:
            data_obj:= list<OrderedDict>
        """
        with open(config.csv_path) as f:
            data_obj = list(csv.DictReader(f))
        return data_obj

    def _make_gameslist(self):
        """A unique list of games

        Returns:
            games:= list<dict<str>>
        """
        data_obj = self._csv_to_obj()
        games = list(set([row['Game'] for row in data_obj]))
        games_obj = [{'game': game} for game in games]
        return games_obj

    def _insert_games(self):
        """Insert game titles into database"""
        games_obj = self._make_gameslist()
        for obj in games_obj:
            obj['create_date'] = datetime.now()
            obj['modify_date'] = datetime.now()

        conn = self.engine.connect()
        conn.execute(self.games_table.insert(), games_obj)
        conn.close()
