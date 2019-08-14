from google.appengine.ext import ndb
import helper.py

class user(ndb):
    googleUser_id 
    name = 'luis'

class userplay(ndb.Model):
    user = ndb.KeyProperty()
    game = 'top'
    points = 0
    round = 1
    answer = 'hai'
    position = 1
    roundPoints = 0



class answers(ndb.Model):
    player_id =


player = userplay()

player2 = userplay()

player3 = userplay()

player4 = userplay()

player5 = userplay()

player6 = userplay()
