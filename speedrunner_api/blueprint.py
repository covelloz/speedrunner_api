from flask import Blueprint, jsonify
from speedrunner_api.search import Search


api = Blueprint('api', __name__)


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
