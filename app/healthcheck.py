import os
from flask import jsonify
from werkzeug.exceptions import HTTPException
from app import db, api


@api.route('/healthcheck', methods=['GET'])
def healthcheck():
    try:
        db.session.execute('SELECT 1')
    except:
        return jsonify({
            'status': 'fail'
        }), 503
    else:
        return jsonify({
            'status': 'pass'
        }), 200


@api.errorhandler(Exception)
def handle_exception(error):
    # handling HTTP errors
    if isinstance(error, HTTPException):
        return jsonify({
            'status': 'warn'
        }), error.code

    # handling non-HTTP erros only
    return jsonify({
        'status': 'fail'
    }), 500


if __name__ == '__main__':
    api.run()
