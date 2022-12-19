from flask import Flask,render_template, redirect, url_for, request
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return "<h1>Home Page!</h1>"

@app.route("/about")
def about():
    return "<h1>About Page</h1>"

if __name__ == '__main__':
	app.run(debug=True)