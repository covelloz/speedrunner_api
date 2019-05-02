from flask import Blueprint, jsonify, request, abort
from speedrunner_api.search import Search
from speedrunner_api.models import Game, Category, Player
from speedrunner_api.models import GameCategoryMap, SpeedRun


api = Blueprint('api', __name__)


# Search Routes
@api.route('/all-games', methods=['GET'])
def all_games():
    return jsonify(Search().all_games())


@api.route('/all-games/category/<string:category>',  methods=['GET'])
def all_games_by_category(category):
    return jsonify(Search().all_games_by_category(category))


@api.route('/top/speedruns/game/<string:game>',  methods=['GET'])
def top_speedruns_by_game(game):
    return jsonify(Search().top_speedruns_by_game(game))


@api.route('/all/speedruns/player/<string:player>',  methods=['GET'])
def all_speedruns_by_player(player):
    return jsonify(Search().all_speedruns_by_player(player))


@api.route('/top/players/category/<string:category>',  methods=['GET'])
def top_players_by_category(category):
    return jsonify(Search().top_players_by_category(category))


# POST requests
@api.route('/add-game', methods=['GET', 'POST'])
def add_game():
    if request.method == 'POST':
        content = request.get_json()
        try:
            game = Game(content['game'])
        except KeyError:
            return jsonify({
                'content': {},
                'message': r'Bad payload'
            })
        message = game.insert_record()
        return jsonify({
            'content': {
                'game_id': game.game_id,
                'game': game.game
            },
            'message': message
        })
    else:
        return abort(400)


@api.route('/add-category', methods=['GET', 'POST'])
def add_category():
    if request.method == 'POST':
        content = request.get_json()
        try:
            game = Game(content['game'])
            category = Category(content['category'])
        except KeyError:
            return jsonify({
                'content': {},
                'message': r'Bad payload'
            })
        gamecategorymap = GameCategoryMap(game.game, category.category)
        message = gamecategorymap.insert_record()
        return jsonify({
            'content': {
                'gamecategorymap_id': gamecategorymap.gamecategorymap_id,
                'game_id': game.game_id,
                'game': game.game,
                'category_id': category.category_id,
                'category': category.category
            },
            'message': message
        })
    else:
        return abort(400)


@api.route('/add-speedrun', methods=['GET', 'POST'])
def add_speedrun():
    if request.method == 'POST':
        content = request.get_json()
        try:
            game = Game(content['game'])
            player = Player(content['player'])
            duration = content['duration']
        except KeyError:
            return jsonify({
                'content': {},
                'message': r'Bad payload'
            })
        speedrun = SpeedRun(game.game, player.player, duration)
        message = speedrun.insert_record()
        return jsonify({
            'content': {
                'speedrun_id': speedrun.speedrun_id,
                'game_id': game.game_id,
                'game': game.game,
                'player_id': player.player_id,
                'player': player.player,
                'duration': speedrun.duration
            },
            'message': message
        })
    else:
        return abort(400)
