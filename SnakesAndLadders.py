'''
Created on Feb 23, 2013

@author: Harry
'''

import pygame, sys, random
class player:
    def __init__(self, name, data, position, lock, multiplier,territories):
        '''Initialize this player to have given data, position, status'''
        self._name=name
        self._data=data
        self._position=position
        self._lock=lock
        self._multiplier=multiplier
        self._territories=territories
    def name(self):
        '''Returns the name of the player if inputted or the player number'''
        return self._name
    def data(self):#Type of data the player wants to use
        '''Returns the data for the player or None if data has not been chosen'''
        return self._data
    def position(self):#Where the player is on the board
        '''Returns the position of the player'''
        return self._position
    def lock(self):#Locks player into the data they chose
        '''Returns an int if the player is locked into a data set or None otherwise'''
        return self._lock
    def multiplier(self):
        return self._multiplier
    def territories(self):
        return self._territories
    def change_name(self, name):
        '''Changes the name of the player'''
        self._name=name
    def change_data(self, data):
        '''Changes the data chosen by the player'''
        self._data=data
    def change_position(self, movement):#Moves the pieces
        '''Changes the position of the player based on the movement value'''
        self._position+=movement
    def change_lock(number):
        self._lock=number
    def change_multiplier(number):
        self._multipler=number
    def get_territory(territory):
        self._territories.append(territory)
    def remove_territory(territory):
        self._territories.remove(territory)

"""PLAYERS"""#Current max of 4 players
player1=player('Player 1', None, 0, None, 1,[])
player2=player('Player 2', None, 0, None, 1,[])
player3=player('Player 3', None, 0, None, 1,[])
player4=player('Player 4', None, 0, None, 1,[])
players=[player1,player2,player3,player4]

##def number_of_players(number):#Chooses how many players that the user wants in the current game
##    all_players=[player1,player2,player3,player4]
##    players=[]
##    for i in range(number-1):
##        players.append(all_players[i])
##    return players

def random_subtract(player, data):
    if player.multipler()!=1:
        new_data=[]
        for i in player.data():
            new_data.append(i*player.multiplier())
        player.change_data(new_data)
        player.change_multiplier(1)
    return data[random.randint(0,len(data)-1)]-data[random.randint(0,len(data)-1)]

def dice_roll(player, data):
    result=random_subtract(player, data)
    if result <= -2:
        return 1
    elif result<-2 and result>0:
        return 2
    elif result==0:
        return 3
    elif result<0 and result>2:
        return 4
    elif result>=2 and result<5:
        return 5
    elif result >=5:
        return 6

def triple_dice_roll(player, data):
    rolls=[]
    for roll in range(3):
        rolls.append(dice_roll(player, data))
    return rolls[0], rolls[1], rolls[3], sum(rolls)//3

def movement(player, spaces):
    '''Moves the piece'''
    return player.change_position(spaces)

def check_player_data_lock(player):
    if player.lock()==None:
        return
    elif player.lock()!= None and player.lock() != 0:
        turns_left=player.lock()-1
        player.change_lock(turns_left)
        print("Player's data control will be returned in {} turns.".format(player.data()))
    elif player.lock()==0:
        print("Player's data control has been returned.")
        player.change_lock(None)


def snakes_and_ladders(player):
    if player.position()==1:
        movement(player,10)
    elif player.position()==7:
        movement(player,-3)
    elif player.position()==5 or 11 or 20:
        movement(player,11)
    elif player.position()==10 or 21:
        movement(player,-8)
    elif player.position()==15:
        movement(player,8)
    elif player.position()==24:
        movement(player,-18)
    elif player.position()==33:
        movement(player,-14)

def affectors(player):
    if player.position()==2 or 16 or 31:#Halves on spaces 2,16,31
        player.change_multiplier(1/2)
    elif player.position==6 or 26 or 29:#Doubles on spaces 6,26,29
        player.change_multiplier(2)
    elif player.position==19 or 22 or 25:#Locks data set on spaces 19,22,25
        player.change_lock(3)

def winning_player(player):#I'll figure this out later.
    if player.position()==34:
        return
def battle(attacker,defender,territory):
    attacker_roll=triple_dice_roll(attacker,attacker.data())[3]
    defender_roll=triple_dice_roll(defender,defender.data())[3]
    if attacker_roll>defender_roll:
        attacker.get_territory(territory)
        defender.remove_territory(territory)

def player_territory_check(player):
    if len(player.territories)==0:
        pass
##def game():
##    _display = pygame.display.set_mode((600, 480), 0, 32)
##    pygame.display.set_caption('Snakes and Ladders')
    
test_data=[75,60,80,65,63,91,72,73,70,67]       
