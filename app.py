from flask import Flask, request, jsonify, redirect
import psycopg2
from dotenv import load_dotenv
import os


app = Flask(__name__)

conn = psycopg2.connect(dbname="pyServe", user=os.environ.get("DBUSER"), password=os.environ.get("DBPASS"), host=os.environ.get("DBHOST"), port=os.environ.get("DBPORT"))

@app.route('/')
def index():
	return 'Hello, Flask!'

@app.route('/control', methods=['GET', 'POST'])
def control():
	arr = [1, 2, 3]
	print(request.method)
	if request.method == 'GET':
		return arr

@app.route('/inserter', methods=['GET'])
def insertions():
    r = None

    cur = conn.cursor()
    try:
        cur.execute(
					""" CREATE TABLE IF NOT EXISTS first (
										book_id serial PRIMARY KEY,
										name TEXT)"""
        )

    except Exception as error:
        conn.commit()
        cur.close()
        return jsonify({"error": "ERROR"}), 500

    conn.commit()
    cur.close()
    return jsonify({"message":"OK"}), 200



if __name__ == '__main__':
	app.run(host='0.0.0.0',port=8000)