from flask import Flask
from flask import render_template, redirect, url_for, request
app = Flask(__name__)


@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      return redirect(url_for('success',name = user))
   else:
      user = request.args.get('nm')
      return redirect(url_for('success',name = user))


@app.route('/')
def index():
	greeting = "Hello World from Kavis Mac"
	return render_template("index.html", greeting=greeting)

@app.route('/hello')
def hello_world():
	greeting="world"
	f = "I\'m the greatest women on this planet"
	return f

@app.route('/python/')
def hello_python():
   return 'Hello Python'


@app.route('/guest/<guest>')
def hello_guest(guest):
   return 'Hello %s as Guest' % guest

@app.route('/user/<name>')
def hello_user(name):
   if name =='admin':
      return redirect(url_for('hello_admin'))
   else:
      return redirect(url_for('hello_guest',guest = name))


if __name__ == '__main__':
	#app.run(debug = True)
	app.run()
#	app.add_url_rule(‘/’, ‘hello’, hello_world)
	#app.run()
