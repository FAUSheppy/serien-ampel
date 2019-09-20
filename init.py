#!/usr/bin/python3
import flask
import flask_login as fl
import python.backend as backend
import python.user as user
import argparse

app = flask.Flask("serien-ampel")
app.secret_key             = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'
loginManager               = fl.LoginManager()
SEPERATOR = ","

##### FRONTEND PATHS ########
@app.route('/')
def rootPage():
    footer  = flask.Markup(flask.render_template("partials/footer.html"))
    header  = flask.Markup(flask.render_template("partials/header.html"))
    navbar  = flask.Markup(flask.render_template("partials/navbar.html", user=fl.current_user))
    
    print(fl.current_user)

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
    navbar  = flask.Markup(flask.render_template("partials/navbar.html", user=fl.current_user))
    columNames = flask.Markup(flask.render_template("partials/seriesResultEntry.html", \
                                                                                seriesTitle="Title", \
                                                                                rank="#", \
                                                                                netflix="Netfix", \
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
    footer = flask.Markup(flask.render_template("partials/footer.html"))
    header = flask.Markup(flask.render_template("partials/header.html"))
    navbar  = flask.Markup(flask.render_template("partials/navbar.html", user=fl.current_user))
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


##### USER SESSION MANAGEMENT #####
@loginManager.user_loader
def load_user(userId):
    return user.User(hash(userId))

@app.route('/login', methods=['GET', 'POST'])
def login():
    footer = flask.Markup(flask.render_template("partials/footer.html"))
    header = flask.Markup(flask.render_template("partials/header.html"))
    navbar  = flask.Markup(flask.render_template("partials/navbar.html", user=fl.current_user))
    if flask.request.method == 'POST':
        username = flask.request.form['username']
        password = flask.request.form['password']        
        if password == username:
            newUser = user.User(username)
            fl.login_user(newUser)
            return flask.redirect(app.config["REDIRECT_BASE"])
        else:
            return flask.abort(401)
    else:
        return flask.render_template('login.html', navbar=navbar, footer=footer, header=header)

@app.route("/logout")
@fl.login_required
def logout():
    fl.logout_user()
    return flask.redirect(app.config["REDIRECT_BASE"])

if __name__ == "__main__":

    parser  = argparse.ArgumentParser(description="serienampel server", \
                                        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument("-i", "--interface",  default="0.0.0.0", help="Interface to listen on")
    parser.add_argument("-p", "--port",       default="5000",    help="Port to listen on")
    parser.add_argument("-s", "--servername",                    help="External hostname (i.e. serienampel.de)")
    args = parser.parse_args()

    backend.loadDB()
    loginManager.init_app(app)
    if args.servername:
        app.config['HOST']           = args.servername
        app.config['REDIRECT_BASE']  = args.servername + "/"
    else:
        app.config['REDIRECT_BASE']  = "/"

    app.run(host=args.interface, port=args.port)
