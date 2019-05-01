from speedrunner_api.models import Database


class Search(Database):
    def __init__(self):
        super().__init__()

    def all_games(self):
        conn = super().make_connection()
        sql = 'SELECT game_id, game FROM Games;'
        results = conn.execute(sql).fetchall()
        super().destroy_connection(conn)
        keys = ('game_id', 'game')
        response = [dict(zip(keys, result)) for result in results]
        return response

    def games_in_category(self, category):
        conn = super().make_connection()
        sql = '''
            SELECT
                g.game_id, g.game, c.category_id, c.category
            FROM Games g
            INNER JOIN GameCategoryMap gcm
                ON g.game_id = gcm.game_id
            INNER JOIN Categories c
                ON gcm.category_id = c.category_id
            WHERE c.category = %s;
        '''
        results = conn.execute(sql, category).fetchall()
        super().destroy_connection(conn)
        keys = ('game_id', 'game', 'category_id', 'category')
        response = [dict(zip(keys, result)) for result in results]
        return response

    def top_speedruns_by_game(self, game):
        pass

    def top_speedruns_by_category(self, category):
        pass

    def all_speedruns_by_player(self, player):
        pass
