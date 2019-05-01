from speedrunner_api.models import Database


class Search(Database):
    def __init__(self):
        super().__init__()

    def _exec_query(self, sql, params=None):
        """
        Params:
            sql:= <str>
            params:= <None>/<str>/list<str>

        Returns:
            response:= list<dict<variant>> (json serializable)
        """
        conn = super().make_connection()
        if params is None:
            results = conn.execute(sql)
        else:
            results = conn.execute(sql, params)
        keys = results.keys()
        response = [
            dict(zip(keys, [str(column) for column in result]))
            for result in results.fetchall()
        ]
        super().destroy_connection(conn)
        return response

    def all_games(self):
        sql = 'SELECT game_id, game FROM Games;'
        response = self._exec_query(sql)
        return response

    def all_games_by_category(self, category):
        sql = '''
            SELECT
                g.game_id, g.game
            FROM Games g
            INNER JOIN GameCategoryMap gcm
                ON g.game_id = gcm.game_id
            INNER JOIN Categories c
                ON gcm.category_id = c.category_id
            WHERE c.category = %s;
        '''
        response = self._exec_query(sql, params=category)
        return response

    def top_speedruns_by_game(self, game):
        sql = '''
            SELECT sr.speedrun_id, p.player, sr.duration
            FROM SpeedRuns sr
            INNER JOIN Games g
                ON sr.game_id = g.game_id
            INNER JOIN Players p
                ON sr.player_id = p.player_id
            WHERE g.game = %s
            ORDER BY sr.duration ASC
            LIMIT 10;
        '''
        response = self._exec_query(sql, params=game)
        return response

    def all_speedruns_by_player(self, player):
        sql = '''
            SELECT sr.speedrun_id, g.game, sr.duration
            FROM SpeedRuns sr
            INNER JOIN Games g
                ON sr.game_id = g.game_id
            INNER JOIN Players p
                ON sr.player_id = p.player_id
            WHERE p.player = %s;
        '''
        response = self._exec_query(sql, params=player)
        return response

    def top_players_by_category(self, category):
        sql = '''
            SELECT p.player_id, p.player
            FROM SpeedRuns sr
            INNER JOIN GameCategoryMap gcm
                ON sr.game_id = gcm.game_id
            INNER JOIN Categories c
                ON gcm.category_id = c.category_id
            INNER JOIN Players p
                ON sr.player_id = p.player_id
            WHERE c.category = %s
            ORDER BY sr.duration ASC
            LIMIT 10;
        '''
        response = self._exec_query(sql, params=category)
        return response
