#Flask Tutorial #3 - HTML Templates
#https://www.youtube.com/watch?v=xIgPMguqyws&list=PLzMcBGfZo4-n4vJJybUVV3Un_NFS5EOgX&index=3

from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
def home():
	return render_template("index.html", content="Testing") 



if __name__=="__main__":
	app.run(debug=True)
 