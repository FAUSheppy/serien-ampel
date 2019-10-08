import flask
import re

class Series:
    def __init__(self, data):
        self.genre    = list(filter(lambda s: s.strip() != "", data["genre"].split(",")))
        self.score    = data["score"]
        self.season   = data["season"]
        self.title    = data["title"]
        self.complete = data["complete"]

        if 'netflix' not in data:
            self.netflix = "N/A"
        elif data['netflix']:
            self.netflix = "Yes"
        else:
            self.netflix = "No"

        if 'description' in data:
            self.description = data['description']
        else:
            self.description = "No Information (yet)"


    def getLineHTML(self, rank):
        string = flask.render_template("partials/seriesResultEntry.html", rank=rank, 
											seriesTitle=self.title, netflix=self.netflix)
        return flask.Markup(string)

    def getDetailsHTML(self, rank):
        string = flask.render_template("partials/seriesResultDetails.html", score=self.score, \
                                            description=self.description, rank=rank)
        return flask.Markup(string)

    def __gt__(self, other):
        return self.score > other.score

    def __lt__(self, other):
        return self.score < other.score

    def __eq__(self, other):
        return self.title == other.title
