from flask import Flask, request, redirect, render_template

app = Flask(__name__)

app.config['DEBUG'] = True  

@app.route("/enter", methods=['POST'])
def signup():
    username = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify']
    email = request.form['email']

    return render_template('welcome.html',username=username)


@app.route("/")
def index():
    return render_template('signup.html',title="Signup")

app.run()