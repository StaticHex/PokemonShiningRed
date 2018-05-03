from math import *
import random as rand
"""
================================================================================
=== Pokemath provides basic functions for running the S.P.S. tabletop system ===
================================================================================
"""
"""
================================================================================
HEALTH CONSTANTS
================================================================================
"""
FULL = 0
HIGH = 1
MED = 2
LOW = 3

"""
================================================================================
POKEBALL CONSTANTS
================================================================================
"""
POKEBALL = 7
GREATBALL = 5
ULTRABALL = 3

"""
================================================================================
STATUS CONSTANTS
================================================================================
"""
NORM = 0
AFFLICT = 1
"""
================================================================================
LOOKUP TABLES
================================================================================
"""

flavors = ["Spicy","Sour","Dry","Bitter","Sweet"]
pk_types = ["Normal","Fire", "Water", "Electric", "Grass",
            "Ice","Fighting","Poison","Ground","Flying",
            "Psychic","Bug","Rock","Ghost","Dragon",
            "Dark","Steel","Shadow"]

pk_stats = ["HP", "ATK","DEF","SP. ATK", "SP. DEF", "SPD",
            "Energy","Max Energy", "Friendship", "Max Friendship"]

pk_skills = ["Hiking", "Jumping", "Swimming", "Climbing", "Fishing",
             "Hunting", "Farming", "Tracking", "Foraging", "Mining",
             "Sneaking", "Instinct", "Performing", "Forecasting",
             "Perception", "Sensing", "Fortitude", "Intimidation",
             "Persuasion","Cut","Fly","Surf","Strength","Rock Smash",
             "Headbutt","Defog","Flash","Whirlpool","Waterfall",
             "Rock Climb","Dig","Teleport","Dive","Lockpicking",
             "Pickpocketing","ESP"]

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
ITEM CLASS
================================================================================
"""
class Item:
    id_no = 0
    name = ""
    cost = ""
    sell = ""
    fling_dmg = 0
    fling_effect = ""
    nature_dmg = 0
    nature_type = ""
    description = ""
    def __init__(self, entry=["0","Null","N/A","0P","0","-","0","-",
                              "This item does not exist"]):
        self.id_no = int(entry[0])
        self.name = entry[1]
        self.cost = entry[2]
        self.sell = entry[3]
        self.fling_dmg = int(entry[4])
        self.fling_effect = entry[5]
        self.nature_dmg = int(entry[6])
        self.nature_type = entry[7]
        self.description = entry[8]

"""
================================================================================
MOVE CLASS
================================================================================
"""
class Move:
    id_no = 0
    name = ""
    element = 0
    category = ""
    pp = 0
    max_pp = 0
    pp_rate = 0
    power = ""
    accuracy = ""
    description = ""
    c_category = ""
    c_points = 0
    c_jam = 0
    c_description = ""
    rank = 0
    def __init__(self, entry=["0","None","0","Status","???","-","0","0%",
                              "This move does not exist.","0","0",
                              "This move probably won't go over very well at contest"]):
        self.id_no = int(entry[0])
        self.name = entry[1]
        self.element = int(entry[2])
        self.category = entry[3]
        if(entry[5] == "-"):
            self.pp = -1
        else:
            self.pp = int(entry[5])
        if(self.pp < 0):
            self.max_pp = -1
        else:
            self.max_pp = int(round(self.pp * 1.6))
        if(self.pp < 0):
            self.pp_rate = -1
        else:
            self.pp_rate = int(round(self.pp * 0.2))
        self.power = entry[6]
        self.accuracy = entry[7]
        self.description = entry[8]
        self.c_category = entry[4]
        self.c_points = int(entry[9])
        self.c_jam = int(entry[10])
        self.c_description = entry[11]
        self.rank = self.calcRank()
    def calcRank(self):
        status = ["poison", "paralyze", "confuse", "infatuate", "burn", "freeze"]
        rank = 0
        if self.category == "Status":
            for s in status:
                if s in self.description:
                    rank += 3
            rank += 2
        else:
            if self.power == "*" or self.power == "-":
                rank += 60
            else:
                rank += int(self.power)
        if self.element == 17:
            rank = 500
        return rank

"""
================================================================================
ABILITY CLASS
================================================================================
"""
class Ability:
    id_no = 0
    name = ""
    description = ""
    def __init__(self, entry=["0","Null","This ability does not exist."]):
        self.id_no = int(entry[0])
        self.name = entry[1]
        self.description = entry[2]
""" 
================================================================================
ABILITY CLASS
================================================================================
"""
class Nature:
    id_no = 0
    name = ""
    stat_mods = []
    skill_mods = []
    description = ""
    def __init__(self, entry=["0","Empty","-","-","This nature does not exist."]):
        self.id_no = int(entry[0])
        self.name = entry[1]
        self.stat_mods = entry[2].split(",")
        self.skill_mods = entry[3].split(",")
        self.description = entry[4]

"""
================================================================================
POKEMON CLASS
================================================================================
"""
class Pokemon:
    id_no = 0
    species = ""
    name = ""
    height = 0 # in inches
    weight = 0.0 #in lbs
    element = []
    owner = ""
    level = 1
    evol = 5
    exp = 0
    stats = []
    pstat = []
    sstat = []
    moves = []
    skills = []
    ability = Ability()
    nature = Nature()
    h_power = 0
    n_def = ""
    flavors = []
    rarity = 0
    is_shiny = False
    item = Item()
    def __init__(self):
        self.level = 1
        
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
print "Natures successfully loaded.\n"
print "Data successfully loaded, PokeMath initalized; ready to begin.\n\n\n\n\n\n\n\n\n\n"

def getItem(prob):
    tup = prob.split(",")
    p_vec =[]
    it = []
    for t in tup:
        pair = [int(i) for i in t.split(":")]
        it.append(pair[0])
        p_vec.append(pair[1] / 100.0)

    it_prob = rand.random
    p_sum = p_vec[0]
    i = 0
    while(it_prob < p_sum):
        i += 1
        p_sum += p_vec[i]
    return it[i]    

def getIndex(probs = [0.166667, 0.166667, 0.166667, 0.166667, 0.166667, 0.166667]):
    s = 0.0
    p = rand.random()
    for i in range(6):
        s += probs[i]    
        if p < s:
           return i
    return 5

def arrayAdd(a, b, size):
    for i in range(size):
        a[i] += b[i]
    return a

def arrayDiv(a, num, size):
    for i in range(size):
        a[i] /= round(float(num))
        a[i] = int(a[i])
    return a

def generatePVector(stars=[5,5,5,5,5,5]):
    t = float(sum(stars))
    for i in range(len(stars)):
        stars[i] /= t
    return stars

def assignStats(probs = [0.166667, 0.166667, 0.166667, 0.166667, 0.166667, 0.166667]):
    # HP ATK DEF SP.ATK SP.DEF SPD
    stats = [0,0,0,0,0,0]
    tp = 0
    while(tp != 64):
        i = getIndex(probs)
        if(stats[i] < 255):
            stats[i] += 1
        tp = sum(stats)
    return stats

def balanceStats(probs = [0.166667, 0.166667, 0.166667, 0.166667, 0.166667, 0.166667]):
    s_stats = [0, 0, 0, 0, 0, 0]
    for i in range(1000):
        s_stats = arrayAdd(s_stats, assignStats(probs), 6)
    s_stats = arrayDiv(s_stats, 1000.0, 6)
    return s_stats

def levelUpRoll():
    minr = 0
    maxr = 3
    return [rand.randint(minr,maxr),
            rand.randint(minr,maxr),
            rand.randint(minr,maxr),
            rand.randint(minr,maxr),
            rand.randint(minr,maxr),
            rand.randint(minr,maxr)]

RANKED = 1
SHADOW = 2
# ======================================================================
# === Generates a pokemon from a file and does the math to set it's  ===
# === level up to the passed level                                   ===
# === name -- which pokemon you want to load                         ===
# === lvl --- the level you want the pokemon to be                   ===
# === ranked - whether or not to rank skills when learning new ones  ===
# ======================================================================
def genPokemon(name="Bulbasaur", lvl=1, mods=0):
    pokemon = Pokemon()
    
    #1. open file from pokemon/name.txt
    with open("pokemon/"+name.lower()+".txt") as f:
        content = f.readlines()
    f.close()
    content = [x.strip() for x in content]
    content = content[0].split("|")

    # turn our string into a list to choose from
    abil = [int(i) for i in content[7].split(":")]

    #calculate which foods our pokemon likes to eat
    l_flav = rand.randint(0,4)
    h_flav = rand.randint(0,4)
    while(l_flav == h_flav):
        h_flav = rand.randint(0,4)
    flavs = [l_flav,h_flav]
        
    pokemon.id_no = int(content[0])
    pokemon.species = content[1]
    pokemon.name = "N/A"
    pokemon.owner = "N/A"
    pokemon.height = int(content[2])
    pokemon.weight = float(content[3])
    pokemon.element = [int(i) for i in content[4].split(":")]
    pokemon.level = lvl
    pokemon.evol = content[10]
    pokemon.exp = howMuchXP(lvl)  
    pokemon.stats = [int(i) for i in content[5].split(":")]

    #generate pokemon's base stats, primary stats, and secondary stats
    p_vec = generatePVector(pokemon.stats[:6])
    new_stats = balanceStats(p_vec)
    ns_copy = pokemon.stats[:6]
    mx = min(ns_copy)
    pstat = []
    sstat = []
    for i in range(len(ns_copy)):
        if ns_copy[i] == mx:
            sstat.append(i)

    mx = max(ns_copy)
    for i in range(len(ns_copy)):
        if ns_copy[i] == mx:
            pstat.append(i)
            ns_copy[i] = -1
    mx = max(ns_copy)
    for i in range(len(ns_copy)):
        if ns_copy[i] == mx:
            pstat.append(i)
            ns_copy[i] = -1

    pokemon.pstat = pstat
    pokemon.sstat = sstat

    #level up the pokemon's stats to match it's current level
    for i in range(lvl-1):
        lup_stats = levelUpRoll()
        mx = max(lup_stats)
        assigned = [1,1,1,1,1,1]
        
        #highest roll gets assigned to one of the primary stats
        ind = pokemon.pstat[rand.randint(0,len(pokemon.pstat)-1)]
        idx = rand.randint(0,len(lup_stats)-1)
        if new_stats[ind] < 255:
            new_stats[ind] += max(0,mx-1)
            if new_stats[ind] > 255:
                new_stats[ind] = 255
            ind = lup_stats.index(mx)
            assigned[ind] = 0
            lup_stats[ind] = -1
        else:
            assigned[ind] = 0

        #lowest roll gets assigned to one of the secondary stats
        mx = min(lup_stats)
        ind = pokemon.sstat[rand.randint(0,len(pokemon.sstat)-1)]
        if new_stats[ind] < 255:
            new_stats[ind] += mx+1*(i%2)
            if new_stats[ind] > 255:
                new_stats[ind] = 255
            ind = lup_stats.index(mx)
            assigned[ind] = 0
            lup_stats[ind] = -1
        else:
            assigned[ind] = 0

        #now assign the rest of the stats
        while(max(assigned)):
            ind = rand.randint(0, len(lup_stats)-1)
            if(assigned[ind]):
                new_stats[ind] += lup_stats[ind]
                if new_stats[ind] > 255:
                    new_stats[ind] = 255
                assigned[ind] = 0
    pokemon.stats[:6] = new_stats[:6]

    #Grab the pokemon's learnset and partition it
    mov = []
    m_lv = []
    tup = content[6].split(",")
    for t in tup:
        t = t.split(":")
        mov.append(int(t[0]))
        m_lv.append(int(t[1]))

    if mods & 2:
        s_count = 0
        new_species = "Dark "+pokemon.species
        pokemon.ability = abilities[124]
        pokemon.species = new_species
        for i in range(len(mov)-1):
            ind = [int(i) in s_moves[i].split()]
            if ind[0] > 0:
                mov[i] = ind[rand.randint(0,len(ind)-1)]
                s_count += 1
        if s_count == 0:
            mov[0] = 469

    # Teach the pokemon some moves
    mi = 0
    while mi < len(m_lv) and m_lv[mi] < lvl:
        if len(pokemon.moves) < 4:
            pokemon.moves.append(moves[mov[mi]])
        else:
            if mods & 1:
                r_min = 0
                min_i = 0
                for m in range(4):
                    if pokemon.moves[m].rank < r_min:
                        r_min = pokemon.moves[m].rank
                        min_i = m
                pokemon.moves[min_i] = moves[mov[mi]]
            else:
                pokemon.moves[rand.randint(0,3)] = moves[mov[mi]]
        mi += 1

    # Teach the pokemon some skills
    skills = [int(i) for i in content[11].split(":")]
    
    skills[0] = 5 + int(round(pokemon.stats[5] / 255.0 * 15))
    skills[1] += 5
    
    sum_skill = 0
    for s in pokemon.element:
        sum_skill += swimming[s]
    sum_skill /= 1.0*len(pokemon.element)
    
    skills[2] = int(sum_skill)
    skills[3] += 5
    skills[4] += 5
    skills[5] += 5

    sum_skill = 0
    for s in pokemon.element:
        sum_skill += farming[s]
    sum_skill /= 1.0*len(pokemon.element)
    
    skills[6] += int(sum_skill)
    skills[7] += 5
    skills[8] += 5

    sum_skill = 0
    for s in pokemon.element:
        sum_skill += mining[s]
    sum_skill /= 1.0*len(pokemon.element)
    
    skills[9] += int(sum_skill)
    skills[10] = (20 - int(round(pokemon.weight / 2204.4 * 20)))

    sum_skill = 0
    for s in pokemon.element:
        sum_skill += instinct[s]
    sum_skill /= 1.0*len(pokemon.element)
    
    skills[11] += int(sum_skill)
    skills[12] += 5
    skills[13] += 5
    skills[14] += 5

    sum_skill = 0
    for s in pokemon.element:
        sum_skill += sensing[s]
    sum_skill /= 1.0*len(pokemon.element)
    
    skills[15] += int(sum_skill)

    sum_skill = 0
    for s in pokemon.element:
        sum_skill += fortitude[s]
    sum_skill /= 1.0*len(pokemon.element)
    
    skills[16] += int(sum_skill)

    sum_skill = 0
    for s in pokemon.element:
        sum_skill += intimidation[s]
    sum_skill /= 1.0*len(pokemon.element)
    
    skills[17] += int(sum_skill)

    sum_skill = 0
    for s in pokemon.element:
        sum_skill += persuasion[s]
    sum_skill /= 1.0*len(pokemon.element)
    
    skills[18] += int(sum_skill)

    pokemon.skills = skills
    if(not(mods & 2)):
        pokemon.ability = abilities[abil[rand.randint(0,len(abil)-1)]]
    pokemon.nature = natures[rand.randint(1,len(natures)-1)]

    #Adjust skills and stats according to pokemon's nature
    if pokemon.nature.stat_mods[0] != "-":
        for nm in pokemon.nature.stat_mods:
            tup = [int(i) for i in nm.split(":")]
            pokemon.stats[tup[0]] += tup[1]

    if pokemon.nature.skill_mods[0] != "-":
        for nm in pokemon.nature.skill_mods:
            tup = [int(i) for i in nm.split(":")]
            pokemon.skills[tup[0]] += tup[1]

    #adjust HP for 512
    pokemon.stats[0] *= 2
    
    pokemon.flavors = flavs
    pokemon.h_power = rand.randint(0,len(pk_types)-1)
    pokemon.n_def = content[12]
    pokemon.rarity = int(content[9])
    pokemon.is_shiny = isShiny()
    pokemon.item = items[getItem(content[8])]

    return pokemon

# ======================================================================
# === Saves a generated pokemon to a file                            ===
# ======================================================================
def savePokemon(pokemon):
    fentry = ""
    fentry += str(pokemon.id_no)+"|"            # ID No.
    fentry += pokemon.species+"|"               # Species
    fentry += pokemon.name+"|"                  # Name
    fentry += str(pokemon.height)+"|"           # Height
    fentry += str(pokemon.weight)+"|"           # Weight
    for e in pokemon.element:                   # Element
        fentry += str(e)+":"
    fentry = fentry[:-1]
    fentry += "|"
    fentry += pokemon.owner+"|"                 # Owner
    fentry += str(pokemon.level)+"|"            # Level
    fentry += pokemon.evol+"|"                  # Evolution Method
    fentry += str(pokemon.exp)+"|"              # Exp points
    for s in pokemon.stats:
        fentry += str(s)+":"                    # Stats
    fentry = fentry[:-1]
    fentry += "|"
    for ps in pokemon.pstat:                    # Primary Stats
        fentry += str(ps)+":"
    fentry = fentry[:-1]
    fentry += "|"
    for ss in pokemon.sstat:                    # Secondary Stats
        fentry += str(ss)+":"
    fentry = fentry[:-1]
    fentry += "|"
    for m in pokemon.moves:                     # Moves
        fentry += str(m.id_no)+":"
    fentry = fentry[:-1]
    fentry += "|"
    for sk in pokemon.skills:                   # Skills
        fentry += str(sk)+":"
    fentry = fentry[:-1]
    fentry += "|"
    fentry += str(pokemon.ability.id_no)+"|"    # Ability
    fentry += str(pokemon.nature.id_no)+"|"     # Nature
    fentry += str(pokemon.h_power)+"|"          # Hidden Power Type
    fentry += str(pokemon.n_def)+"|"            # Natural Defense Value
    for f in pokemon.flavors:                   # Flavors
        fentry+= str(f)+":"
    fentry = fentry[:-1]
    fentry += "|"
    fentry += str(pokemon.rarity)+"|"           # Rarity
    fentry += str(pokemon.is_shiny)+"|"         # Shiny
    fentry += str(pokemon.item.id_no)           # Item

    fname = "pokemon/saved/"+pokemon.species+"-"+pokemon.owner+".txt"
    fname = fname.lower()
    fname = fname.replace(" ", "_")
    f = open(fname,'w')
    f.write(fentry)
    f.close

# ======================================================================
# === Loads a previously saved pokemon from a file                   ===
# ======================================================================
def loadPokemon(fname):
    with open("pokemon/saved/"+fname.lower()+".txt") as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    content = content[0].split("|")
    pokemon = Pokemon()
    pokemon.id_no = int(content[0])
    pokemon.species = content[1]
    pokemon.name = content[2]
    pokemon.height = int(content[3])
    pokemon.weight = float(content[4])
    pokemon.element = [int(i) for i in content[5].split(":")]
    pokemon.owner = content[6]
    pokemon.level = int(content[7])
    pokemon.evol = content[8]
    pokemon.exp = int(content[9])
    pokemon.stats = [int(i) for i in content[10].split(":")]
    pokemon.pstat = [int(i) for i in content[11].split(":")]
    pokemon.sstat = [int(i) for i in content[12].split(":")]
    pokemon.moves = [moves[int(i)] for i in content[13].split(":")]
    pokemon.skills = [int(i) for i in content[14].split(":")]
    pokemon.ability = abilities[int(content[15])]
    pokemon.nature = natures[int(content[16])]
    pokemon.h_power = int(content[17])
    pokemon.n_def = content[18]
    pokemon.flavors = [flavors[int(i)] for i in content[19].split(":")]
    pokemon.rarity = int(content[20])
    if(content[21] == "False"):
        pokemon.is_shiny = False
    else:
        pokemon.is_shiny = True
    pokemon.item = items[int(content[22])]
    return pokemon

# ======================================================================
# === Boosts a pokemon's stats                                       ===
# ======================================================================
P_BONUS = 15
S_BONUS = 10
L_BONUS = 25

def boostPokemon(pokemon, boost=[0,0,0,0,0,0], bonus=0):
    pokemon.stats[0] += boost[0]+bonus
    for i in range(len(boost)):
        pokemon.stats[i] += boost[i]+bonus
   
# ======================================================================
# === Checks to see whether a pokemon is shiny or not                ===
# === can either call the check with or without a number to do       ===
# === the check for multiple pokemon                                 ===
# === (optional) num -- number of pokemon to check for               ===
# ======================================================================
def isShiny(num=1):
    for i in range(num):
        chance = rand.randint(1, 8192)
        if chance is 4096:
            return True
        else:
            return False

# ======================================================================
# === Calculates the target number to beat for a pokemon catch       ===
# === attempt                                                        ===
# === name -- the name of the pokemon you are trying to catch        ===
# === hp -- the pokemon's HP either FULL, HIGH, MED, or LOW          ===
# === status -- either NORM or AFFLICTED                             ===
# === ball_type -- the type of pokeball you're using                 ===
# ======================================================================
def catchAttempt(name, hp, status, ball_type):
    return ""
    #1. call load pokemon with name
    #2. get the rarity from the loaded pokemon
    #3. return ball_type - (hp + status) + rarity

# ======================================================================
# === Calculates the target number to beat for skill usage           ===
# === p_skill -- the player's skill level                            ===
# === skill_l -- the level of the skill to beat                      ===
# ======================================================================
def skillAttempt(p_skill,skill_l=5):
    rounding = Rounding()
    mod = rounding.BankersRounding(-5*sin((3*pi/2) + p_skill/7.0)+5)
    return int(skill_l + mod)

# ======================================================================
# === Returns the amount of exp needed to reach the level passed     ===
# ======================================================================
def howMuchXP(lvl):
    sum = 0;
    for i in range(lvl):
        sum += int(round(exp(lvl/28.518)*300))
    return sum

# ======================================================================
# === Returns the amount of exp gained from battle                   ===
# ======================================================================
WILD = 0
TRAINER = 10
LEADER = 20
CHAMPION = 30
def battleXP(pokemon, mod=WILD):
    return ((20 + mod) * pokemon.level * pokemon.rarity)


# ======================================================================
# === Create a stack of pokemon to work with                         ===
# ======================================================================
poke_stack = []

def pokePush(pokemon):
    poke_stack.append(pokemon)

def pokePop():
    global poke_stack
    poke_stack = poke_stack[:-1]

def pokeTop():
    return poke_stack[-1]

def pokePrint():
    line = 15
    print '-'*line
    for p in poke_stack:
        print "| "+padString(p.species,11,CENTER)+" |"
        print "-"*line
        
"""
================================================================================
PRINT FUNCTIONS
================================================================================
"""

LEFT = 0
RIGHT = 1
CENTER = 2

def printWrapped(string, length, offset, lead="", trail=""):
    str_len = len(string)
    l_len = len(lead)
    t_len = len(trail)
    cor_len = length - l_len - t_len
    i = 0
    tok = ""
    while(i < str_len):
        tok += string[i]
        if(len(tok) > cor_len):
            while(tok[-1] != " "):
                tok = tok[:-1]
                i -= 1
            tok = tok[:-1]
            print lead+padString(tok,cor_len,LEFT)+trail
            tok = " "*offset
        i += 1
    print lead+padString(tok,cor_len,LEFT)+trail

def padString(string, length, style):
    i = 0
    while(len(string) < length):
        if style is 0:
            string += " "
        elif style is 1:
            string = " "+string
        else:
            if i % 2 is 0:
                string += " "
            else:
                string = " "+string
            i += 1
    return string
        
def printItem(id_no):
    title = "* "+padString(items[id_no].name,38,LEFT)+padString("#"
                +str(items[id_no].id_no),38,RIGHT)+" *"
    price = padString("Buy Price: "+items[id_no].cost, 30, LEFT)
    price += padString("Sell Price: "+items[id_no].sell,46,LEFT)
    
    fling = padString("Fling Damage: "+str(items[id_no].fling_dmg),30,LEFT)
    fling += padString("Fling Effect: "+items[id_no].fling_effect,46,LEFT)
    
    natural_gift = padString("Natural Gift Damage: "+str(items[id_no].nature_dmg),30,LEFT)
    natural_gift += padString("Natural Gift Type: "+items[id_no].nature_type,46,LEFT)

    
    print "*"*80
    print title
    print "*"*80
    print "| "+price+" |"
    print "-"*80
    print "| "+fling+" |"
    print "-"*80
    print "| "+natural_gift+" |"
    print "-"*80
    desc = items[id_no].description
    printWrapped("Description: "+desc, 80,
                 len("Description: "), "| ", " |")
    print "-"*80

def printMove(id_no):
    title = "* "+padString(moves[id_no].name,38,LEFT)
    title += padString("#"+str(moves[id_no].id_no), 38, RIGHT)+" *"

    classifier = "| "+padString("Element: "+pk_types[moves[id_no].element],
                                38, LEFT);
    classifier += padString("Category: "+moves[id_no].category,38, LEFT)+" |"

    pp_info = "| "+padString("PP: "+str(moves[id_no].pp),25,LEFT)
    pp_info += padString("Max PP: "+str(moves[id_no].max_pp),25,LEFT)
    pp_info += padString("PP Rate: "+str(moves[id_no].pp_rate),26,LEFT)+" |"

    move_info = "| "+padString("Power: "+moves[id_no].power, 38, LEFT)
    move_info += padString("Accuracy: "+moves[id_no].accuracy, 38, LEFT)+" |"

    cont_info = "| "+padString("Category: "+moves[id_no].c_category, 25, LEFT)
    cont_info += padString("Appeal Points: "+str(moves[id_no].c_points), 25, LEFT)
    cont_info += padString("Jam Points: "+str(moves[id_no].c_jam),26,LEFT)+" |"

    print "*"*80
    print title
    print "*"*80
    print "="*80
    print "| "+padString("Battle Info", 76, CENTER)+" |"
    print "="*80
    print pp_info
    print "-"*80
    print classifier
    print "-"*80
    print move_info
    print "-"*80
    desc = moves[id_no].description
    printWrapped("Description: "+desc, 80,
                 len("Description: "), "| ", " |")
    print "="*80
    print "| "+padString("Contest Info", 76, CENTER)+" |"
    print "="*80
    print cont_info
    print "-"*80
    desc = moves[id_no].c_description
    printWrapped("Description: "+desc, 80,
            len("Description: "), "| ", " |")
    print "="*80

def printAbility(id_no):
    title = "* "+padString(abilities[id_no].name,38,LEFT)
    title += padString("#"+str(abilities[id_no].id_no),38,RIGHT)+" *"
    desc = abilities[id_no].description
    print "*"*80
    print title
    print "*"*80
    printWrapped("Description: "+desc, 80,
            len("Description: "), "| ", " |")
    print "-"*80

def printNature(id_no):
    title = "* "+padString(natures[id_no].name,38,LEFT)
    title += padString("#"+str(natures[id_no].id_no),38,RIGHT)+" *"

    stat_string = ""
    if natures[id_no].stat_mods[0] != "-":
        for mod in natures[id_no].stat_mods:
            tup = mod.split(":")
            stat_string += pk_stats[int(tup[0])]+": "
            if int(tup[1]) > 0:
                stat_string += "+"
            stat_string += tup[1]+"     "
    else:
        stat_string = "-"

    skill_string = ""
    if natures[id_no].skill_mods[0] != "-":
        for mod in natures[id_no].skill_mods:
            tup = mod.split(":")
            skill_string += pk_skills[int(tup[0])]+": "
            if int(tup[1]) > 0:
                skill_string += "+"
            skill_string += tup[1]+"     "
    else:
        skill_string = "-"

    desc = natures[id_no].description
    print "*"*80
    print title
    print "*"*80
    printWrapped("Stat Mods: "+stat_string, 80, len("Stat Mods: "),"| ", " |")
    print "-"*80
    printWrapped("Skill Mods: "+skill_string, 80, len("Skill Mods: "), "| ", " |")
    print "-"*80
    printWrapped("Description: "+desc, 80, len("Description: "), "| ", " |")
    print "-"*80

def inchToFt(inches):
    feet = 0
    while(inches >= 12):
        inches -= 12
        feet += 1
    return str(feet)+"' "+str(inches)+"\""
        
def printPokemon(subject):
    e_string = ""
    for e in subject.element:
        e_string += "["+pk_types[e]+"]["
    e_string = e_string[:-1]

    title = "* "+padString(subject.species,26,LEFT)
    title += padString(e_string, 25, CENTER)
    title += padString("#"+str(subject.id_no),25,RIGHT)+" *"

    l_info = "| "+padString("Lvl: "+str(subject.level),25,LEFT)
    l_info += padString("Exp: "+str(subject.exp),26,LEFT)
    l_info += padString("Evolve: "+subject.evol,25,RIGHT)+" |"

    p_info = "| "+padString("Nickname: "+subject.name,38,LEFT)
    p_info += padString("Height: "+inchToFt(subject.height), 19, LEFT)
    p_info += padString("Weight: "+str(subject.weight)+"lbs.", 19, RIGHT)+" |"

    p_owner = "| "+padString("Owner: "+subject.owner,38,LEFT)

    n_ar = padString("Natural Armor: "+subject.n_def,38,LEFT)+" |"

    stat_str = ""
    stat_str2 = ""
    for i in range(len(subject.stats)):
        st = str(subject.stats[i])
        if i == 0:
            stat_str += pk_stats[i]+": "+st+"/"+st+"  "
        elif i < 6:
            stat_str += pk_stats[i]+": "+st+"  "
        elif i % 2 == 0:
            stat_str2 += pk_stats[i]+": "+st+"/"+str(subject.stats[i+1])+"   "
    stat_str = "| "+padString(stat_str,76,LEFT)+" |"
    stat_str2 = "| "+padString(stat_str2,51,LEFT)
    stat_str2 += padString("Shiny: "+str(subject.is_shiny),25,RIGHT)+" |"

    p_stat = "Strong: "
    for i in subject.pstat:
        p_stat += pk_stats[i]+", "
    p_stat = p_stat[:-2]
    p_stat = "| "+padString(p_stat,38,LEFT)

    s_stat = "Weak: "
    for i in subject.sstat:
        s_stat += pk_stats[i]+", "
    s_stat = s_stat[:-2]
    s_stat = padString(s_stat,38,LEFT)+" |"

    hp_type = "| "+padString("Hidden Power Type: "+pk_types[subject.h_power], 30, LEFT)
    
    flav = padString("Likes: "+subject.flavors[0],26,RIGHT)
    flav += padString("Hates: "+subject.flavors[1],20,RIGHT)+" |"

    sk_string = ""
    for sk in range(len(subject.skills)):
        if subject.skills[sk] > 0:
            sk_string += padString(pk_skills[sk]+": "+str(subject.skills[sk]),25,LEFT)

    print "="*80
    print "*"*80
    print title
    print "*"*80
    print "="*80
    print p_info
    print "-"*80
    print p_owner+n_ar
    print "-"*80
    print l_info
    print "-"*80
    print stat_str
    print "-"*80
    print stat_str2
    print "-"*80
    print p_stat+s_stat
    print "-"*80
    print hp_type+flav
    print "="*80
    printWrapped(sk_string,80,0,"| ", " |")
    print "="*80
    print "\n\n"
    for m in subject.moves:
        printMove(m.id_no)
        print ""
    print "\n"
    printAbility(subject.ability.id_no)
    print "\n\n"
    printNature(subject.nature.id_no)
    if subject.item.id_no > 0:
        print "\n"
        printItem(subject.item.id_no)
    
    
def print_skills():
    margin = ['  ', '  ', '  ', '  ', '  ',
              'S ', 'k ', 'i ', 'l ', 'l ', '  ',
              'P ', 'o ', 'i ', 'n ', 't ', 's ',
              '  ', '  ', '  ', '  ']
    print "                 Difficulty         "
    print "        1  2  3  4  5  6  7  8  9 10"
    for i in range(21):
        if (i < 10):
            print margin[i]+" "+str(i)+": ",
        else:
            print margin[i]+str(i)+": ",
        for j in range(10):
            mod = skillAttempt(i, j+1)
            if (mod < 10) and (mod >= 0):
                print '',
            print str(mod),
        print ''


"""
================================================================================
SEARCH FUNCTIONS
================================================================================
"""
def findItem(name):
    for i in items:
        if i.name.upper().replace(" ","") == name.upper().replace(" ",""):
            return i.id_no
    return 0

def findMove(name):
    for m in moves:
        if m.name.upper().replace(" ","") == name.upper().replace(" ",""):
            return m.id_no
    return 0

def findAbility(name):
    for a in abilities:
        if a.name.upper().replace(" ","") == name.upper().replace(" ",""):
            return a.id_no
    return 0

def findNature(name):
    for n in natures:
        if n.name.upper().replace(" ","") == name.upper().replace(" ",""):
            return n.id_no
    return 0

l_level = [1,5,9,13,17,21,25,29,33,37,41,45,49,53]
learnset= ["Tackle","Howl","Sand Attack","Bite","Odor Sleuth","Roar","Swagger","Assurance",
           "Scary Face","Taunt","Embargo","Take Down", "Sucker Punch", "Crunch"]

def fLearnset(lev, learn):
    m_str = ""
    for i in range(len(learn)):
        m_str += str(findMove(learn[i]))+":"+str(lev[i])+","
    m_str = m_str[:-1]
    print m_str

#pokePush(genPokemon("Rattata",5))
#pokeTop().owner = "Evan White"
#savePokemon(pokeTop())

pokePush(loadPokemon("Rattata-Evan_White"))
printPokemon(pokeTop())

