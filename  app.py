from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Flask!"

@app.route('/ping')
def ping():
    return "pong", 200

if __name__ == '__main__':
    app.run()
