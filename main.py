import os
from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
 return '<h1>Hello World!</h1>'

@app.route('/unifran')
def unifran():
 return '<h2>Universidade de Franca</h2>'

if __name__ == "__main__":
 port = int(os.environ.get("PORT", 5000))
 app.run(host='0.0.0.0', port=port)
