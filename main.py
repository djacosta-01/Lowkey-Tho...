import webapp2
import jinja2
import os
from database_files.cards import get_card

the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainPage(webapp2.RequestHandler):
    def get(self):
        template = the_jinja_env.get_template('templates/main.html')
        self.response.write(template.render())

class GamePage(webapp2.RequestHandler):
    def post(self):
        username = self.request.get('query')
        card = {
        "prompt": get_card()
        }
        template = the_jinja_env.get_template('templates/game.html')
        self.response.write("Username: {}".format(username))
        self.response.write(template.render(card))
    def get(self):
        username = self.request.get('query')
        card = {
        "prompt": get_card()
        }
        template = the_jinja_env.get_template('templates/game.html')
        self.response.write(template.render(card))

class ResultsPage(webapp2.RequestHandler):
    def get(self):
        template = the_jinja_env.get_template('templates/results.html')
        self.response.write(template.render())
    def post(self):
        answer = self.request.get('answer')
        self.response.write("Your answer: {}".format(answer))
        template = the_jinja_env.get_template('templates/results.html')
        self.response.write(template.render())

class JoinPage(webapp2.RequestHandler):
    def post(self):
        template = the_jinja_env.get_template('templates/join-game.html')
        # games = Game.query().fetch()
        games = ["top",  "bottom", "strange"]
        self.response.write(template.render({"games": games}))
    def get(self):
        template = the_jinja_env.get_template('templates/join-game.html')
        self.response.write(template.render())

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/join', JoinPage),
    ('/game', GamePage),
    ('/results', ResultsPage)
], debug=True)
