from flask import Flask
from flask import render_template
from flask import request


app = Flask(__name__)

@app.route('/index')
def index():
    name = request.args.get('name')
    Nobody = request.args.get('Nobody')

    if name:
        greeting = ("Hello, {} Nobody value {}".format(name, Nobody))
    else:
        greeting = "Hello World"
    return render_template("index.html", greeting=greeting)
	


@app.route('/')
def hello_world():
    greeting = "World"
    s = ('Hello, {}!'.format(greeting))
    return s 


if __name__ == "__main__":
    app.run()


