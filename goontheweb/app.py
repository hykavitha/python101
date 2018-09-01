from flask import Flask
from flask import render_template, redirect, url_for, request
app = Flask(__name__)



@app.route('/')
def index():
	greeting = "Hello World from Kavis Mac"
	return render_template("index.html", greeting=greeting)

@app.route('/hello')
def hello_world():
	greeting="world"
	f = "I\'m the greatest women on this planet"
	return f

@app.route('/guest/<guest>')
def hello_guest(guest):
   return 'Hello %s as Guest' % guest

@app.route('/user/<name>')
def hello_user(name):
   if name =='admin':
      return redirect(url_for('hello_admin'))
   else:
      return redirect(url_for('hello_guest',guest = name))



@app.route('/admin')
def hello_admin():
   return 'This is admin page'


@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      return redirect(url_for('success',name = user))
   else:
      user = request.args.get('nm')
      return redirect(url_for('success',name = user))


if __name__ == '__main__':
	#app.run(debug = True)
#	app.add_url_rule(‘/’, ‘hello’, hello_world)
	app.run()
