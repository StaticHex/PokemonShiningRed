from math import *
import random as rand
import time as time
from rounding import *
from os import listdir, path
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
FORMATTING CONSTANTS
================================================================================
"""

LEFT = 0
RIGHT = 1
CENTER = 2

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
            "Energy", "Friendship"]

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
    bonus = {'normal':0,'evolve1':10,'evolvem':20,'noevol':15,'mythic':15,'legendary':30}
    id_no = 0
    species = ""
    name = ""
    gender = ""
    height = 0 # in inches
    weight = 0.0 #in lbs
    element = []
    owner = ""
    level = 1
    evol = 5
    exp = 0
    stats = []
    sorder = []
    moves = []
    skills = []
    ability = Ability()
    nature = Nature()
    h_power = 0
    hp = 0
    energy = 0
    friendship = 0
    n_def = ""
    flavors = []
    rarity = 0
    is_shiny = False
    item = Item()
    learnset = []
    def __init__(self):
        self.level = 1
        self.exp = howMuchXP(self.level)

    def lvlUp(self,st=[]):
        self.level += 1
        if not len(st):
            self.exp = howMuchXP(self.level)
            st = levelUpRoll()
        st.sort()
        st.reverse()
        for s in self.sorder:
            if not s:
                self.stats[s] += st[0]*2
                self.hp += st[0]*2
            self.stats[s] += st[0]
            st = st[1:]
        # check for new moves
        while int(self.learnset[0][1]) <= self.level:
            alreadyLearned = 0
            for m in self.moves:
                if(int(self.learnset[0][0]) == m.id_no):
                    alreadyLearned = 1
            if not alreadyLearned:
                if len(self.moves) < 4:
                    self.moves.append(moves[int(self.learnset[0][0])])
                else:
                    inp = "n"
                    while(inp.lower() == "n"):
                        self.printMoves()
                        print ""
                        if self.name == "N/A":
                            inp = raw_input(self.species+" wants to learn the move "+moves[int(self.learnset[0][0])].name+" replace a move? (y/n): ")
                        else:
                            inp = raw_input(self.name+"wants to learn the move"+moves[int(self.learnset[0][0])].name+" replace a move? (y/n): ")
                        if inp.lower() == "y":
                            inp = raw_input("Choose a move number (1-4) to replace: ")
                            self.moves[int(inp)-1] = moves[int(self.learnset[0][0])]
                        else:
                            inp = raw_input("Really stop learning this move? (y/n): ")
                    if inp.lower() == "y":
                        if self.name == "N/A":
                            print self.species,"did not learn",moves[int(self.learnset[0][0])].name+"."
                        else:
                            print self.name,"did not learn",moves[int(self.learnset[0][0])].name+"."
            self.learnset = self.learnset[1:]

    def grow(self, lvl):
        diff = lvl - self.level
        if diff > 0:
            for i in range(diff):
                self.lvlUp()

    def buff(self, b_type="Normal"):
        for i in range(6):
            if not i:
                self.stats[i] += 2*self.bonus[b_type.lower()]
                self.hp += 2*self.bonus[b_type.lower()]
            else:
                self.stats[i] += self.bonus[b_type.lower()]

    def evolve(self, evolution, flags=0):
        pk = genPokemon(evolution, self.level-1, flags)
        self.id_no = pk.id_no
        self.species = pk.species
        self.height = pk.height
        self.weight = pk.weight
        self.element = list(set(self.element+pk.element[:]))
        self.evol = pk.evol
        self.buff('evolve1')
        self.sorder = pk.sorder[:]
        self.learnset = []
        self.learnset = pk.learnset[:]
        for i in range(len(self.skills)):
            self.skills[i] = pk.skills[i]
        self.ability = pk.ability
        self.n_def = pk.n_def
        self.rarity = pk.rarity

        # have to do this because we pass in evolution at lvl-1
        while int(self.learnset[0][1]) < self.level:
            self.learnset = self.learnset[1:]

        # check for new moves
        while int(self.learnset[0][1]) <= self.level:
            alreadyLearned = 0
            for m in self.moves:
                if(int(self.learnset[0][0]) == m.id_no):
                    alreadyLearned = 1
            if not alreadyLearned:
                if len(self.moves) < 4:
                    self.moves.append(moves[int(self.learnset[0][0])])
                else:
                    inp = "n"
                    while(inp.lower() == "n"):
                        self.printMoves()
                        print ""
                        if self.name == "N/A":
                            inp = raw_input(self.species+" wants to learn the move "+moves[int(self.learnset[0][0])].name+" replace a move? (y/n): ")
                        else:
                            inp = raw_input(self.name+"wants to learn the move"+moves[int(self.learnset[0][0])].name+" replace a move? (y/n): ")
                        if inp.lower() == "y":
                            inp = raw_input("Choose a move number (1-4) to replace: ")
                            self.moves[int(inp)-1] = moves[int(self.learnset[0][0])]
                        else:
                            inp = raw_input("Really stop learning this move? (y/n): ")
                    if inp.lower() == "y":
                        if self.name == "N/A":
                            print self.species,"did not learn",moves[int(self.learnset[0][0])].name+"."
                        else:
                            print self.name,"did not learn",moves[int(self.learnset[0][0])].name+"."
            self.learnset = self.learnset[1:]
                      
                    
                
    def printLearnset(self):
        print padString("I.",3,LEFT)+" "+padString("Move Name",16,LEFT)+" Lvl."
        print "-------------------------"
        for i in range(len(self.learnset)):
            s = padString(str(i+1),3,LEFT)
            s += " "+padString(moves[int(self.learnset[i][0])].name,16,LEFT)
            s += " "+self.learnset[i][1]
            print s
    def printMoves(self):
        print "I. Move Name"
        print "-------------------"
        for i in range(len(self.moves)):
            print str(i+1)+" "+self.moves[i].name


class Modifier:
    name = "N/A"
    m_type = "N/A"
    skill_mods = []
    stat_mods = []
    cash_mods = 0
    effects = []
    description = "N/A"

    def __init__(self,mstring):
        self.skill_mods = []
        self.stat_mods = []
        self.effects = []
        mstring = mstring.split("|")
        self.name = mstring[0]
        self.m_type = mstring[1]
        st_mod = mstring[2].split(",")
        if not st_mod[0] == "-":
            for st in st_mod:
                st = st.split(":")
                self.stat_mods.append((st[0],int(st[1])))
        sk_mod = mstring[3].split(",")
        if not sk_mod[0] == "-":
            for sk in sk_mod:
                sk = sk.split(":")
                self.skill_mods.append((sk[0],int(sk[1])))
        if not mstring[4] == "-":
            self.cash_mods = int(mstring[4])
        self.effects = mstring[5].split(",")
        self.description = mstring[6]

    def pprint(self):
        p_stats = {"HP":"HP","ATK":"ATK","DEF":"DEF","SP. ATK":"SP. ATK",
                   "SP. DEF":"SP. DEF","SPD":"SPD","CHARISMA":"Charisma"}
        header = "="*80+"\n"+"*"*80 + "\n"
        header += "* "+padString(self.name,76,LEFT)+" *\n"
        header += "*"*80 + "\n" + "="*80 + "\n"
        mod_type = "| "+padString("Type: "+self.m_type,76,LEFT)+" |\n"+("-")*80
        st_mods = ""
        i = 0
        for st in self.stat_mods:
            st_mods += st[0]+": "
            if(st[1] > 0):
                st_mods += "+"
            st_mods += str(st[1])+"     "
        
        print header+mod_type
        if len(st_mods):
            printWrapped(st_mods,80,0,"| "," |")
        #sk_mods = ""
        #i = 0
        #for sk in self.skill_mods:
            
    
    
"""
================================================================================
CHARACTER CLASS
================================================================================
"""
class Character:
    name = ""
    owner = ""
    height = 0
    weight = 0
    stats = {"HP":0,"ATK":0,"DEF":0,"SP. ATK":0,"SP. DEF":0,"SPD":0
             ,"MAX HP":0,"ENERGY":0,"MAX ENERGY":0,"CHARISMA":0,"MAX CHARISMA":0}
    skills = {"hiking":0,"jumping":0,"swimming":0,"climbing":0,"fishing":0,
              "hunting":0,"farming":0,"training":0,"riding":0,"trapping":0,
              "poke speak":0,"veterinary":0,"husbandry":0,"tracking":0,
              "camping":0,"foraging":0,"mining":0,"esp":0,"pharmaceuticals":0,
              "herbology":0,"cooking":0,"tinkering":0,"sneaking":0,"lockpicking":0,
              "pickpocketing":0,"instint":0,"fortitude":0,"medicine":0,"performing":0,
              "mechanic":0,"hacking":0,"investigation":0,"persuasion":0, "intimidation":0,
              "forecasting":0,"legend lore":0,"perception":0,"sensing":0,"geography":0}
    cash = 0
    coins = 0
    perks = []
    defects = []
    items = []
    notes = []
    def __init__(self,fname=[]):
        if len(fname):
            fname = fname.split("|")
            self.name = fname[0]
            self.owner = fname[1]
            self.height = int(fname[2])
            self.weight = float(fname[3])
            if not fname[4] == "-":
                i = 0
                st_list = fname[4].split(":")
                for st in self.stats:
                    self.stats[st] = st_list[i]
                    i+=1
            if not fname[5] == "-":
                i = 0
                sk_list = fname[5].split(":")
                for sk in self.skills:
                    self.skills[sk] = sk_list[i]
                    i+=1
            self.cash = int(fname[6])
            self.coins = int(fname[7])
            if not fname[8] == "-":
                pk_list = fname[8].split(":")
                for pk in pk_list:
                    self.perks.append(getPerk(pk))
            if not fname[9] == "-":
                df_list = fname[9].split(":")
                for df in df_list:
                    self.defects.append(getDefect(df))
            if not fname[10] == "-":
                it_list = fname[10].split(",")
                for it in it_list:
                    it = it.split(":")
                    self.items.append((it[0],it[1]))
            if len(fname) > 11:
                nt_list = fname[11].split(":")
                for nt in nt_list:
                    self.notes.append(nt)

    def save(self,pref=""):
        outstring = ""
        outstring += self.name + "|"
        outstring += self.owner + "|"
        outstring += str(self.height) + "|"
        outstring += str(self.weight) + "|"
        for st in self.stats:
            outstring += str(self.stats[st])+":"
        outstring = outstring[:-1]+"|"
        for sk in self.skills:
            outstring += str(self.skills[sk])+":"
        outstring = outstring[:-1]+"|"
        outstring += str(self.cash)+"|"
        outstring += str(self.coins)+"|"
        if len(self.perks):
            for pk in self.perks:
                outstring += pk.name + ":"
            outstring = outstring[:-1]+"|"
        else:
            outstring += "-|"
        if len(self.defects):
            for df in self.defects:
                outstring += df.name + ":"
            outstring = outstring[:-1]+"|"
        else:
            outstring += "-|"
        if len(self.items):
            for it in self.items:
                outstring+= it[0] + ":" + str(it[1]) + ","
            outstring = outstring[:-1]+"|"
        else:
            outstring += "-|"
        if len(self.notes):
            for nt in self.notes:
                outstring += nt + ":"
            outstring = outstring[:-1]

        fname = "players/"
        if len(pref):
            fname += pref+"-"
        fname += self.name+"-"
        if len(self.owner):
            fname += self.owner+".txt"
        else:
            fname += "npc.txt"
        fname = fname.lower()
        fname = fname.replace(" ", "_")
        f = open(fname,'w')
        f.write(outstring)
        f.close

    def load(self, fname):
        with open("players/"+fname+".txt") as f:
            content = f.readlines()
        content = [x.strip() for x in content]
        content = content[0]
        print content
        self.__init__(content)
        
            

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
print "Defects successfully loaded.\n"

print "Data successfully loaded, PokeMath initalized; ready to begin.\n\n\n\n\n\n\n\n\n\n"

def getPerk(name):
    return perks[name.lower().replace("-","").replace(" ","")]

def getDefect(name):
    return defects[name.lower().replace("-","").replace(" ","").replace("/","")]

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
    for i in range(len(probs)):
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
    minr = 1
    maxr = 10
    pList = [rand.randint(minr,maxr),
            rand.randint(minr,maxr),
            rand.randint(minr,maxr),
            rand.randint(minr,maxr),
            rand.randint(minr,maxr),
            rand.randint(minr,maxr)]
    for i in range(len(pList)):
        if pList[i] > 5:
            pList[i] = 2
        else:
            pList[i] = 1
    return pList

def getGender(genders):
    rand.seed(time.gmtime())
    genders = genders.split(":")
    gen = rand.randint(0,len(genders)-1)
    return genders[gen]

def convertElements(elements):
    elements = elements.split(":")
    out = ''
    for e in elements:
        for i in range(len(pk_types)):
            if pk_types[i].lower() == e.lower():
                out += str(i)+":"
    out = out[:-1]
    return out

def convertMoveset(mov):
    mov = mov.split(",")
    out = ""
    notfound = []
    count = 0
    for m in mov:
        found = 0
        mv = m.split(":")
        n = findMove(mv[0])
        if n == 0:
            notfound.append(mv[0]+" "+mv[1])
        else:
            out += str(n)+":"+mv[1]+","
            count += 1
            found = 1
    out = out[:-1]
    print len(mov), "moves fed in."
    print count, "moves found"
    if len(notfound):
        print "The following moves were not found: "
        for i in notfound:
            print i
    return out

def convertAbilities(abi):
    abi = abi.split(":")
    out = ""
    for a in abi:
        n = findAbility(a)
        if n > 0:
            out += str(n)+":"
    out = out[:-1]
    return out

RANKED = 1
SHADOW = 2
# ======================================================================
# === Checks to see if the specified pokemon has a config file       ===
# ======================================================================
def chkExist(name=""):
    if path.isfile("pokemon/"+name.lower()+".txt"):
        print name+" exists"
    else:
        print name+" does not exist"

def chkWork(names):
    names = names.split(":")
    for n in names:
        if not path.isfile("pokemon/"+n.lower()+".txt"):
            print n+" needs to be created"

# ======================================================================
# === Generates a pokemon from a file and does the math to set it's  ===
# === level up to the passed level                                   ===
# === name -- which pokemon you want to load                         ===
# === lvl --- the level you want the pokemon to be                   ===
# === ranked - whether or not to rank skills when learning new ones  ===
# ======================================================================
def genPokemon(name="Bulbasaur", lvl=1, mods=0):
    pokemon = Pokemon()
    pokemon.learnset = []
    pokemon.energy = 100
    pokemon.friendship = 5
    #1. open file from pokemon/name.txt
    with open("pokemon/"+name.lower()+".txt") as f:
        content = f.readlines()
    f.close()
    content = [x.strip() for x in content]
    content = content[0].split("|")

    # turn our string into a list to choose from
    abil = [int(i) for i in content[8].split(":")]

    #calculate which foods our pokemon likes to eat
    l_flav = rand.randint(0,4)
    h_flav = rand.randint(0,4)
    while(l_flav == h_flav):
        h_flav = rand.randint(0,4)
    flavs = [l_flav,h_flav]
        
    pokemon.id_no = int(content[0])
    pokemon.species = content[1]
    pokemon.name = "N/A"
    pokemon.gender = getGender(content[2])
    pokemon.owner = "N/A"
    pokemon.height = int(content[3])
    pokemon.weight = float(content[4])
    pokemon.element = [int(i) for i in content[5].split(":")]
    pokemon.level = lvl
    pokemon.evol = content[11]
    pokemon.exp = howMuchXP(lvl)  
    pokemon.stats = [int(i) for i in content[6].split(":")]

    #generate pokemon's base stats, primary stats, and secondary stats
    p_vec = generatePVector(pokemon.stats[:6])
    new_stats = balanceStats(p_vec)
    ns_copy = pokemon.stats[:6]
    mx = max(ns_copy)
    sorder = [0,0,0,0,0,0]
    j = 0;
    while(mx):
        i = ns_copy.index(mx)
        sorder[j] = i
        ns_copy[i] = 0
        mx = max(ns_copy)
        j += 1

    pokemon.sorder = sorder
    #level up the pokemon's stats to match it's current level
    for i in range(lvl-1):
        lup_stats = levelUpRoll()
        mx = max(lup_stats)
        i = 0
        
        #assign our stat rolls from highest to lowest
        while(mx):
            st = sorder[i]
            new_stats[st] += mx
            if new_stats[st] > 255:
                new_stats[st] = 255
            ind = lup_stats.index(mx)
            lup_stats[ind] = 0
            mx = max(lup_stats)
            i += 1
            
    pokemon.stats[:6] = new_stats[:6]

    #Grab the pokemon's learnset and partition it
    mov = []
    m_lv = []
    tup = content[7].split(",")
    for t in tup:
        t = t.split(":")
        pokemon.learnset.append(t[:])
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
    new_moves = []
    while mi < len(m_lv) and m_lv[mi] <= lvl:
        alreadyLearned = 0
        for mmm in new_moves:
            if(int(pokemon.learnset[0][0]) == mmm.id_no):
                alreadyLearned = 1
        if not alreadyLearned:
            if len(new_moves) < 4:
                new_moves.append(moves[mov[mi]])
            else:
                if mods & 1:
                    r_min = 10000
                    min_i = 0
                    for m in range(4):
                        if new_moves[m].rank < r_min:
                            r_min = new_moves[m].rank
                            min_i = m
                    if moves[mov[mi]].rank >= new_moves[min_i].rank:
                        new_moves[min_i] = moves[mov[mi]]
                else:
                   new_moves[rand.randint(0,3)] = moves[mov[mi]]
            mi += 1
        pokemon.learnset = pokemon.learnset[1:]
    pokemon.moves = new_moves

    # Teach the pokemon some skills
    skills = [int(i) for i in content[12].split(":")]
    
    skills[0] += 5 + int(round(pokemon.stats[5] / 255.0 * 15))
    skills[1] += 5
    
    sum_skill = 0
    for s in pokemon.element:
        sum_skill += swimming[s]
    sum_skill /= 1.0*len(pokemon.element)
    
    skills[2] += int(sum_skill)
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
    skills[10] += max(0,(20 - int(round(pokemon.height / 100.0 * 20))))

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

    #clamp any skills above 20 or below 0 between those ranges
    for i in range(len(pokemon.skills)):
        pokemon.skills[i] = max(0, min(20,pokemon.skills[i]))

    #Adjust skills and stats according to pokemon's nature
    if pokemon.nature.stat_mods[0] != "-":
        for nm in pokemon.nature.stat_mods:
            tup = [int(i) for i in nm.split(":")]
            if tup[0] < 6:
                pokemon.stats[tup[0]] += tup[1]
            else:
                pokemon.friendship += tup[1]

    if pokemon.nature.skill_mods[0] != "-":
        for nm in pokemon.nature.skill_mods:
            tup = [int(i) for i in nm.split(":")]
            pokemon.skills[tup[0]] += tup[1]

    #adjust HP for 512
    pokemon.stats[0] *= 2
    
    pokemon.flavors = flavs
    pokemon.h_power = rand.randint(0,len(pk_types)-2)
    pokemon.n_def = content[13]
    pokemon.rarity = int(content[10])
    pokemon.is_shiny = isShiny()
    pokemon.item = items[getItem(content[9])]
    pokemon.hp = pokemon.stats[0]
    return pokemon

# ======================================================================
# === Saves a generated pokemon to a file                            ===
# ======================================================================
def savePokemon(pokemon,fname=""):
    fentry = ""
    fentry += str(pokemon.id_no)+"|"            # ID No.
    fentry += pokemon.species+"|"               # Species
    fentry += pokemon.name+"|"                  # Name
    fentry += pokemon.gender+"|"                # Gender
    fentry += str(pokemon.hp)+"|"               # HP
    fentry += str(pokemon.energy)+"|"           # Energy
    fentry += str(pokemon.friendship)+"|"       # Friendship
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
    for so in pokemon.sorder:                   # Stat Order
        fentry += str(so)+":"
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
    fentry += str(pokemon.item.id_no)+"|"       # Item
    for le in pokemon.learnset:
        fentry += le[0]+":"+le[1]+","
    fentry = fentry[:-1]

    if fname is "":
        fname = "pokemon/saved/"+pokemon.species+"-"+pokemon.owner+".txt"
    fname = fname.lower()
    fname = fname.replace(" ", "_")
    f = open(fname,'w')
    f.write(fentry)
    f.close

# ======================================================================
# === Allows the previously saved pokemon to be viewed               ===
# ======================================================================
def viewSaved():
    saved = [i[:-4] for i in listdir("pokemon/saved")]
    for s in saved:
        print s

def getSaved():
    saved = [i[:-4] for i in listdir("pokemon/saved")]
    return saved[:]
        
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
    pokemon.gender = content[3]
    pokemon.hp = int(content[4])
    pokemon.energy = int(content[5])
    pokemon.friendship = int(content[6])
    
    pokemon.height = int(content[7])
    pokemon.weight = float(content[8])
    pokemon.element = [int(i) for i in content[9].split(":")]
    pokemon.owner = content[10]
    pokemon.level = int(content[11])
    pokemon.evol = content[12]
    pokemon.exp = int(content[13])
    pokemon.stats = [int(i) for i in content[14].split(":")]
    pokemon.sorder = [int(i) for i in content[15].split(":")]
    pokemon.moves = [moves[int(i)] for i in content[16].split(":")]
    pokemon.skills = [int(i) for i in content[17].split(":")]
    pokemon.ability = abilities[int(content[18])]
    pokemon.nature = natures[int(content[19])]
    pokemon.h_power = int(content[20])
    pokemon.n_def = content[21]
    pokemon.flavors = [int(i) for i in content[22].split(":")]
    pokemon.rarity = int(content[23])
    if(content[24] == "False"):
        pokemon.is_shiny = False
    else:
        pokemon.is_shiny = True
    pokemon.item = items[int(content[25])]
    pokemon.learnset = []

    if len(content) > 26:
        sl = content[26].split(",")
        for s in sl:
            pokemon.learnset.append(s.split(":")[:])
    return pokemon

# ======================================================================
# === Loads all saved pokemon and pushes them on the stack           ===
# ======================================================================
def loadAll(searchst=""):
    sav = getSaved()
    for s in sav:
        if searchst+"-" in s:
            pokePush(loadPokemon(s),s)
   
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
def catchAttempt(pokemon, status, ball_type):
    #1. call load pokemon with name
    hp_mod = 4 - int(round(4.0*(pokemon.hp / (pokemon.stats[0]*1.0))))
    
    #2. get the rarity from the loaded pokemon
    rarity = pokemon.rarity
    
    #3. return ball_type - (hp + status) + rarity
    return max(1,ball_type - (hp_mod + 2*status) + rarity)

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
# === Calculates the target number to beat for a pokemon to obey the ===
# === trainer's orders based on that trainer's training level        ===
# === p_train -- the player's training skill points                  ===
# === pk -- the pokemon who is being ordered                         ===
# ======================================================================
def orderAttempt(p_train, pk):
    frnd = pk.friendship
    return skillAttempt(p_train, max(1,10 - (frnd / 2.0)))

PERSUASION = 0
INTIMIDATION = 1
# ======================================================================
# === Calculates the target number to beat for either persuasion or  ===
# === intimidation                                                   ===
# ======================================================================
def speechAttempt(p_speech, p_charisma, t_speech, s_type=0):
    diff = 0
    skill = 0
    if s_type:
        skill = min(20,abs(p_speech - p_charisma) + 1)
    else:
        skill = min(20, int(round((p_speech + p_charisma) / 2.0 + 1)))
    diff = min(10, int(round(t_speech / 2.0 + 1)))
    return skillAttempt(skill, diff)
        
    

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
name_stack = []
def pokePush(pokemon, name=""):
    poke_stack.append(pokemon)
    if len(name):
        name_stack.append(name)
    else:
        name_stack.append(pokemon.species+"-"+pokemon.owner+".txt")

def pokePop(pos=-1):
    global poke_stack
    if pos == -1:
        poke_stack = poke_stack[:pos]
    elif pos == 0:
        poke_stack = poke_stack[pos+1:]
    else:
        poke_stack = poke_stack[pos+1:]+poke_stack[:pos]
def pokeGet(ind):
    return poke_stack[ind]

def pokePrint():
    line = 2*len("| ") + 3 + 16 + len(" | ") + 32
    print '-'*line
    for i in range(len(poke_stack)):
        st = "| "+padString(str(i),3, LEFT)
        st += padString(poke_stack[i].species,16,LEFT)+" | "
        st += padString(name_stack[i],32,LEFT)+" |"
        print st
        print "-"*line

def pokeSave(ref=""):
    for i in range(len(poke_stack)):
        if(len(ref)):
            savePokemon(poke_stack[i],"pokemon/saved/"+ref+"-"+name_stack[i]+".txt")
            name_stack[i] = ref+"-"+name_stack[i]
        else:
            savePokemon(poke_stack[i],"pokemon/saved/"+name_stack[i]+".txt")

def pokeExport():
    for i in range(len(poke_stack)):
        exportPokemon(poke_stack[i],"pokemon/export/"+name_stack[i]+".txt")
        
"""
================================================================================
PRINT FUNCTIONS
================================================================================
"""

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

def writeWrapped(f,string, length, offset, lead="", trail=""):
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
            f.write(lead+padString(tok,cor_len,LEFT)+trail+"\n")
            tok = " "*offset
        i += 1
    f.write(lead+padString(tok,cor_len,LEFT)+trail+"\n")

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
            if(int(tup[0]) < 6):
                stat_string += pk_stats[int(tup[0])]+": "
            else:
                stat_string += pk_stats[7]+": "
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
        e_string += "["+pk_types[e]+"]"

    title = "* "+padString(subject.species+" ("+subject.gender+")",26,LEFT)
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
            stat_str += pk_stats[i]+": "+str(subject.hp)+"/"+st+"  "
        elif i < 6:
            stat_str += pk_stats[i]+": "+st+"  "
        elif i == 6:
            stat_str2 += pk_stats[i]+": "+str(subject.energy)+"/"+st+"   "
        elif i == 7:
            stat_str2 += pk_stats[i]+": "+str(subject.friendship)+"/"+st+"   "
    stat_str = "| "+padString(stat_str,76,LEFT)+" |"
    stat_str2 = "| "+padString(stat_str2,51,LEFT)
    stat_str2 += padString("Shiny: "+str(subject.is_shiny),25,RIGHT)+" |"

    s_order = "Stat Ordering: "
    for i in subject.sorder:
        s_order += pk_stats[i]+", "
    s_order = s_order[:-2]
    s_order = "| "+padString(s_order,76,LEFT)+" |"

    hp_type = "| "+padString("Hidden Power Type: "+pk_types[subject.h_power], 30, LEFT)
    
    flav = padString("Likes: "+flavors[subject.flavors[0]],26,RIGHT)
    flav += padString("Hates: "+flavors[subject.flavors[1]],20,RIGHT)+" |"

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
    print s_order
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

def writeItem(f,id_no):
    title = "* "+padString(items[id_no].name,38,LEFT)+padString("#"
                +str(items[id_no].id_no),38,RIGHT)+" *"
    price = padString("Buy Price: "+items[id_no].cost, 30, LEFT)
    price += padString("Sell Price: "+items[id_no].sell,46,LEFT)
    
    fling = padString("Fling Damage: "+str(items[id_no].fling_dmg),30,LEFT)
    fling += padString("Fling Effect: "+items[id_no].fling_effect,46,LEFT)
    
    natural_gift = padString("Natural Gift Damage: "+str(items[id_no].nature_dmg),30,LEFT)
    natural_gift += padString("Natural Gift Type: "+items[id_no].nature_type,46,LEFT)

    
    f.write("*"*80+"\n")
    f.write(title+"\n")
    f.write("*"*80+"\n")
    f.write("| "+price+" |"+"\n")
    f.write("-"*80+"\n")
    f.write("| "+fling+" |"+"\n")
    f.write("-"*80+"\n")
    f.write("| "+natural_gift+" |"+"\n")
    f.write("-"*80+"\n")
    desc = items[id_no].description
    writeWrapped("Description: "+desc, 80,
                 len("Description: "), "| ", " |")
    f.write("-"*80+"\n")
            
def writeMove(f, id_no):
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

    f.write("*"*80+"\n")
    f.write(title+"\n")
    f.write("*"*80+"\n")
    f.write("="*80+"\n")
    f.write("| "+padString("Battle Info", 76, CENTER)+" |"+"\n")
    f.write("="*80+"\n")
    f.write(pp_info+"\n")
    f.write("-"*80+"\n")
    f.write(classifier+"\n")
    f.write("-"*80+"\n")
    f.write(move_info+"\n")
    f.write("-"*80+"\n")
    desc = moves[id_no].description
    writeWrapped(f,"Description: "+desc, 80,
                 len("Description: "), "| ", " |")
    f.write("="*80+"\n")
    f.write("| "+padString("Contest Info", 76, CENTER)+" |"+"\n")
    f.write("="*80+"\n")
    f.write(cont_info+"\n")
    f.write("-"*80+"\n")
    desc = moves[id_no].c_description
    writeWrapped(f,"Description: "+desc, 80,
            len("Description: "), "| ", " |")
    f.write("="*80+"\n")

def writeNature(f,id_no):
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
    f.write("*"*80+"\n")
    f.write(title+"\n")
    f.write("*"*80+"\n")
    writeWrapped(f,"Stat Mods: "+stat_string, 80, len("Stat Mods: "),"| ", " |")
    f.write("-"*80+"\n")
    writeWrapped(f,"Skill Mods: "+skill_string, 80, len("Skill Mods: "), "| ", " |")
    f.write("-"*80+"\n")
    writeWrapped(f,"Description: "+desc, 80, len("Description: "), "| ", " |")
    f.write("-"*80+"\n")

def writeAbility(f,id_no):
    title = "* "+padString(abilities[id_no].name,38,LEFT)
    title += padString("#"+str(abilities[id_no].id_no),38,RIGHT)+" *"
    desc = abilities[id_no].description
    f.write("*"*80+"\n")
    f.write(title+"\n")
    f.write("*"*80+"\n")
    writeWrapped(f,"Description: "+desc, 80,
            len("Description: "), "| ", " |")
    f.write("-"*80+"\n")
            
def exportPokemon(subject, ref=""):
    if ref is "":
        if subject.owner == "N/A":
            ref = "pokemon/export/"+subject.species+"-unclaimed.txt"
        else:
            ref = "pokemon/export/"+subject.species+"-"+subject.owner+".txt"
    ref = ref.lower()
    ref = ref.replace(" ", "_")
    f = open(ref,'w')
    e_string = ""
    for e in subject.element:
        e_string += "["+pk_types[e]+"]"

    title = "* "+padString(subject.species+" ("+subject.gender+")",26,LEFT)
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
            stat_str += pk_stats[i]+": "+str(subject.hp)+"/"+st+"  "
        elif i < 6:
            stat_str += pk_stats[i]+": "+st+"  "
        elif i == 6:
            stat_str2 += pk_stats[i]+": "+str(subject.energy)+"/"+st+"   "
        elif i == 7:
            stat_str2 += pk_stats[i]+": "+str(subject.friendship)+"/"+st+"   "
    stat_str = "| "+padString(stat_str,76,LEFT)+" |"
    stat_str2 = "| "+padString(stat_str2,51,LEFT)
    stat_str2 += padString("Shiny: "+str(subject.is_shiny),25,RIGHT)+" |"

    s_order = "Stat Ordering: "
    for i in subject.sorder:
        s_order += pk_stats[i]+", "
    s_order = s_order[:-2]
    s_order = "| "+padString(s_order,76,LEFT)+" |"

    hp_type = "| "+padString("Hidden Power Type: "+pk_types[subject.h_power], 30, LEFT)
    
    flav = padString("Likes: "+flavors[subject.flavors[0]],26,RIGHT)
    flav += padString("Hates: "+flavors[subject.flavors[1]],20,RIGHT)+" |"

    sk_string = ""
    for sk in range(len(subject.skills)):
        if subject.skills[sk] > 0:
            sk_string += padString(pk_skills[sk]+": "+str(subject.skills[sk]),25,LEFT)

    f.write("="*80+"\n")
    f.write("*"*80+"\n")
    f.write(title+"\n")
    f.write("*"*80+"\n")
    f.write("="*80+"\n")
    f.write(p_info+"\n")
    f.write("-"*80+"\n")
    f.write(p_owner+n_ar+"\n")
    f.write("-"*80+"\n")
    f.write(l_info+"\n")
    f.write("-"*80+"\n")
    f.write(stat_str+"\n")
    f.write("-"*80+"\n")
    f.write(stat_str2+"\n")
    f.write("-"*80+"\n")
    f.write(s_order+"\n")
    f.write("-"*80+"\n")
    f.write(hp_type+flav+"\n")
    f.write("="*80+"\n")
    writeWrapped(f,sk_string,80,0,"| ", " |")
    f.write("="*80+"\n")
    f.write("\n\n\n")
    for m in subject.moves:
        writeMove(f, m.id_no)
        f.write("\n")
    f.write("\n\n")
    writeAbility(f,subject.ability.id_no)
    f.write("\n\n\n")
    writeNature(f,subject.nature.id_no)
    if subject.item.id_no > 0:
        f.write("\n")
        writeItem(f,subject.item.id_no)
    f.close()

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

l_level = [1,5,9,13,17,21,25,29,33,37,41,45,49,53]
learnset= ["Tackle","Howl","Sand Attack","Bite","Odor Sleuth","Roar","Swagger","Assurance",
           "Scary Face","Taunt","Embargo","Take Down", "Sucker Punch", "Crunch"]

def fLearnset(lev, learn):
    m_str = ""
    for i in range(len(learn)):
        m_str += str(findMove(learn[i]))+":"+str(lev[i])+","
    m_str = m_str[:-1]
    print m_str

