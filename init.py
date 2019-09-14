#!/usr/bin/python3
import flask
import python.backend as backend

app = flask.Flask("serien-ampel")
SEPERATOR = ","

##### FRONTEND PATHS ########
@app.route('/')
def rootPage():
    footer  = flask.Markup(flask.render_template("partials/footer.html"))
    header  = flask.Markup(flask.render_template("partials/header.html"))
    navbar  = flask.Markup(flask.render_template("partials/navbar.html"))

    options = backend.getFilters()
    #["Action", "SiFi", "Anime", "Crime"]
    filters = []
    for opt in options:
        filters += [flask.Markup(flask.render_template("partials/suggest-filter-option.html", \
                                    optionName=opt))]
    return flask.render_template("home.html", header=header, footer=footer, navbar=navbar, \
                                    prerenderedFilters=filters)

@app.route("/suggest-results")
def suggestResults():
    '''This path displays results for a suggest with parameters'''
    footer  = flask.Markup(flask.render_template("partials/footer.html"))
    header  = flask.Markup(flask.render_template("partials/header.html"))
    navbar  = flask.Markup(flask.render_template("partials/navbar.html"))
    columNames = flask.Markup(flask.render_template("partials/seriesResultEntry.html", \
                                                                                seriesTitle="Title", \
                                                                                rank="#", \
                                                                                netflix="Netfix"))
    tagListString = flask.request.args.get("query")
    if not tagListString:
        raise AssertionError()
    if SEPERATOR in tagListString:
        tagList = tagListString.split(SEPERATOR)
    else:
        tagList = [tagListString]

    return flask.render_template("results.html", header=header, footer=footer, navbar=navbar,
                                    seriesList=backend.suggest(tagList), columNames=columNames)

@app.route("/search-results")
def searchResults():
    '''This path displays results for a series-search'''
    footer = flask.Markup(flask.render_template("partials/footer.html"))
    header = flask.Markup(flask.render_template("partials/header.html"))
    navbar = flask.Markup(flask.render_template("partials/navbar.html"))
    columNames = flask.Markup(flask.render_template("partials/seriesResultEntry.html", \
                                                                                seriesTitle="Title", \
                                                                                rank="#", \
                                                                                seriesScore="Rating"))
    inputString = flask.request.args.get("query")
    if not inputString:
        raise AssertionError()
    return flask.render_template("results.html", header=header, footer=footer, navbar=navbar,
                                    seriesList=backend.search(inputString), columNames=columNames)

##### STATIC FILES #####
@app.route('/static/<path:path>')
def staticFiles():
    send_from_directory('static', path)

@app.route('/defaultFavicon.ico')
def icon():
    return app.send_static_file('defaultFavicon.ico')

if __name__ == "__main__":
    backend.loadDB()
    app.run(host='0.0.0.0')
