from asciiml import *
from header import *
from pokemon import *
from character import *
from pstack import *
"""
================================================================================
=== Pokemath provides basic functions for running the S.P.S. tabletop system ===
================================================================================
"""
# ======================================================================
# === Allows the previously saved pokemon to be viewed               ===
# ======================================================================
def viewSaved():
    pkmn = [i[:-4] for i in listdir("pokemon/saved")]
    play = listdir("players/")
    print "="*80
    print "| "+padString("Pokemon",76,CENTER)+" |"
    print "="*80
    for s in pkmn:
        print s
    print ""
    print "="*80
    print "| "+padString("Characters",76,CENTER)+" |"
    print "="*80
    for p in play:
        if p[-4:] == ".txt":
            print p[:-4]

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
# === Calculates the target number to beat for either persuasion or  ===
# === intimidation                                                   ===
# ======================================================================
def speechAttempt(player, t_speech, s_type="Persuasion"):
    s_type = s_type.lower()
    diff = 0
    skill = 0
    if s_type == "persuasion":
        skill = abs(player.getSkill(s_type) - player.getStat("Charisma"))
        skill += 1
    else:
        skill = (player.getSkill(s_type) + player.getStat("Charisma"))
        skill /= 2.0
        skill += 1
        skill = int(round(skill))
    skill = max(0, min(20, skill))
    diff = min(10, int(round(t_speech / 2.0 + 1)))
    return skillAttempt(skill, diff)
        
"""
================================================================================
DEV FUNCTIONS
================================================================================
"""
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

def train(pkm,p_list=["Pidgey","Rattata"],min_lvl=1,max_lvl=5):
    rand.seed(time.time())
    new_energy = pkm.getStat("Energy") - rand.randint(0,5)
    new_hp = pkm.getStat("HP") - rand.randint(0,5)
    xp_sum = 0
    while(new_energy > 0 and new_hp > 0):
        pkm.setStat("Energy",new_energy,SET)
        pkm.setStat("HP",new_hp,SET)
        name = p_list[rand.randint(0,len(p_list)-1)]
        lvl = rand.randint(min_lvl,max_lvl)
        opp = Pokemon(name, lvl)
        xp_sum += opp.calcXP()
        new_energy = pkm.getStat("Energy") - rand.randint(0,5)
        new_hp = pkm.getStat("HP") - rand.randint(0,5)
    return xp_sum    
    
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

"""
================================================================================
BEGIN SESSION SETUP: Put Startup Script Here
================================================================================
"""
rt2 = ["Caterpie", "Weedle", "Pidgey","Rattata","NidoranF","NidoranM"]
rt2mn = 4
rt2mx = 5

party = PokeStack("gm")
evan = Character(ld="evan_white-joe")
kian = Character(ld="kian_solari-kyle")
arthanis = Character(ld="arthanis-travis")
june = Character(ld="june-npc")
paul = Character(ld="paul-npc")
cliff = Character(ld="cliff-npc")
keith = Character(ld="keith-npc")

b1 = PokeStack("b1")
b2 = PokeStack("b2")
b3 = PokeStack("b3")
june_p = PokeStack("june")
paul_p = PokeStack("paul")
cliff_p = PokeStack("cliff")
keith_p = PokeStack("keith")
