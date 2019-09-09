#!/usr/bin/python3
import flask
from   utils.cpwrap      import CFG
import database.database as db

app = flask.Flask(CFG("appName"))

##### FRONTEND PATHS ########
@app.route('/')
def rootPage():
    footer = flask.Markup(flask.render_template("partials/footer.html"))
    header = flask.Markup(flask.render_template("partials/header.html"))
    header = flask.Markup(flask.render_template("partials/navbar.html"))
    return flask.render_template("home.html", header=header, footer=footer)

@app.route("/search-results")
def tokenInputView():
    '''This path displays results for a suggest with parameters'''
    footer = flask.Markup(flask.render_template("partials/footer.html"))
    header = flask.Markup(flask.render_template("partials/header.html"))
    header = flask.Markup(flask.render_template("partials/navbar.html"))
    return flask.render_template("search-results.html", header=header, footer=footer)

@app.route("/suggest-results")
def viewCreate():
    '''This path displays results for a series-search'''
    footer = flask.Markup(flask.render_template("partials/footer.html"))
    header = flask.Markup(flask.render_template("partials/header.html"))
    header = flask.Markup(flask.render_template("partials/navbar.html"))
    return flask.render_template("suggest-results.html", header=header, footer=footer)

##### STATIC FILES #####
@app.route('/static/<path:path>')
def staticFiles():
    send_from_directory('static', path)

@app.route('/defaultFavicon.ico')
def icon():
    return app.send_static_file('defaultFavicon.ico')

if __name__ == "__main__":
    db.init()
    app.run(host='0.0.0.0')
