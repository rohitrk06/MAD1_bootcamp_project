from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return f'Hello, World! {6} + {7} = {6 + 7}'


if __name__ == '__main__':
    app.run(debug=True)