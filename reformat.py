from pokemath import *

with open("f_file.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]

"""
pk_types = ["Normal","Fire", "Water", "Electric", "Grass",
            "Ice","Fighting","Poison","Ground","Flying",
            "Psychic","Bug","Rock","Ghost","Dragon",
            "Dark","Steel","Shadow","nature type"]

pk_stats = ["HP", "ATK","DEF","SP. ATK", "SP. DEF", "SPD",
            "Energy","Max Energy", "Friendship", "Max Friendship"]

pk_skills = ["Hiking", "Jumping", "Swimming", "Climbing", "Fishing",
             "Hunting", "Farming", "Tracking", "Foraging", "Mining",
             "Sneaking", "Instinct", "Performing", "Forecasting",
             "Perception", "Sensing", "Fortitude", "Intimidation",
             "Persuasion"]
"""

st = ""
for c in content:
    index = c.split("|")
    if len(index) == 1:
        if len(st) > 0:
            st = st[:-1]
            print convertMoveset(st)
            st = ""
        print index[0]
    else:
        st += index[1]+":"+index[0]+","
st = st[:-1]
print convertMoveset(st)
