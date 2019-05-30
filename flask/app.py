# Arjan's first Flask program

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index(): #this function can be named anything. It defines the route of the landing page, i.e. '/'
    return 'Hello World'

@app.route('/tacos')
def tacos():
    return 'Tacos are yummy'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0') #0.0.0.0 means that this web app is accessible to any device on the current network