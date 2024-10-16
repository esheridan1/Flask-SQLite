#Flask Tutorial #1 - How to Make Websites with Python
#https://www.youtube.com/watch?v=mqhxxeeTbu0&list=PLzMcBGfZo4-n4vJJybUVV3Un_NFS5EOgX

from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
	return "Hello!  This is the main page <h1>HELLO<h1>"  



@app.route("/<name>")
def user(name):
	return f"Hello {name}!"	

# In this revision we do a redirect. 
@app.route("/admin")
def admin():	
	return redirect(url_for("home"))   # home is the name of the function, NOT the specific URL.

if __name__=="__main__":
	app.run()
