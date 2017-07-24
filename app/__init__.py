from flask import Flask, flash, render_template, json, request, url_for
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from flask_mail import Mail, Message

app = Flask(__name__)
app.config.from_object('config')

mail=Mail(app)

@app.route("/response", methods=['POST','GET'])
def email_response():
	if request.method == 'POST':
		_name = request.form['name']
		_email = request.form['email']
		_message = request.form['message']

		send_email(_name,_email,_message)

	return render_template("email_confirm.html")


@app.route("/signup", methods=['POST','GET'])
def signUp():
	return render_template("signup.html")

@app.route("/launchdate", methods=['POST','GET'])
def launchDate():
	if request.method == 'POST':
		_username = request.form['username']
		_phone = request.form['phone']
		_email = request.form['email']

		send_email(_username, _email, _phone)

	return render_template("launchdate.html")


@app.route("/elements")
def elements():
	return render_template('elements.html')


@app.route("/generic")
def generic():
	return render_template('generic.html')


@app.route("/giftform", methods=['POST','GET'])
def giftform():
	form = ReusableForm(request.form)
 
	print form.errors
	if request.method == 'POST':
		name=request.form['name']
		password=request.form['password']
		email=request.form['email']
		print name, " ", email, " ", password
 
	if form.validate():
		# Save the comment here.
		flash('Thanks for registration ' + name)
	else:
		flash('Error: All the form fields are required. ')

	return render_template('giftform.html', form=form)


@app.route("/", methods=['POST','GET'])
def main():
	return render_template('index.html')


class ReusableForm(Form):
	name = TextField('Name:', validators=[validators.required()])
	email = TextField('Email:', validators=[validators.required(), validators.Length(min=6, max=35)])
	password = TextField('Password:', validators=[validators.required(), validators.Length(min=3, max=35)])
 

def send_email(name, email, message):
	msg = mail.send_message(
		'You got email from an Repeat Gifts user',
		sender='bsgilber@gmail.com',
		recipients=['bsgilber@gmail.com'],
		body="The user " + name + " emailed you with the message \"" + message + ".\" You can get in touch with them at " + email + "."
		)
	return
