from flask import Flask
app = Flask(__name__)

@app.route('/')
def receive_log():
    return {'message': 'Log received!'}


