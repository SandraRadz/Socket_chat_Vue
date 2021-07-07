from flask import Flask
from flask_socketio import SocketIO, emit


from config import DevelopmentConfig

app = Flask(__name__)
app.config.from_object(DevelopmentConfig())

socketio = SocketIO(app, cors_allowed_origins='*', logger=True, engineio_logger=True)


@socketio.on('connect')
def connect():
    print("Connected")
    emit('MESSAGE1', ["Message from server"])


@socketio.on('disconnect')
def disconnect():
    print('Client disconnected')


@socketio.on('send_message')
def client_send_message(data):
    print("client sent message")
    print(data)


if __name__ == '__main__':
    socketio.run(app)