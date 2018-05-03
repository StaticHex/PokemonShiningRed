from item import *
from move import *
from ability import *
from modifier import *
from nature import *
from job import *

"""
================================================================================
SHARED CONSTANTS
================================================================================
"""
flavors = ["Spicy","Sour","Dry","Bitter","Sweet"]

pk_types = ["Normal","Fire", "Water", "Electric", "Grass",
            "Ice","Fighting","Poison","Ground","Flying",
            "Psychic","Bug","Rock","Ghost","Dragon",
            "Dark","Steel","Shadow"]

pk_stats = ["HP","ATK","DEF","SP. ATK","SP. DEF","SPD","Energy","Friendship",
            "Max HP","MAX Energy","Max Friendship"]

pk_skills = ["Hiking", "Jumping", "Swimming", "Climbing", "Fishing",
             "Hunting", "Farming", "Tracking", "Foraging", "Mining",
             "Sneaking", "Instinct", "Performing", "Forecasting",
             "Perception", "Sensing", "Fortitude", "Intimidation",
             "Persuasion","Cut","Fly","Surf","Strength","Rock Smash",
             "Headbutt","Defog","Flash","Whirlpool","Waterfall",
             "Rock Climb","Dig","Teleport","Dive","Lockpicking",
             "Pickpocketing","ESP"]
pl_stats = ["HP","ATK","DEF","SP. ATK","SP. DEF","SPD"
           ,"MAX HP","ENERGY","MAX ENERGY","CHARISMA","MAX CHARISMA"]
pl_skills = ["hiking","jumping","swimming","climbing","fishing",
             "hunting","farming","training","riding","trapping",
             "poke speak","veterinary","husbandry","tracking",
             "camping","foraging","mining","esp","pharmaceuticals",
             "herbology","cooking","tinkering","sneaking","lockpicking",
             "pickpocketing","instint","fortitude","medicine","performing",
             "mechanic","hacking","investigation","persuasion", "intimidation",
             "forecasting","legend lore","perception","sensing","geography"]

cond = ['NORM','PSN','BRN','PRLZ','SLP','FRZ']
    
instinct = [5,5,5,5,5,5,10,5,5,5,5,5,5,5,5,5,5,5]
swimming = [5,0,20,5,5,5,5,5,0,5,5,5,0,5,5,5,5,5]
farming = [5,5,5,5,15,5,5,5,10,5,5,5,5,5,5,5,5]
mining = [0,0,0,0,0,0,0,0,10,0,0,0,5,0,0,0,0,5]
sensing = [5,5,5,5,5,5,5,5,5,5,10,5,5,15,5,5,10,5]
fortitude = [5,5,5,5,5,5,5,5,5,5,10,5,5,10,5,5,15,5]
intimidation = [5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,10,5,5]
persuasion = [5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,10,5,5]

"""
================================================================================
LOAD IN DATA
================================================================================
"""
print "Preparing program..."
print "Loading items..."
# Load in items
items = []
with open("data/items.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]
for c in content:
    new_item = c.split("|")
    items.append(Item(new_item))
print "Items successfully loaded."

moves = []

print "Loading moves..."
with open("data/moves.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]
for c in content:
    new_move = c.split("|")
    moves.append(Move(new_move))
print "Moves successfully loaded."

s_moves = []
print "Loading shadow moves..."
with open("data/shadow_m.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]
for c in content:
    new_move = c.split("|")
    s_moves.append(new_move[1])
print "Shadow moves successfully loaded."

abilities = []

print "Loading abilities..."
with open("data/abilities.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]
for c in content:
    new_ability = c.split("|")
    abilities.append(Ability(new_ability))
print "Abilities successfully loaded."

natures = []

print "Loading natures..."
with open("data/natures.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]
for c in content:
    new_nature = c.split("|")
    natures.append(Nature(new_nature))
print "Natures successfully loaded."

perks = {}

print "Loading perks..."
with open("data/perks.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]
for c in content:
    new_perk = Modifier(c)
    perks[new_perk.name.lower().replace("-","").replace(" ","")] = new_perk
print "Perks successfully loaded."

defects = {}

print "Loading defects..."
with open("data/defects.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]
for c in content:
    new_defect = Modifier(c)
    defects[new_defect.name.lower().replace("-","").replace(" ","").replace("/","")] = new_defect
print "Defects successfully loaded."

jobs = {}
print "Loading jobs..."
with open("data/jobs.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]
for c in content:
    new_job = Job(c)
    entry = new_job.name.lower().replace("-","").replace(" ","").replace("/","")
    jobs[entry] = new_job
print "Jobs successfully loaded.\n"

print "Data successfully loaded, PokeMath initalized; ready to begin.\n\n\n\n\n\n\n\n\n\n"

"""
================================================================================
SEARCH FUNCTIONS
================================================================================
"""
def findItem(name):
    for i in items:
        shearedI = i.name.upper().replace(" ","").replace("-","")
        shearedN = name.upper().replace(" ","").replace("-","")
        if shearedI == shearedN:
            return i.id_no
    return 0

def findMove(name):
    for i in moves:
        shearedI = i.name.upper().replace(" ","").replace("-","")
        shearedN = name.upper().replace(" ","").replace("-","")
        if shearedI == shearedN:
            return i.id_no
    return 0

def findAbility(name):
    for i in abilities:
        shearedI = i.name.upper().replace(" ","").replace("-","")
        shearedN = name.upper().replace(" ","").replace("-","")
        if shearedI == shearedN:
            return i.id_no
    return 0

def findNature(name):
    for i in natures:
        shearedI = i.name.upper().replace(" ","").replace("-","")
        shearedN = name.upper().replace(" ","").replace("-","")
        if shearedI == shearedN:
            return i.id_no
    return 0

def findPerk(name):
    return perks[name.lower().replace("-","").replace(" ","")]

def findDefect(name):
    return defects[name.lower().replace("-","").replace(" ","").replace("/","")]
