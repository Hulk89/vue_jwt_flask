from flask import Flask, jsonify, request
from flask_cors import CORS

import jwt
from datetime import datetime, timedelta

SECRET_KEY = "hulk89-secret-key"

app = Flask(__name__)
CORS(app)

@app.route('/login', methods=('POST', ))
def login():
    data = request.get_json()
    print(data)
    if data['user'] == 'hulk' and \
       data['password'] == 'pw':
        print("login success")
        token = jwt.encode({
            'sub': 'hulk89@email.com',
            'iat': datetime.utcnow(),
            'exp': datetime.utcnow() + timedelta(minutes=30)},
        SECRET_KEY)
        return jsonify({'token': token.decode('UTF-8')})
    else:
        return jsonify({ 'message': 'Invalid credentials', 'authenticated': False }), 401


def token_required(f):
    def _verify(*args, **kwargs):
        auth_headers = request.headers.get('Authorization', '').split()
        
        invalid_msg = {
            'message': 'Invalid token. Registeration and / or authentication required',
            'authenticated': False
        }
        expired_msg = {
            'message': 'Expired token. Reauthentication required.',
            'authenticated': False
        }

        if len(auth_headers) != 2:
            return jsonify(invalid_msg), 401

        try:
            token = auth_headers[1]
            data = jwt.decode(token, SECRET_KEY)

            if data['sub'] != 'hulk89@email.com':
                raise RuntimeError('User not found')
            return f(data['sub'], *args, **kwargs)
        except jwt.ExpiredSignatureError:
            return jsonify(expired_msg), 401 # 401 is Unauthorized HTTP status code
        except (jwt.InvalidTokenError, Exception) as e:
            print(e)
            return jsonify(invalid_msg), 401

    return _verify


@app.route('/')
@token_required
def home(name):
    return "hello {}".format(name)
    

app.run()
