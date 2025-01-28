from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wrapper():
        return f'<b>{function()}</b>'

    return wrapper


def make_underlined(function):
    def wrapper():
        return f'<u>{function()}</u>'

    return wrapper


def make_emphasized(function):
    def wrapper():
        return f'<em>{function()}</em>'

    return wrapper


@app.route("/")
def hello():
    return 'Hello, Flask'


@app.route("/bye")
@make_bold
@make_underlined
@make_emphasized
def bye():
    return 'Bye, Flask'


@app.route('/username/<name>')
def greet(name):
    return f'Hello there, {name}'


if __name__ == '__main__':
    app.run(debug=True)
