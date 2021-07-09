from flask import Flask, request
from flask_sockets import Sockets

from config import DevelopmentConfig

app = Flask(__name__)
app.config.from_object(DevelopmentConfig())

sockets = Sockets(app)


@sockets.route('/echo')
def echo_socket(ws):
    # while not socket.closed:
    while True:
        message = ws.receive()
        ws.send(message)


@app.route('/')
def hello():
    return 'Hello World!'


if __name__ == "__main__":
    from gevent import pywsgi
    from geventwebsocket.handler import WebSocketHandler
    server = pywsgi.WSGIServer(('', 5000), app, handler_class=WebSocketHandler)
    server.serve_forever()