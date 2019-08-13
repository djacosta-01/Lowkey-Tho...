import webapp2
import jinja2
import os

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
        template = the_jinja_env.get_template('templates/game.html')
        self.response.write("Username: {}".format(username))
        self.response.write(template.render())
    def get(self):
        template = the_jinja_env.get_template('templates/game.html')
        self.response.write(template.render())

class ResultsPage(webapp2.RequestHandler):
    def get(self):
        template = the_jinja_env.get_template('templates/results.html')
        self.response.write(template.render())
    def post(self):
        template = the_jinja_env.get_template('templates/results.html')
        self.response.write(template.render())

 




app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/game', GamePage),
    ('/results', ResultsPage)
], debug=True)
