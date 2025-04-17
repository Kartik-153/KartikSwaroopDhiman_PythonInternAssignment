from flask import Blueprint, request, jsonify
from psycopg2.extras import RealDictCursor
from .database import get_db_connection

routes = Blueprint('routes', __name__)

@routes.route('/add-app', methods=['POST'])
def add_app():
    data = request.get_json()
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('''
        INSERT INTO info (app_name, version, description)
        VALUES (%s, %s, %s) RETURNING id
    ''', (data.get('app_name'), data.get('version'), data.get('description', '')))
    app_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({"message": "App added", "id": app_id}), 201

@routes.route('/get-app/<int:id>', methods=['GET'])
def get_app(id):
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute('SELECT * FROM info WHERE id = %s', (id,))
    app_data = cur.fetchone()
    cur.close()
    conn.close()
    if app_data:
        return jsonify(app_data)
    else:
        return jsonify({"error": "App not found"}), 404

@routes.route('/delete-app/<int:id>', methods=['DELETE'])
def delete_app(id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('DELETE FROM info WHERE id = %s RETURNING id', (id,))
    deleted = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    if deleted:
        return jsonify({"message": "App deleted"}), 200
    else:
        return jsonify({"error": "App not found"}), 404
