#Flask Tutorial #1 - How to Make Websites with Python
#https://www.youtube.com/watch?v=mqhxxeeTbu0&list=PLzMcBGfZo4-n4vJJybUVV3Un_NFS5EOgX

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
	return "Hello!  This is the main page <h1>HELLO<h1>"  

# In this revision we can return the name added to the URL

@app.route("/<name>")
def user(name):
	return f"Hello {name}!"	

if __name__=="__main__":
	app.run()
