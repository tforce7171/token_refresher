from flask import Flask, request
from flask_restful import Api, Resource
from flask_cors import CORS
import json
import os
import psycopg2

app = Flask(__name__)
api = Api(app)
CORS(app)


class GetActiveToken(Resource):
    def get(self):
        conn = DBConnect()
        cur = conn.cursor()
        cur.execute('SELECT * FROM wg_access_token')
        token = dict(cur.fetchall())
        return token[1]

def DBConnect():
    DATABASE_URL = os.environ['DATABASE_URL']
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    return conn

api.add_resource(GetActiveToken, "/active_token")

if __name__ == "__main__":
    app.run()
