
from flask import Flask, jsonify, make_response
from lbcapi import api
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def call_api_get(ep):
    conn=api.hmac()
    resp = make_response(conn.call('GET', f'/api/{ep}/').json())
    resp.headers['Access-Control-Allow-Origin'] ='*'
    return resp

@app.route("/me", methods=["GET"])
def get_me():
    return call_api_get('myself')

@app.route("/ads", methods=["GET"])
def get_ads():
    return call_api_get('ads')

@app.route("/bal", methods=["GET"])
def get_bal():
    return call_api_get('wallet-balance')

@app.route("/db", methods=["GET"])
def get_db():
    return call_api_get('dashboard')

@app.route("/notif", methods=["GET"])
def get_notif():
    return call_api_get('notifications')

@app.route("/eq/<int:id>", methods=["GET"])
def get_eq(id):
    return call_api_get(f'/api/ad-equation/{id}/')

@app.route('/ad/<int:id>')
def get_ad(id):
    return call_api_get(f'/api/ad-get/{id}/')
