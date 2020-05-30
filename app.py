from flask import Flask
from datetime import datetime
import re
from flask_socketio import SocketIO
from flask import render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
socketio = SocketIO(app)

@app.route("/")
def home():
    return "Hello, Flask"

@app.route("/hello/")
@app.route("/hello/<name>")
def hello_there(name):
    return render_template(
        "hello_there.html",
        name=name,
        date=datetime.now()
    )

@app.route("/api/data")
def get_data():
    return app.send_static_file("data.json")


@app.route("/session/video")
def session():
    return render_template("session.html")

def messageReceived(methods=['GET', 'POST']):
    print('message was recieved')

@socketio.on("my event")
def handle_my_custom_event(json, methods=["GET", "POST"]):
    print('received my event: ' + str(json))
    socketio.emit('my response', json, callback=messageReceived )

if __name__ == '__main__':
    socketio.run(app, debug=True)