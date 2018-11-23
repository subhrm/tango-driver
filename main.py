from flask import make_response, Flask, json
import requests
from flask_cors import CORS, cross_origin
from gevent.pywsgi import WSGIServer, LoggingLogAdapter
import os
from datetime import datetime

app = Flask(__name__)

CORS(app)


@app.route("/api/hello")
def say_hello():
    return make_response("Hello")

@app.route('/api/qa', methods=['POST'])
def answer_qa():
    resp = {"answer": "I am thinking about it"}
    resp = make_response(json.dumps(resp))
    resp.headers['Content-Type'] = 'application/json'
    return resp

def start_http_server():
    '''
        Start the API server over HTTP
    '''
    # logger.info("Starting HTTP Server")
    http_server = WSGIServer(('0.0.0.0', 8080),
                             app,)
    http_server.serve_forever()

if __name__ == "__main__":
    start_http_server()