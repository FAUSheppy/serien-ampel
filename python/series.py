import flask
import re

class Series:
    def __init__(self, genre, score, season, title, complete):
        self.genre    = list(filter(lambda s: s.strip() != "", genre.split(",")))
        self.score    = score
        self.season   = season
        self.title    = title
        self.complete = complete

    def getLineHTML(self, rank):
        string = flask.render_template("partials/seriesResultEntry.html", rank=rank, \
                                                                 seriesTitle=self.title, \
                                                                 seriesScore=self.score)
        return flask.Markup(string)

    def getDetailsHTML(self, rank):
        string = flask.render_template("partials/seriesResultDetails.html", score=self.score, \
                                            reason="Not Implemented", rank=rank)
        return flask.Markup(string)

    def __gt__(self, other):
        return self.score > other.score

    def __lt__(self, other):
        return self.score < other.score

    def __eq__(self, other):
        return self.title == other.title
