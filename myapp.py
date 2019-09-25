from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'hello world!'


if __name__ == '__main__':

    print(__name__)
    app.run(port=7089, debug=True)
