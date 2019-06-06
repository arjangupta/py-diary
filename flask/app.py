# Arjan's first Flask program

from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

num_tacos = 0

@app.route('/')
def index(): #this function can be named anything. It defines the route of the landing page, i.e. '/'
    return render_template("index.html")

@app.route('/tacos', methods=['POST'])
def tacos():
    global num_tacos
    print("Taco endpoint is being hit")
    num_tacos += 1
    socketio.emit('tacoUpdate', num_tacos)
    return f"You have requested {num_tacos} tacos!\n" 

if __name__ == '__main__':
    socketio.run(app, debug=True, host='0.0.0.0') #0.0.0.0 means that this web app is accessible to any device on the current network