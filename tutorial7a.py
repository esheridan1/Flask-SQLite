#Flask Tutorial #7 - Using SQLAlchemy Database
#https://www.youtube.com/watch?v=uZnp21fu8TQ&list=PLzMcBGfZo4-n4vJJybUVV3Un_NFS5EOgX&index=7

from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta
import sqlalchemy

app = Flask(__name__)
app.secret_key = "hello"
app.permanent_session_lifetime = timedelta(minutes=5)
 
@app.route("/")
def home():
	return render_template("index.html") 

@app.route("/login", methods=["POST", "GET"])
def login():
	if request.method=="POST":
		session.permanant = True		
		user = request.form["nm"]
		session["user"] = user
		flash("Login successful")
		return redirect(url_for("user"))
	else:
		if "user" in session:
			flash("Already logged in ")
			return redirect(url_for("user"))

		return render_template("login.html") 

@app.route("/user", methods=["POST", "GET"])
def user():
	email = None
	if "user" in session:
		user = session["user"]

		if request.method == "POST":
			email = request.form["email"]
			session["email"] = email
			flash("Email was saved")
		else:
			if "email" in session:
				email = session["email"]	
			
		return render_template("user.html", email=email)
	else:
		flash("You are not logged in")
		return redirect(url_for("login"))

@app.route("/logout")
def logout():
	flash(f"You have been logged out", "info")
	session.pop("user", None)
	session.pop("email", None)
	return redirect(url_for("login"))

if __name__ == "__main__":
	app.run(debug=True)
 