import flask
import sys
import re

EXPECTED_KEYS = ["title", "score", "title", "netflix", "description"]

class Series:
    def __init__(self, data, enforceComplete=False):

        # check input #
        if not "title" in data:
            raise ValueError("Series must have a title, input dict was {}".format(data))

        missing = list(filter(lambda x: x not in data, EXPECTED_KEYS))
        if missing:
            msg = "Missing Information {} for {}".format(missing, data["title"])
            if enforceComplete:
                raise ValueError(msg)
            else:
                print(msg, file=sys.stderr)

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

        if 'warning' in data:
            self.warning = "Warning: {}".format(data['warning'])
        else:
            self.warning = None

        if 'description' in data:
            self.description = data['description']
        else:
            self.description = "No Information (yet)"


    def getLineHTML(self, rank, score=-1):
        string = flask.render_template("partials/seriesResultEntry.html", rank=rank, 
											seriesTitle=self.title, netflix=self.netflix)
        return flask.Markup(string)

    def getBackgroundColor(self):
        color = None
        if self.score > 5:
            color = '#7bab7d'
        elif self.score > 3:
            color = '#ebeb7c'
        elif self.score != -1:
            color = '#e65f29'
        else:
            return ''

        return 'style=background-color:{};'.format(color)

    def getDetailsHTML(self, rank):
        string = flask.render_template("partials/seriesResultDetails.html", score=self.score, \
                                            description=self.description, warning=self.warning, rank=rank)
        return flask.Markup(string)

    def __gt__(self, other):
        return self.score > other.score

    def __lt__(self, other):
        return self.score < other.score

    def __eq__(self, other):
        return self.title == other.title

    def __hash__(self):
        return hash(self.title)

    def __cmp__(self, other):
        return self.title == other.title
