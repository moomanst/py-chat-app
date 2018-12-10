from flask import Flask, render_template
from flask_socketio import SocketIO
import hashlib

app = Flask(__name__)
app.config['SECRET_KEY'] = hashlib.sha256(b"AnotherChatApp")
socketio = SocketIO(app)

@app.route('/')
def sessions():
    return render_template('session.html')

def messageRecived(methods=['GET', 'POST']):
    print('Message Recived')

@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('recived my event: ' + str(json))
    socketio.emit('my responce', json, callback=messageRecived)


if __name__ == '__main__':
    socketio.run(app, debug=True, host='0.0.0.0', port='3000')
