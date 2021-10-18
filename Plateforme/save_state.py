
import pickle
from Performia import Performia
from Game import Game

def save_state(obj, filename):
    with open(filename, 'wb') as outp:  
        pickle.dump(obj, outp)

def load_state(obj,filename):
    with open(filename, 'rb') as inp:
        obj = pickle.load(inp)
        return obj


"""
Example of using our function
p=Performia()
G=Game()
save_state(p,'Plateforme_state.pkl')
save_state(G,'Game_state.pkl')
del G
del p
p2=Performia()
G2=Game()
p2 = load_state(p2,'Plateforme_state.pkl')
G2=load_state(G2,'Game_state.pkl')
"""

