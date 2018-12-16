from flask import Flask
from flask import Response, request
from functools import wraps

app = Flask(__name__)

def enableBasicAuth():
    return Response(
        'Could not verify your access level for that URL.\n'
        'You have to login with proper credentials', 401,
        {'WWW-Authenticate': 'Basic realm="Login Required"'})

def requireAuth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or auth.username != 'gini' or auth.password != 'gini':
            return enableBasicAuth()
        return f(*args, **kwargs)
    return decorated

@app.route('/')
@requireAuth
def main():
    return "successful"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)