from google.appengine.ext import ndb
class game_session(ndb.Model)
      game_id = ndb.integerProperty(required=True)
      players = ndb.keyProperty(repeated=True)
      current_round_id = ndb.keyProperty

class round(ndb.Model)
     round_id = ndb.integerProperty(required=True)
     players = ndb.keyProperty(repeated=True)
     answers = ndb.stringProperty(repeated=True)

class answers(ndb.Model)
    
