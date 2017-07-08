from flask import Flask, request, redirect, render_template

app = Flask(__name__)

app.config['DEBUG'] = True  

def is_empty(str):
    return str == ""

def is_invalid(str):
    return len(str) < 3 or len(str) > 20

@app.route("/enter", methods=['POST'])
def signup():
    username = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify']
    email = request.form['email']
    errors = False
    u_error = ""
    p_error = ""
    v_error = ""
    e_error = ""

    if is_empty(email) is False:
        if is_invalid(email) or "." not in email or "@" not in email:
            errors = True
            e_error = "Invalid email"

    if password != verify_password:
        errors = True
        v_error = "Password and Verify Password must match"

    if is_invalid(username):
        errors = True
        u_error = "Username must be between 3 and 20 characters"
    
    if is_invalid(password):
        errors = True
        p_error = "Password must be between 3 and 20 characters"

    if is_invalid(verify_password):
        errors = True
        v_error = "Verify Password must be between 3 and 20 characters"

    if is_empty(username):
        errors = True
        u_error = "Username cannot be blank"
    
    if is_empty(password):
        errors = True
        p_error = "Password cannot be blank"

    if is_empty(verify_password):
        errors = True
        v_error = "Verify Password cannot be blank"
    
    if errors:
        return render_template('signup.html',username="value="+username,u_error=u_error,p_error=p_error,v_error=v_error,email="value="+email,e_error=e_error)
    else:
        return render_template('welcome.html',username=username)

@app.route("/")
def index():
    return render_template('signup.html',title="Signup")

app.run()