from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


# create a Flask instance.
app = Flask(__name__) # helps flask find all our files in the dir here. 
app.config['SECRET_KEY'] = "my super secret key that no one is supposed to know"

# create a form class
class NamerForm(FlaskForm):
	name = StringField("What's your name", validators=[DataRequired()])
	submit = SubmitField('Submit')


# create a route decorator 
@app.route("/")

# def index():
# 	return "<h1>Hello World</h1>"

def index():
	favorite_pizza = ['Pepperoni', 'Cheese', 'Mushrooms', 41]
	first_name = "JOhN"
	stuff = "This is text.                  "
	return render_template('index.html', 
		user_name=first_name,
		stuff=stuff,
		favorite_pizza=favorite_pizza)



# a route for users.
@app.route("/user/<name>")
def user(name):
	return render_template('user.html', username = name)


# create name page
app.route("/name", methods=['GET', 'POST'])
def name():
	name = None
	form = NamerForm()
	# Validate Form
	if form.validate_on_submit():
		name = form.name.data
		form.name.data = ''

	return render_template('nameform.html',
		name = name,
		form = form)

app.route('/nameform')
def name1():
	return render_template('user.html')


# safe capitalize lower upper title trim striptags
# create Custom error page.
# 1. invalid url
@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404

# 1. Server Error url
@app.errorhandler(500)
def page_not_found(e):
	return render_template('500.html'), 500

