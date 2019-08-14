import random

def make_card(promt):
    cards.append(promt)

sub = 'hey'

def get_promt():
    cards = ['Low-key though','The song that is the lowkeyiest of bangers is ', 'Low-key though when I was a kid', 'The thing about pets is', 'My mother was low-ky right when she said','Lowkey if I did not waste my time on youtube', 'The lair is', 'Lowkey though I really want to','I hate it when', 'Why does everyone think that', 'Lowkey tho I was this many years old when I realized', 'I hate it when', 'I love how','I Thought by now I would have', '']
    return cards[random.randint(0,len(cards)-1)] + '...'

def make_card(prompt):
    cards.append(prompt)




answers = []
def get_answer():
    while len(answers)=< 5:
        answers.append(sub)
    return answers

def is_game_done():
    done = False
    if len(answers) == 5
        done = True
    return done



def get_user_model():
    pass

def get_game_from_user(user_model):
    game = Play.query().filter(Play.user == user_model).get()
    return game







def get_all_game_answers
