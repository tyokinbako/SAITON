from flask import Flask, render_template, request, redirect

from database import Chat

app = Flask(__name__)

@app.route("/")
def hme():
    return "Hello, World!"

@app.route("/SAITON")
def saiton():
    Chats = Chat.select()
    return render_template("SAITON.html", title="ホームページ",Chats=Chats)

@app.route("/ZIRON")
def saion():
    return render_template("ZINRON.html", title="")

@app.route("/Chat",methods=['POST'])
def san():
    name = request.form['name']
    message = request.form['message']
    Chat.create(name=name, message=message)
    return redirect("/SAITON")

if __name__ == "__main__":
    app.run(debug=True)
