import random

def make_card(promt):
    cards.append(promt)


def get_card():
    cards = ['Low-key though','The song that is the low-keyiest of bangers is ',
    'Low-key though when I was a kid', 'Low-key tho, the thing about pets is',
    'My mother was low-key right when she said',"Low-key if I didn't waste my time on YouTube",
    'The lair is low-key', 'Low-key tho, I really want to','I low-key hate it when',
    'Low-key tho, why does everyone think that', 'Low-key tho, I was this many years old when I realized',
    'I lowkey hate it when', 'I lowkey love how','I thought by now I would have',
    'Low-key, my guilty pleasure is', 'Low-key, the weirdest thing I like eating is']
    return cards[random.randint(0,len(cards)-1)] + '...'

def make_card(prompt):
    cards.append(prompt)
