# Python Text RPG
# (Game Title)
# Made by Tyron Margaret

import cmd
import textwrap
import sys
import time
import os
import random

screen_width = 100

#### Player Setup ####
class player:
    def __init__(self):
        self.game_over = False
        self.name = ''
        self.gender = ''
        self.age = '19'
        self.light = 0
        self.hp = 0
        self.sanity = 0
        self.mp = 0
        self.status_effects = []
        self.strength = 0
        self.dexterity = 0
        self.agility = 0
        self.intelligence = 0
        self.location = 'start'
        self.weapon = 'Broken Estoc'
        self.armour = 'Ruined Breastplate'
        self.inventory = [[weapon], [armour]]
        self.spells = []

my_player = player()

#### Title Screen ####
def title_screen_selections():
    option = input('> ')
    if option.lower() == ('play'):
        start_game() # Placeholder unit (for now!)
    elif option.lower() == ('help'):
        help_menu()
    elif option.lower() == ('quit'):
        sys.exit()
    while option.lower() not in play ['play', 'help', 'quit']:
        print('Please enter a valid command.')
        option = input('> ')
        if option.lower() == ('play'):
            start_game() # Placeholder unit (for now!)
        elif option.lower() == ('help'):
            help_menu()
        elif option.lower() == ('quit'):
            sys.exit()

def title_screen():
    os.system(cls)
    print('############################')
    print('# Welcome to the text RPG! #')
    print('############################')
    print('          - Play -          ')
    print('          - Help -          ')
    print('          - Quit -          ')
    print('Made by Tyron Margaret, 2018')
    title_screen_selections()

def help_menu():
    print('############################')
    print('# Welcome to the text RPG! #')
    print('############################')
    print('- Use up, down, left or right to move -')
    print('- Type your commands to do perform actions -')
    print('- Use "look" to inspect something -')
    print('- Good luck, try to survive and I wish you the very best of reading pleasure!')
    title_screen_selections()

#### Game Interactivity ###
def print_location():
    print('\n' + ('#' * (4 + len(my_player.location))))
    print('#' + my_player.location.upper + '#')
    print('#' + zone_map [my_player.position] [description] + '#')
    print('\n' + ('#' * (4 + len(my_player.location))))

def prompt():
    print('\n' + '===================')
    print('> What action will you perpetrate?')
    action = input('> ')
    acceptable_actions = ['move', 'go', 'travel', 'walk', 'quit', 'examine', 'inspect', 'interact', 'look']
    while action.lower() not in acceptable_actions:
        print('Unknown action has been specified, try to perpertrate an acceptable one.\n')
        action = input('> ')
    if action.lower() == 'quit':
        sys.exit()
    elif action.lower in ['move','go', 'travel', 'walk']:
        player_move(action.lower())
    elif action.lower in ['examine', 'inspect', 'interact', 'look']:
        player_examine(action.lower())

def player_move(action):
    ask = 'In which direction will you lumber?\n'
    dest = input(ask)
    if destination == ['up', 'north']:
        destination = zone_map [my_player.location] [up]
        movement_handler(destination)
    elif dest == ['down', 'south']:
        destination = zone_map [my_player.location] [down]
        movement_handler(destination)
    elif dest == ['left', 'west']:
        destination = zone_map [my_player.location] [left]
        movement_handler(destination)
    elif dest == ['right', 'east']:
        destination = zone_map [my_player.location] [right]
        movement_handler(destination)

def movement_handler(destination):
    print('\n' + 'You have relocated to ' + destination + '.')
    my_player.location = destination
    print_location()

def player_examine(action):
    if zone_map [my_player.location] [solved] == True:
        print('Your efforts have already been spent.')
    else:
        print('Your valiant effort continues here in the room.')

#### Game Functionality ####
def start_game():
    return

def main_game_loop():
    while my_player.game_over == False:
        prompt()
        # handle if player escaped Dimmest Pine alive

def setup_game():
    os.system('clear')

def print_text(message, speed):
    for character in message:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(speed)

#### Name Handling ####
    print_text('In all of the realms you\'re the secondborn child of king Tonir Scrum, with lots of love he named you...?\n', 0.05)
    player_name = input('> ')
    if player_name == input('> '):
        player_name = 'Arden'
    my_player.name = player_name
    print_text('Then your name will be spiral throughout the eons as ' + player_name + '!', 0.05)

#### Gender Handling ####
    os.system('clear')
    print_text('Is that name befitting of a man or a woman?\n', 0.05)
    player_gender = input('> ')
    acceptable_genders = ['man', 'woman']
    my_player.gender = player_gender
    if player_gender.lower in acceptable_genders:
        my_player.gender = player_gender
        print_text('Forever more you will be a ' + player_gender + '.', 0.05)
    elif player_gender.lower == '> ':
        player_gender = 'man'
        print_text('Forever more you will be a ' + player_gender + '.', 0.05)
    while player_gender.lower not in acceptable_genders:
        player_gender = input('> ')
        if player_gender.lower == acceptable_genders:
            my_player.gender = player_gender
            print_text('Forever more you will be a ' + player_gender + '.', 0.05)

#### Player Stat Assignment ####
    if my_player.gender is 'man':
        self.hp = 25
        self.mp = 15
        self.sanity = 100
        self.strength = 4
        self.dexterity = 2
        self.agility = 2
        self.intelligence = 3
    elif my_player.gender is 'woman':
        self.hp = 15
        self.mp = 25
        self.sanity = 100
        self.strength = 2
        self.dexterity = 2
        self.agility = 3
        self.intelligence = 4

#### Prologue ####
        print_text('Enjoy your stay on this vivid world!', 0.03)
        print_text('May it greet you with plentiful frevor.', 0.05)
        print_text('Take heed of the warnings, ' + player_name + '...', 0.2)
        print_text('Don\'t trust anyone...', 0.1)

        os.system('clear')
        print('####################################')
        print('#            Connecting...         #')
        print('####################################')

        main_game_loop()

title_screen()


#### Map ####
"""
a1 a2 ...    # PLAYER STARTS AT B2!
-------------
|  |  |  |  | a4
-------------
|  | x|  |  | b4 ...
-------------
|  |  |  |  |
-------------
|  |  |  |  |
-------------
|  |  |  |  |
-------------
# EXIT IS AT A2!
# WORLD EATER IS AT E3!
"""
zone_name = ''
description = 'description'
examination = 'examine'
solved = False
up = 'up',
down = 'down',
left = 'left',
right = 'right',

solved_places = {'a1': False, 'a2': False, 'a3': False, 'a4': False,
                 'b1': False, 'b2': False, 'b3': False, 'b4': False,
                 'c1': False, 'c2': False, 'c3': False, 'c4': False,
                 'd1': False, 'd2': False, 'd3': False, 'd4': False,
                 'e1': False, 'e2': False, 'e3': False, 'e4': False
                }

zone_map = {
     'a1': {
         zone_name: 'A pleasant Respite'
         description = 'description'
         examination = 'examine'
         solved = False
         up = 'up', 'north', '8', 'w'
         down = 'down', 'south', '2', 's'
         left = 'left', 'west', '4', 'a'
         right = 'right', 'east', '6', 'd'
    },
        'a2': {
        zone_name: 'Closed Circle'
        description = 'description'
        examination = 'examine'
        solved = False
        up = 'meteorexit',
        down = 'down', 'south', '2', 's'
        left = 'left', 'west', '4', 'a'
        right = 'right', 'east', '6', 'd'
    },
        'a3': {
        zone_name: 'Rocks Fall, You Might Die...'
        description = 'description'
        examination = 'examine'
        solved = False
        up = 'b3',
        down = 'wall',
        left = 'a2',
        right = 'a4',
    },
        'a4': {
        zone_name: 'An Most Unfortunate Encounter'
        description = 'description'
        examination = 'examine'
        solved = False
        up = 'b4',
        down = 'wall',
        left = 'a3',
        right = 'wall',
    },
        'b1': {
        zone_name: 'Tragic Reunion'
        description = 'You continue westward and after what feels to be a half hour. You find yourself near by wall, a body lies propped up against it.'
        examination = 'As you kneel to inspect the body, your attention is drawn to an amulet. It has the same insignia as yours, the house of Scrum. It\'s your eldest brother, Braedo.'
        solved = False
        up = 'c1',
        down = 'a1',
        left = 'wall',
        right = 'b2',
    },
        'b2': {
        zone_name: 'No Way Home'
        description = 'You stand a fair distance away from the mouth of the meteorite entrance, if you squint you can barely see the beams of light piercing past the boulder.'
        examination = 'Before you is complete blackness and from the sides as well... And diagonally too. Luckily, you have your lantern and some fuel.'
        solved = False
        up = 'a2',
        down = 'c2',
        left = 'b1',
        right = 'b3',
    },
        'b3': {
        zone_name: 'No Way Home'
        description = 'You stand a fair distance away from the mouth of the meteorite entrance, if you squint you can barely see the beams of light piercing past the boulder.'
        examination = 'Before you is complete blackness and from the sides as well... And diagonally too. Luckily, you have your lantern and some fuel.'
        solved = False
        up = 'a2',
        down = 'c2',
        left = 'b1',
        right = 'b3',
    },
        'b4': {
        zone_name: ''
        description = ''
        examination = ''
        solved = False
        up = 'a2',
        down = 'c2',
        left = 'b1',
        right = 'b3',
    },
        'c1': {
        zone_name: ''
        description = ''
        examination = ''
        solved = False
        up = 'a2',
        down = 'c2',
        left = 'b1',
        right = 'b3',
    },
        'c2': {
        zone_name: ''
        description = ''
        examination = ''
        solved = False
        up = 'a2',
        down = 'c2',
        left = 'b1',
        right = 'b3',
    },
        'c3': {
        zone_name: ''
        description = ''
        examination = ''
        solved = False
        up = 'a2',
        down = 'c2',
        left = 'b1',
        right = 'b3',
    },
        'c4': {
        zone_name: ''
        description = ''
        examination = ''
        solved = False
        up = 'a2',
        down = 'c2',
        left = 'b1',
        right = 'b3',
    },
        'd1': {
        zone_name: ''
        description = ''
        examination = ''
        solved = False
        up = 'a2',
        down = 'c2',
        left = 'b1',
        right = 'b3',
    },

'd2': {
zone_name: ''
description = ''
examination = ''
solved = False
up = 'a2',
down = 'c2',
left = 'b1',
right = 'b3',
},

'd3': {
zone_name: ''
description = ''
examination = ''
solved = False
up = 'a2',
down = 'c2',
left = 'b1',
right = 'b3',
},

'd4': {
zone_name: ''
description = ''
examination = ''
solved = False
up = 'a2',
down = 'c2',
left = 'b1',
right = 'b3',
},

'e1': {
zone_name: ''
description = ''
examination = ''
solved = False
up = 'a2',
down = 'c2',
left = 'b1',
right = 'b3',
},

'e2': {
zone_name: ''
description = ''
examination = ''
solved = False
up = 'a2',
down = 'c2',
left = 'b1',
right = 'b3',
},

'e3': {
zone_name: ''
description = ''
examination = ''
solved = False
up = 'a2',
down = 'c2',
left = 'b1',
right = 'b3',
},

'e4': {
zone_name: ''
description = ''
examination = ''
solved = False
up = 'a2',
down = 'c2',
left = 'b1',
right = 'b3',
},








}
