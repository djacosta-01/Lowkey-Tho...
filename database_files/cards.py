import random
from google.appengine.api import users
from user import User
from games import Play


def make_card(promt):
    cards.append(promt)

sub = 'hey'

<<<<<<< HEAD
def get_promt():
    cards = ['Low-key though','The song that is the lowkeyiest of bangers is ', 'Low-key though when I was a kid', 'The thing about pets is', 'My mother was low-ky right when she said','Lowkey if I did not waste my time on youtube', 'The lair is', 'Lowkey though I really want to','I hate it when', 'Why does everyone think that', 'Lowkey tho I was this many years old when I realized', 'I hate it when', 'I love how','I Thought by now I would have', '']
=======
def get_card():
    cards = ['Low-key though','The song that is the low-keyiest of bangers is ',
    'Low-key though when I was a kid', 'Low-key tho, the thing about pets is',
    'My mother was low-key right when she said',"Low-key if I didn't waste my time on YouTube",
    'The lair is low-key', 'Low-key tho, I really want to','I low-key hate it when',
    'Low-key tho, why does everyone think that', 'Low-key tho, I was this many years old when I realized',
    'I lowkey hate it when', 'I lowkey love how','I thought by now I would have',
    'Low-key, my guilty pleasure is', 'Low-key, the weirdest thing I like eating is']
>>>>>>> 7fffff1d82aaa5142ca81970bff260a711a4dfe6
    return cards[random.randint(0,len(cards)-1)] + '...'

def make_card(prompt):
    cards.append(prompt)




answers = []
def get_answer():
    while len(answers) <= 5:
        answers.append(sub)
    return answers

def is_game_done():
    done = False
    if len(answers) == 5:
        done = True
    return done


def get_user_model():
    email = users.get_current_user().email()
    user = User.query().filter(User.email == email).get()
    return user

#check to make sure user is logged in/getuser != null
def get_play_from_user(user_model):
    play_model = Play.query().filter(Play.user == user_model.key).get()
    return play_model

def get_game_from_play_model(play_model):
    return play_model.game

def get_all_plays_from_game(game):
    plays = Play.query().filter(Play.game == game).fetch()
    return plays

def is_round_fully_answered():
    user = get_user_model()
    user_session = get_play_from_user(user)
    game = get_game_from_play_model(user_session)
    list_of_plays = get_all_plays_from_game(game)
    return len(list_of_plays) <= 5
