import random 



cards = ['Low-key though','The song that is the lowkeyiest of bangers is ', 'Low-key though when I was a kid', 'The thing about pets is', 'My mother was low-ky right when she said','Lowkey if I did not waste my time on youtube', 'The lair is']

class user:
  def __init__(self, name, accont):
    self.name = name
    self.accont = accont

p1 = user("John", 36)



def make_card(promt):
    cards.append(promt)


def get_card():
    cards[random.randint(0,len(cards))] + '...'

def make_card(prompt):
    cards.append(prompt)
