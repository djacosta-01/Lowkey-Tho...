from google.appengine.ext import ndb
import user

class Play(ndb.Model):
    user = ndb.KeyProperty(user.User, required=True)
    game = ndb.StringProperty(default='top')
    points = ndb.IntegerProperty(default=0)
    round = ndb.IntegerProperty(default=1)
    answer = ndb.StringProperty(default='hai')
    order = ndb.IntegerProperty(default=1)
    roundPoints = ndb.IntegerProperty(default=0)
