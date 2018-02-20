from flask import render_template

from flask import Flask

app = Flask(__name__)

@app.route('/', methods=["GET"])
def index():
    return render_template("main_page.html")
git init
