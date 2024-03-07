import random

from flask import Flask, render_template,request
from dotenv import load_dotenv

load_dotenv()
def create_app():
    app = Flask(__name__)

    @app.route("/",methods=["GET","POST"])
    def home():
        characters = list('abcdefghijklmnopqrstuvwxyz')
        if request.form.get("uppercase"):
            characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
        if request.form.get("special"):
            characters.extend(list('!@#$%&*'))
        if request.form.get("numbers"):
            characters.extend(list('1234567890'))
        length = int(request.form.get("length") or 12)
        password = ''
        for x in range(length):
            password += random.choice(characters)
        return render_template("home.html",password=password)

    @app.route("/about/")
    def about():
        return render_template("about.html")
    return app

app = create_app()

if __name__ == '__main__':
    app.run()