#Flask Tutorial #6 - Message flashing
#https://www.youtube.com/watch?v=iIhAfX4iek0&list=PLzMcBGfZo4-n4vJJybUVV3Un_NFS5EOgX&index=6

from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta
import sqlalchemy

app = Flask(__name__)
app.secret_key = "this is my SECRET key"
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

@app.route("/user")
def user():
	if "user" in session:
		user = session["user"]
		return render_template("user.html", user=user)
	else:
		flash("You are not logged in")
		return redirect(url_for("login"))

@app.route("/logout")
def logout():
	flash(f"You have been logged out", "info")
	session.pop("user", None)
	return redirect(url_for("login"))

if __name__ == "__main__":
	app.run(debug=True)
 