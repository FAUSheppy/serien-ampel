#!/usr/bin/python3
import flask
import python.backend as backend
import argparse
import markupsafe

app = flask.Flask("serien-ampel")
app.secret_key             = 'super secret key'

app.config['SESSION_TYPE']    = 'filesystem'
app.config['REDIRECT_BASE']   = "/"
app.config["ENFORCE_COMPLETE"] = False

SEPERATOR = ","
TITLE = "Serienampel"

##### FRONTEND PATHS ########
@app.route('/')
def rootPage():
    footer  = markupsafe.Markup(flask.render_template("partials/footer.html"))
    header  = markupsafe.Markup(flask.render_template("partials/header.html", websiteTitle=TITLE))
    navbar  = markupsafe.Markup(flask.render_template("partials/navbar.html", user="<disabled>"))
    
    options = backend.getFilters()
    #["Action", "SiFi", "Anime", "Crime"]
    filters = []
    for opt in options:
        filters += [markupsafe.Markup(flask.render_template("partials/suggest-filter-option.html", \
                                    optionName=opt))]
    return flask.render_template("home.html", header=header, footer=footer, navbar=navbar, \
                                    prerenderedFilters=filters)

@app.route("/suggest-results")
def suggestResults():
    '''This path displays results for a suggest with parameters'''
    footer  = markupsafe.Markup(flask.render_template("partials/footer.html"))
    header  = markupsafe.Markup(flask.render_template("partials/header.html", websiteTitle=TITLE))
    navbar  = markupsafe.Markup(flask.render_template("partials/navbar.html", user="<disabled>"))
    columNames = markupsafe.Markup(flask.render_template("partials/seriesResultEntry.html", \
                                                             seriesTitle="Title", \
                                                             rank="#", \
                                                             netflix="Netflix", \
                                                             details="Details"))
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
    footer = markupsafe.Markup(flask.render_template("partials/footer.html"))
    header  = markupsafe.Markup(flask.render_template("partials/header.html", websiteTitle=TITLE))
    navbar  = markupsafe.Markup(flask.render_template("partials/navbar.html", user="<disabled>"))
    columNames = markupsafe.Markup(flask.render_template("partials/seriesResultEntry.html", \
                                                             seriesTitle="Title", \
                                                             netflix="Netflix",\
                                                             rank="#", \
                                                             seriesScore="Rating"))
    inputString = flask.request.args.get("query")
    return flask.render_template("results.html", header=header, footer=footer, navbar=navbar,
                                    seriesList=backend.search(inputString), columNames=columNames)

##### STATIC FILES #####
@app.route('/static/<path:path>')
def staticFiles():
    send_from_directory('static', path)

@app.route('/defaultFavicon.ico')
def icon():
    return app.send_static_file('defaultFavicon.ico')


def create_app():
    backend.loadDB(app.config["ENFORCE_COMPLETE"])

if __name__ == "__main__":

    parser  = argparse.ArgumentParser(description="serienampel server", \
                                        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument("-i", "--interface",  default="0.0.0.0", help="Interface to listen on")
    parser.add_argument("-p", "--port",       default="5000",    help="Port to listen on")
    parser.add_argument("-s", "--servername",       help="External hostname (i.e. serienampel.de)")
    parser.add_argument("-e", "--enforce-complete", action="store_const", default=False, const=True,
                                                    help="Fail on any Information missing")
    args = parser.parse_args()
    if args.servername:
        app.config['REDIRECT_BASE']  = args.servername + "/"
    
    app.config["ENFORCE_COMPLETE"] = args.enforce_complete

    with app.app_context():
        create_app()

    app.run(host=args.interface, port=args.port)
