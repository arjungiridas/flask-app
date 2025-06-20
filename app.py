from flask import Flask app

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello from Flask with CI/CD!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

