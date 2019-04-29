import csv
from datetime import datetime
from speedrunner_api.config import config
from speedrunner_api.models import Database
from speedrunner_api.models import Game, Category


class Migration(Database):

    def __init__(self):
        super().__init__()

    def exec_migration(self):
        """Initiates Migration"""
        self._insert_records('Games')
        self._insert_records('Categories')
        self._insert_records('Players')
        self._insert_records('GameCategoryMap')

    def _csv_to_obj(self):
        """Converts CSV data into object

        Returns:
            data_obj:= list<OrderedDict>
        """
        with open(config.csv_path) as f:
            data_obj = list(csv.DictReader(f))
        return data_obj

    def _make_games(self):
        """A unique list of games

        Returns:
            games_obj:= list<dict<str>>
        """
        data_obj = self._csv_to_obj()
        games = list(set([row['Game'] for row in data_obj]))
        games_obj = [{'game': game} for game in games]
        return games_obj

    def _make_categories(self):
        """A unique list of categories

        Returns:
            categories_obj:= list<dict<str>>
        """
        data_obj = self._csv_to_obj()
        categories = [row['Categories'] for row in data_obj]
        cleaned_categories = self._clean_categories(categories)
        categories_obj = [{'category': cc} for cc in cleaned_categories]
        return categories_obj

    def _make_players(self):
        """A unique list of players

        Returns:
            players_obj:= list<dict<str>>
        """
        data_obj = self._csv_to_obj()
        players = list(set([row['Player'] for row in data_obj]))
        players_obj = [{'player': player} for player in players]
        return players_obj

    def _make_gamecategorymap(self):
        data_obj = self._csv_to_obj()
        mapping = [{
            'game': row['Game'],
            'categories': self._clean_categories([row['Categories']])
         } for row in data_obj]
        # flatten
        flat_mapping = []
        for gcm in mapping:
            for category in gcm['categories']:
                flat_mapping.append((gcm['game'], category))
        # reduce/map
        gc_map = list(set(flat_mapping))
        gc_map = [{'game': x[0], 'category': x[1]} for x in gc_map]
        # re-map with database ids
        gamecategorymap_obj = []
        for gc in gc_map:
            game_id = Game(gc['game']).game_id
            category_id = Category(gc['category']).category_id

            gamecategorymap_obj.append({
                'game_id': game_id,
                'category_id': category_id
            })
        return gamecategorymap_obj

    def _clean_categories(self, categories):
        """Cleans up concatenated category strings

        Params:
            categories:= list<str>
        Returns:
            cleaned_categories:= list<str>
        """
        _categories = []
        for category in categories:
            cat_split = category.replace('%', '').split(',')
            for cat in cat_split:
                _categories.append(cat.strip())
        cleaned_categories = list(set(_categories))
        return cleaned_categories

    def _insert_records(self, target_table):
        """Inserts records into the database"""
        if target_table == 'Games':
            table = self.games_table
            record_obj = self._make_games()
        elif target_table == 'Categories':
            table = self.categories_table
            record_obj = self._make_categories()
        elif target_table == 'Players':
            table = self.players_table
            record_obj = self._make_players()
        elif target_table == 'GameCategoryMap':
            table = self.gamecategorymap_table
            record_obj = self._make_gamecategorymap()

        # Add timestamps
        for obj in record_obj:
            obj['create_date'] = datetime.now()
            obj['modify_date'] = datetime.now()

        conn = super().make_connection()
        conn.execute(table.insert(), record_obj)
        super().destroy_connection(conn)
