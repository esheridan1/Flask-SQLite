#Flask Tutorial #5 - Sessions
#https://www.youtube.com/watch?v=iIhAfX4iek0&list=PLzMcBGfZo4-n4vJJybUVV3Un_NFS5EOgX&index=5

from flask import Flask, redirect, url_for, render_template, request, session
from datetime import timedelta

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
		return redirect(url_for("user"))
	else:
		if "user" in session:
			return redirect(url_for("user"))

		return render_template("login.html") 

@app.route("/user")
def user():
	if "user" in session:
		user = session["user"]
		return f"<h1>{user}</h1>"
	else:
		return redirect(url_for("login"))

@app.route("/logout")
def logout():
	session.pop("user", None)
	return redirect(url_for("login"))

if __name__ == "__main__":
	app.run(debug=True)
 