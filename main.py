from flask import Flask, render_template, request, redirect, url_for

import emag_db

app = Flask(__name__)
config = emag_db.read_config()
user_id, username, password = emag_db.read_admins(config)

users = {
    username: password
}



@app.route("/")
def first_function():
    print("a rulat")
    return render_template("login.html")


@app.route("/test")
def second_function():
    print("a rulat")
    return render_template("test.html")



@app.route("/login", methods=["POST"])
def web_login():
    user = request.form['username']
    passwd = request.form['password']


    if user in users.keys():
        if passwd == users[user]:
            data = emag_db.read_products(config)
            return render_template("home.html", data=data)

    return render_template("login.html")






if __name__ == '__main__':
    app.run()
