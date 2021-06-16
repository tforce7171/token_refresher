import os
import psycopg2
import requests
import json
import time
import datetime

def ProlongateToken():
    DATABASE_URL = os.environ['DATABASE_URL']
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cur = conn.cursor()
    cur.execute('SELECT * FROM wg_access_token')
    wg_access_token = dict(cur.fetchall())[1]
    print(wg_access_token)
    params = {
        "application_id" : "eda85c3d6ddbb56920d3544319a4a788",
        "access_token" : wg_access_token
    }
    base_url = "https://api.worldoftanks.asia/"
    game = "wot/"
    method = "auth/prolongate/"
    url = base_url + game + method
    result = requests.post(url, data=params)
    result_json = result.json()
    if result_json["status"] == "error":
        print(result_json["error"]["message"])
    wg_access_token = result_json["data"]["access_token"]
    print(wg_access_token)
    with conn.cursor() as cur:
        cur.execute('UPDATE wg_access_token SET wg_access_token = %s WHERE id = 1', (wg_access_token,))
        conn.commit()

if __name__ == "__main__":
    ProlongateToken()
