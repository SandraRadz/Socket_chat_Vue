import copy
import json
import random

from flask import Flask, request
from flask_sockets import Sockets
import uuid

from geventwebsocket import WebSocketError

from config import DevelopmentConfig

app = Flask(__name__)
app.config.from_object(DevelopmentConfig())

sockets = Sockets(app)

connections = {}
user_uuids = {}

colors = ['aqua', 'darkcyan', 'cornflowerblue', 'cadetblue', '#5b7899', 'lightblue']
chats = {}


@sockets.route('/echo')
def echo_socket(ws):
    # while not socket.closed:
    while True:
        print(ws)
        print(ws.closed)
        print('--------')
        if not ws.closed:
            message = ws.receive()
            print(message)
            print(type(message))
            if message:
                message_json = json.loads(message)
                print(message_json)
                message_type = message_json["message_type"]
                print(message_type)
                if message_type == "new_user":
                    new_user_connection(ws, message_json)
                elif message_type == "send_message":
                    send_message(ws, message_json)
                elif message_type == "open_chat":
                    open_chat(ws, message_json)
                else:
                    ws.send("Got this!")
        else:
            print("CLOSED!!!!!!!!!!!!!!!!!")
            conn = connections.pop(ws, None)
            if conn:
                user_uuids.pop(conn['user_id'], None)
            print(user_uuids)
            break


def new_user_connection(ws, message_json):
    user_uuid = str(uuid.uuid4())
    color = select_icon_color()
    connections[ws] = {"name": message_json["user_name"], "user_id": user_uuid, "icon_color": color}
    user_uuids[user_uuid] = {"name": message_json["user_name"], "connection": ws, "icon_color": color}
    ws.send(json.dumps({"message_type": "user_id", "user_id": user_uuid}))
    send_new_user_list()


def select_icon_color():
    return colors[int(round(random.random() * len(colors), 0)) - 1]


def send_new_user_list():
    msg = {
        "message_type": "user_list",
        "user_list": list(connections.values())
    }
    print(msg)
    for conn in connections.keys():
        try:
            conn.send(json.dumps(msg))
        except WebSocketError:
            # todo delete websocket
            print("((((((((((((((((((((((((((((((((")
            pass


def send_message(ws, message_json):
    chat_from = message_json['from_user_id']
    chat_to = message_json['to_user_id']
    message = message_json['message']
    values = sorted([chat_from, chat_to])
    chat_hash = f"{values[0]}/{values[1]}"
    msg = {
        "from_id": chat_from,
        "author_name": user_uuids[chat_from]['name'],
        "to_id": chat_to,
        "text": message,
    }
    if chat_hash in chats:
        chats[chat_hash].append(msg)
    else:
        chats[chat_hash] = ([msg])
    res = {
        "message_type": "new_message",
        "new_message": msg
    }
    print(res)
    ws.send(json.dumps(res))


def open_chat(ws, message_json):
    chat_from = message_json['from_user_id']
    chat_to = message_json['to_user_id']
    values = sorted([chat_from, chat_to])
    chat_hash = f"{values[0]}/{values[1]}"
    msg = {
        "message_type": "message_list",
        "message_list": []
    }
    if chat_hash in chats:
        msg["message_list"] = chats[chat_hash]
    ws.send(json.dumps(msg))


@app.route('/')
def hello():
    return 'Hello World!'


if __name__ == "__main__":
    from gevent import pywsgi
    from geventwebsocket.handler import WebSocketHandler
    server = pywsgi.WSGIServer(('', 5000), app, handler_class=WebSocketHandler)
    server.serve_forever()