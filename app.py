from flask import Flask
app = Flask(__name__)

@app.route('/hello')
def hello_hsbc():
    return '<h1 style="color:red;">Hello, HSBC!</h1>'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
