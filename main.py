import webapp2
import jinja2
import os
import json
from database_files.cards import get_promt, get_answer, get_user_model, is_round_fully_answered, get_play_from_user
from google.appengine.api import users
from database_files.user import User
from database_files.games import Play
# from database_files.seed import seed_data



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
        self.response.write(template.render(card))
    def get(self):
        card = {
            "prompt": get_promt()
        }
        template = the_jinja_env.get_template('templates/game.html')
        self.response.write(template.render(card))

class ResultsPage(webapp2.RequestHandler):
    def get(self):
        template = the_jinja_env.get_template('templates/results.html')
        cards=["Cece deserves more treats", "Bing is underrated", "Scoot-scoot", "this audience is great!", "I've eaten so many pop-tarts"]
        self.response.write(template.render({
            'card1':cards[0],
            'card2':cards[1],
            'card3':cards[2],
            'card4':cards[3],
            'card5':cards[4]
        }))
    def post(self):
        print('here we are')
        cards=["Cece deserves more treats", "Bing is underrated", "Scoot-scoot", "this audience is great!", "I've eaten so many pop-tarts"]
        answer = self.request.get('answer')
        user = get_user_model()
        user_session = get_play_from_user(user)
        user_session.answer = answer
        user_session.put()
        template = the_jinja_env.get_template('templates/results.html')
        print(cards)
        self.response.write(template.render({
            'answer': answer,
            'card1':cards[0],
            'card2':cards[1],
            'card3':cards[2],
            'card4':cards[3],
            'card5':cards[4]
        }))

class JoinPage(webapp2.RequestHandler):
    def post(self):
        template = the_jinja_env.get_template('templates/join-game.html')
        # games = Game.query().fetch()
        games = ["top",  "bottom", "strange"]
        self.response.write(template.render({"games": games}))
    def get(self):
        template = the_jinja_env.get_template('templates/join-game.html')
        self.response.write(template.render())

class ScoreHandler(webapp2.RequestHandler):
    def post(self):
        order = json.loads(self.request.body)['order']
        print('I RECEIVED {} FROM JAVASCRIPT'.format(order))
        play = Play.query().filter(Play.order == order).get()
        self.response.headers['Content-Type'] = 'text/plain'
        if is_round_fully_answered():
            order = json.loads(self.request.body)['order']
            print('I RECEIVED {} FROM JAVASCRIPT'.format(order))
            play = Play.query().filter(Play.order == order).get()
            play.score += 1
            play.put()
            self.response.write('true')
        else:
            self.response.write('false')


class SeedHandler(webapp2.RequestHandler):
    def get(self):
        seed_data()
        self.response.write('l0W key s33ded')

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/join', JoinPage),
    ('/game', GamePage),
    ('/results', ResultsPage),
    ('/scores', ScoreHandler)
], debug=True)
