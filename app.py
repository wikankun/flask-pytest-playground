from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return 'Index Page'

@app.route('/login', methods=['POST'])
def receive_post():

    data_string = request.get_data()
    data = json.loads(data_string)

    username = data.get('username')
    password = data.get('password')

    if username == 'a_username' and password == 'a_password':
        return 'Ok', 200
    else:
        return 'Bad Request', 400

if __name__ == '__main__':
    app.run()
