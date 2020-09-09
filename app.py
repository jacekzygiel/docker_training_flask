from flask import Flask
from time import sleep
app = Flask(__name__)


@app.route('/hello')
def hello_hsbc():
    sleep(3)
    return '<h1 style="color:red;">Hello, HSBC!</h1>'


@app.route('/cheers')
def cheers_hsbc():
    return '<h1 style="color:red;">Cheers, HSBC!!</h1>'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
