from google.appengine.ext import ndb
import user


class Play(ndb.Model):
    user = ndb.KeyProperty()
    game = 'top'
    points = 0
    round = 1
    answer = 'hai'
    order = 1
    roundPoints = 0
