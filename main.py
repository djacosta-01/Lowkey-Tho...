import webapp2
import jinja2
import os
from database_files.cards import get_promt, get_answer, get_user_model, get_play_from_user
from google.appengine.api import users
from database_files.user import User

the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

def createUser(name, email):
    user = User(
        username = name,
        email = email,
    )
    user.put()

class MainPage(webapp2.RequestHandler):
    def get(self):
        template = the_jinja_env.get_template('templates/main.html')
        google_user = users.get_current_user()
        if google_user:
            db_user = User.query().filter(User.email == google_user.email()).get()
            if not db_user:
                createUser(google_user.nickname(), google_user.email())
            logout_url = users.create_logout_url('/')
            self.response.write(template.render({
                'nickname': google_user.nickname(),
                'logout_url': logout_url
            }))
        else:
            login_url = users.create_login_url('/')
            self.response.write(template.render({
                'login_url': login_url
            }))

class GamePage(webapp2.RequestHandler):
    def post(self):
        username = self.request.get('query')
        card = {
        "prompt": get_promt()
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
        user = get_user_model()
        user_session = get_play_from_user(user)
        user_session.answer = 'answer'
        user_session.put()
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
