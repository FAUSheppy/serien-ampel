#!/usr/bin/python3
import flask

app = flask.Flask("serien-ampel")

##### FRONTEND PATHS ########
@app.route('/')
def rootPage():
    footer = flask.Markup(flask.render_template("partials/footer.html"))
    header = flask.Markup(flask.render_template("partials/header.html"))
    navbar = flask.Markup(flask.render_template("partials/navbar.html"))
    return flask.render_template("home.html", header=header, footer=footer, navbar=navbar)

@app.route("/suggest-results")
def suggestResults():
    '''This path displays results for a suggest with parameters'''
    footer = flask.Markup(flask.render_template("partials/footer.html"))
    header = flask.Markup(flask.render_template("partials/header.html"))
    navbar = flask.Markup(flask.render_template("partials/navbar.html"))
    return flask.render_template("suggest-results.html", header=header, footer=footer, navbar=navbar)

@app.route("/search-results")
def searchResults():
    '''This path displays results for a series-search'''
    footer = flask.Markup(flask.render_template("partials/footer.html"))
    header = flask.Markup(flask.render_template("partials/header.html"))
    navbar = flask.Markup(flask.render_template("partials/navbar.html"))
    return flask.render_template("search-results.html", header=header, footer=footeri, navbar=navbar)

##### STATIC FILES #####
@app.route('/static/<path:path>')
def staticFiles():
    send_from_directory('static', path)

@app.route('/defaultFavicon.ico')
def icon():
    return app.send_static_file('defaultFavicon.ico')

if __name__ == "__main__":
    app.run(host='0.0.0.0')
