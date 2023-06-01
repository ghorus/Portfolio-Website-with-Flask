from flask import render_template, url_for
#request is for GET or POST methods
from my_official_website import app

@app.route("/skills")
def skills():
    return render_template('skills.html')

@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/stats")
def stats():
    return render_template("stats.html")

@app.route("/questions")
def questions():
    return render_template("questions.html")

@app.route("/activity")
def activity():
    return render_template("activity.html")

@app.route("/todos")
def todos():
    return render_template("todos.html")

@app.route("/journey")
def journey():
    return render_template("journey.html")

@app.route("/pages")
def pages():
    return render_template("pages.html")


