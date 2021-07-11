import json

from flask import Flask, request
from flask_sockets import Sockets
import uuid

from config import DevelopmentConfig

app = Flask(__name__)
app.config.from_object(DevelopmentConfig())

sockets = Sockets(app)

connections = {}
user_uuids = {}


@sockets.route('/echo')
def echo_socket(ws):
    # while not socket.closed:
    while True:
        print(ws)
        message = ws.receive()
        print(message)
        print(type(message))
        message_json = json.loads(message)
        print(message_json)
        message_type = message_json["message_type"]
        print(message_type)
        if message_type == "new_user":
            new_user_connection(ws, message_json)
        elif message_type == "send_message":
            send_message(ws, message_json)
        else:
            ws.send("Got this!")


def new_user_connection(ws, message_json):
    user_uuid = str(uuid.uuid4())
    connections[ws] = {"name": message_json["user_name"], "user_id": user_uuid}
    user_uuids[user_uuid] = {"name": message_json["user_name"], "connection": ws}
    ws.send(json.dumps({"message_type": "user_id", "user_id": user_uuid}))


def send_message(ws, message_json):
    user_uuid = str(uuid.uuid4())
    connections[ws] = {"name": message_json["user_name"], "user_id": user_uuid}
    user_uuids[user_uuid] = {"name": message_json["user_name"], "connection": ws}
    ws.send(json.dumps({"message_type": "user_id", "user_id": user_uuid}))

@app.route('/')
def hello():
    return 'Hello World!'


if __name__ == "__main__":
    from gevent import pywsgi
    from geventwebsocket.handler import WebSocketHandler
    server = pywsgi.WSGIServer(('', 5000), app, handler_class=WebSocketHandler)
    server.serve_forever()