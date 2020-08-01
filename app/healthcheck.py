import os
from flask import jsonify
from app import db, api


@api.route('/healthcheck', methods=['GET'])
def healthcheck():
    try:
        db.session.execute('SELECT 1')
    except:
        return jsonify({
            'status': 'unhealthy'
        }), 500
    else:
        return jsonify({
            'status': 'healthy'
        }), 200


if __name__ == '__main__':
    api.run()
