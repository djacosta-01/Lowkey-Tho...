from google.appengine.ext import ndb
import helper.py
import user


class Play(ndb.Model):
    user = ndb.KeyProperty()
    game = 'top'
    points = 0
    round = 1
    answer = 'hai'
    order = 1
    roundPoints = 0



player = userplay()

player2 = userplay()

player3 = userplay()

player4 = userplay()

player5 = userplay()

player6 = userplay()


def game_loop():
