from math import *
import random as rand
import time as time
from asciiml import *
from header import *
from rounding import *
from pokemon import *
from os import listdir, path

"""
================================================================================
CLASS CONSTANTS
================================================================================
"""
# Pokemon Creation Mods
RANKED = 1
SHADOW = 2

# XP Mods
WILD = 0
TRAINER = 10
LEADER = 20
CHAMPION = 30

# Stat/Skill function mods
SET = 0
MOD = 1

"""
================================================================================
HTML OUTPUT HELPER FUNCTIONS + CONSTANTS
================================================================================
"""
h_tab = "    "
t_ind = 0

def hprint(f,ln=""):
    global t_ind
    f.write(t_ind*h_tab+ln+"\n")
    
def htmlHeader(f, shiny=False):
    color = "#EEEEEE"
    if shiny:
        color = "#FFFFEE"
    global t_ind
    hprint(f,"<html>")
    t_ind+=1
    hprint(f,"<head>")
    t_ind+=1
    hprint(f,"<style>")
    t_ind+=1
    hprint(f,".title {")
    t_ind += 1
    hprint(f,"border-bottom: 1px solid black;")
    hprint(f,"width: 100%;")
    t_ind -= 1
    hprint(f,"}")
    hprint(f,".stats {")
    t_ind += 1
    hprint(f, "height: 10%;")
    hprint(f, "border: 1px solid black;")
    hprint(f, "border-radius: 10px;")
    hprint(f, "background: "+color+";")
    hprint(f, "box-shadow: 2px 2px 5px 0px #666666;")
    hprint(f, "margin-top: 10px;")
    hprint(f, "margin-bottom:10px;")
    t_ind -= 1
    hprint(f,"}")
    hprint(f,".cash {")
    t_ind += 1
    hprint(f, "height: 5%;")
    hprint(f, "border: 1px solid black;")
    hprint(f, "border-radius: 10px;")
    hprint(f, "background: "+color+";")
    hprint(f, "box-shadow: 2px 2px 5px 0px #666666;")
    hprint(f, "margin-top: 10px;")
    hprint(f, "margin-bottom:10px;")
    t_ind -= 1
    hprint(f,"}")
    hprint(f,".stat-sub1 {")
    t_ind += 1
    hprint(f, "height: 50%;")
    hprint(f, "margin-left:5px;")
    hprint(f, "margin-right:5px;")
    hprint(f, "border-bottom: 1px solid black;")
    t_ind -= 1
    hprint(f,"}")
    hprint(f,".stat-sub2 {")
    t_ind += 1
    hprint(f, "margin-left:5px;")
    hprint(f, "margin-right:5px;")
    hprint(f, "height: 50%;")
    t_ind -= 1
    hprint(f,"}")
    hprint(f,".sub-txt {")
    t_ind += 1
    hprint(f, "vertical-align:middle;")
    hprint(f, "padding-top: .5%;")
    hprint(f, "padding-left: .5%;")
    hprint(f, "margin: 0px;")
    t_ind -= 1
    hprint(f,"}")
    hprint(f,".section-head {")
    t_ind += 1
    hprint(f, "background: #BBCCFF;")
    hprint(f, "border-top: 1px solid black;")
    hprint(f, "border-left: 1px solid black;")
    hprint(f, "border-right: 1px solid black;")
    hprint(f, "box-shadow: 2px 2px 5px 0px #666666;")
    hprint(f, "margin-bottom:0px;")
    hprint(f, "margin-top: 10px;")
    t_ind -= 1
    hprint(f,"}")
    hprint(f,".section-body {")
    t_ind += 1
    hprint(f, "border: 1px solid black;")
    hprint(f, "margin-bottom: 10px;")
    hprint(f, "background: #EEFFFF;")
    hprint(f, "box-shadow: 2px 2px 5px 0px #666666;")
    t_ind -= 1
    hprint(f,"}")
    hprint(f,".moveset-top {")
    t_ind += 1
    hprint(f, "background: #DDCCFF;")
    hprint(f, "border: 1px solid black;")
    hprint(f, "box-shadow: 2px 2px 5px 0px #666666;")
    hprint(f, "margin-bottom:0px;")
    hprint(f, "margin-top: 10px;")
    t_ind -= 1
    hprint(f,"}")
    hprint(f,".moveset-middle {")
    t_ind += 1
    hprint(f, "background: #DDCCFF;")
    hprint(f, "border-bottom: 1px solid black;")
    hprint(f, "border-left: 1px solid black;")
    hprint(f, "border-right: 1px solid black;")
    hprint(f, "box-shadow: 2px 2px 5px 0px #666666;")
    hprint(f, "margin-bottom:0px;")
    hprint(f, "margin-top: 0px;")
    t_ind -= 1
    hprint(f,"}")
    hprint(f,".moveset-body {")
    t_ind += 1
    hprint(f, "border: 1px solid black;")
    hprint(f, "margin-bottom: 0px;")
    hprint(f, "background: #EEFFFF;")
    hprint(f, "box-shadow: 2px 2px 5px 0px #666666;")
    t_ind -= 1
    hprint(f,"}")
    hprint(f,".sub-header {")
    t_ind += 1
    hprint(f, "border: 1px solid black;")
    hprint(f, "border-radius: 10px;")
    hprint(f, "background: #EEEEEE;")
    hprint(f, "margin:10px;")
    hprint(f, "padding-left:1%;")
    t_ind -= 1
    hprint(f,"}")
    hprint(f,".sub-section {")
    t_ind += 1
    hprint(f, "margin:10px;")
    hprint(f, "padding-left:.5%;")
    t_ind -= 1
    hprint(f,"}")
    hprint(f,".nopad {")
    t_ind += 1
    hprint(f, "margin-top: 0px;")
    hprint(f, "margin-bottom: 0px;")
    hprint(f, "padding-top: 0px;")
    hprint(f, "padding-left: .5%;")
    hprint(f, "padding-bottom: 0px;")
    t_ind -= 1
    hprint(f,"}")
    t_ind -= 1
    hprint(f,"</style>")
    hprint(f,"<script type=\"text/javascript\">")
    t_ind += 1
    hprint(f,"function hide(x) {")
    t_ind += 1
    hprint(f,"var y = document.getElementById(x);")
    hprint(f,"if (y.style.display === \"none\") {")
    t_ind += 1
    hprint(f,"y.style.display = \"block\";")
    t_ind -= 1
    hprint(f,"} else {")
    t_ind += 1
    hprint(f,"y.style.display = \"none\";")
    t_ind -= 1
    hprint(f,"}")
    t_ind -= 1
    hprint(f,"}")
    t_ind -= 1
    hprint(f,"</script>")
    t_ind -= 1
    hprint(f,"</head>")
    hprint(f,"<body>")
    t_ind += 1

def htmlFooter(f):
    global t_ind
    t_ind -= 1
    hprint(f,"</body>")
    t_ind -= 1
    hprint(f,"</html>")
    
"""
================================================================================
POKEMON CLASS
================================================================================
"""
class Pokemon:
    bonus = {'normal':0,'evolve1':10,'evolvem':20,'noevol':15,'mythic':15,'legendary':30}
    def __init__(self, name="",lvl=1,mods=0,ld=""):
        self.id_no = 0
        self.species = ""
        self.name = ""
        self.gender = ""
        self.height = 0 # in inches
        self.weight = 0.0 #in lbs
        self.element = []
        self.owner = ""
        self.level = 1
        self.evol = 5
        self.exp = 0
        self.stats = {"HP":0,"ATK":0,"DEF":0,"SP. ATK":0,"SP. DEF":0,"SPD":0,"ENERGY":0,"FRIENDSHIP":0,
                     "MAX HP":0,"MAX ENERGY":0,"MAX FRIENDSHIP":0}
        self.sorder = []
        self.moves = []
        self.skills = {"hiking":0,"jumping":0,"swimming":0,"climbing":0,"fishing":0,
                       "hunting":0,"farming":0,"tracking":0,"foraging":0,"mining":0,
                       "sneaking":0,"instinct":0,"performing":0,"forecasting":0,
                       "perception":0,"sensing":0,"fortitude":0,"intimidation":0,
                       "persuasion":0,"cut":0,"fly":0,"surf":0,"strength":0,"rock smash":0,
                       "headbutt":0,"defog":0,"flash":0,"whirlpool":0,"waterfall":0,
                       "rock climb":0,"dig":0,"teleport":0,"dive":0,"lockpicking":0,
                       "pickpocketing":0,"esp":0}
        self.ability = Ability()
        self.nature = Nature()
        self.h_power = 0
        self.status = 0
        self.n_def = ""
        self.flavors = []
        self.rarity = 0
        self.is_shiny = False
        self.item = Item()
        self.learnset = []
        if len(name):
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
                
            self.id_no = int(content[0])
            self.species = content[1]
            self.name = "N/A"
            self.gender = getGender(content[2])
            self.owner = "N/A"
            self.height = int(content[3])
            self.weight = float(content[4])
            self.element = [int(i) for i in content[5].split(":")]
            self.level = lvl
            self.evol = content[11]
            self.exp = howMuchXP(lvl)
            l_stats = [int(i) for i in content[6].split(":")]

            #generate pokemon's base stats, primary stats, and secondary stats
            p_vec = generatePVector(l_stats[:6])
            new_stats = balanceStats(p_vec)
            ns_copy = l_stats[:6]
            mx = max(ns_copy)
            sorder = [0,0,0,0,0,0]
            j = 0;
            while(mx):
                i = ns_copy.index(mx)
                sorder[j] = i
                ns_copy[i] = 0
                mx = max(ns_copy)
                j += 1

            self.sorder = sorder
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

            # Transfer stats into our stat dict      
            l_stats[:6] = new_stats[:6]
            for i in range(len(l_stats)):
                self.stats[pk_stats[i].upper()] = l_stats[i]
            self.stats["MAX HP"] = self.stats["HP"]

            #Grab the pokemon's learnset and partition it
            mov = []
            m_lv = []
            tup = content[7].split(",")
            for t in tup:
                t = t.split(":")
                self.learnset.append(t[:])
                mov.append(int(t[0]))
                m_lv.append(int(t[1]))

            if mods & 2:
                s_count = 0
                new_species = "Dark "+self.species
                self.ability = abilities[124]
                self.species = new_species
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
                    if(int(self.learnset[0][0]) == mmm.id_no):
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
                self.learnset = self.learnset[1:]
            self.moves = new_moves

            # Teach the pokemon some skills
            skills = [int(i) for i in content[12].split(":")]
            
            skills[0] += 5 + int(round(self.stats["SPD"] / 255.0 * 15))
            skills[1] += 5
            
            sum_skill = 0
            for s in self.element:
                sum_skill += swimming[s]
            sum_skill /= 1.0*len(self.element)
            
            skills[2] += int(sum_skill)
            skills[3] += 5
            skills[4] += 5
            skills[5] += 5

            sum_skill = 0
            for s in self.element:
                sum_skill += farming[s]
            sum_skill /= 1.0*len(self.element)
            
            skills[6] += int(sum_skill)
            skills[7] += 5
            skills[8] += 5

            sum_skill = 0
            for s in self.element:
                sum_skill += mining[s]
            sum_skill /= 1.0*len(self.element)
            
            skills[9] += int(sum_skill)
            skills[10] += max(0,(20 - int(round(self.height / 100.0 * 20))))

            sum_skill = 0
            for s in self.element:
                sum_skill += instinct[s]
            sum_skill /= 1.0*len(self.element)
            
            skills[11] += int(sum_skill)
            skills[12] += 5
            skills[13] += 5
            skills[14] += 5

            sum_skill = 0
            for s in self.element:
                sum_skill += sensing[s]
            sum_skill /= 1.0*len(self.element)
            
            skills[15] += int(sum_skill)

            sum_skill = 0
            for s in self.element:
                sum_skill += fortitude[s]
            sum_skill /= 1.0*len(self.element)
            
            skills[16] += int(sum_skill)

            sum_skill = 0
            for s in self.element:
                sum_skill += intimidation[s]
            sum_skill /= 1.0*len(self.element)
            
            skills[17] += int(sum_skill)

            sum_skill = 0
            for s in self.element:
                sum_skill += persuasion[s]
            sum_skill /= 1.0*len(self.element)
            
            skills[18] += int(sum_skill)

            #Clamp skills between 0 and 20
            for i in range(len(skills)):
                skills[i] = min(20,max(0,skills[i]))
                
            for i in range(len(skills)):
                self.skills[pk_skills[i].lower()] = skills[i]

            rand.seed(time.time())
            if(not(mods & 2)):
                self.ability = abilities[abil[rand.randint(0,len(abil)-1)]]
            n = rand.randint(1,len(natures)-1)
            self.nature = natures[n]

            #Adjust skills and stats according to pokemon's nature
            if self.nature.stat_mods[0] != "-":
                for nm in self.nature.stat_mods:
                    tup = [int(i) for i in nm.split(":")]
                    self.stats[pk_stats[tup[0]].upper()] += tup[1]

            if self.nature.skill_mods[0] != "-":
                for nm in self.nature.skill_mods:
                    tup = [int(i) for i in nm.split(":")]
                    self.skills[pk_skills[tup[0]].lower()] += tup[1]

            #adjust HP for 512
            self.stats["HP"] *= 2
            self.stats["MAX HP"] *= 2
            
            self.flavors = flavs
            self.h_power = rand.randint(0,len(pk_types)-2)
            self.n_def = content[13]
            self.rarity = int(content[10])
            self.is_shiny = isShiny()
            self.item = items[getItem(content[9])]
        if len(ld):
            self.load(ld)

    def lvlUp(self,st=[]):
        self.level += 1
        if not len(st):
            self.exp = howMuchXP(self.level)
            st = levelUpRoll()
        st.sort()
        st.reverse()
        for s in self.sorder:
            if pk_stats[s]=="HP":
                self.stats[pk_stats[s].upper()] += st[0]*2
                self.stats["MAX HP"] += st[0]*2
            else:
                self.stats[pk_stats[s].upper()] += st[0]
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
                self.stats[pk_stats[i].upper()] += 2*self.bonus[b_type.lower()]
                self.stats["MAX HP"] += 2*self.bonus[b_type.lower()]
            else:
                self.stats[pk_stats[i].upper()] += self.bonus[b_type.lower()]

    def evolve(self, evolution, flags=0):
        pk = Pokemon(evolution, self.level-1, flags)
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
        for s in self.skills:
            self.skills[s] = pk.skills[s]
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

    def pprint(self):
        e_string = ""
        for e in self.element:
            e_string += "["+pk_types[e]+"]"

        title = "* "+padString(self.species+" ("+self.gender+")",26,LEFT)
        title += padString(e_string, 25, CENTER)
        title += padString("#"+str(self.id_no),25,RIGHT)+" *"

        l_info = "| "+padString("Lvl: "+str(self.level),25,LEFT)
        l_info += padString("Exp: "+str(self.exp),26,LEFT)
        l_info += padString("Evolve: "+self.evol,25,RIGHT)+" |"

        p_info = "| "+padString("Nickname: "+self.name,38,LEFT)
        p_info += padString("Height: "+inchToFt(self.height), 19, LEFT)
        p_info += padString("Weight: "+str(self.weight)+"lbs.", 19, RIGHT)+" |"

        p_owner = "| "+padString("Owner: "+self.owner,26,LEFT)
        n_ar = padString("Natural Armor: "+self.n_def,25,RIGHT)+" |"

        stat_str = ""
        stat_str2 = ""
        for i in range(8):
            st = str(self.stats[pk_stats[i].upper()])
            if not i:
                stat_str += pk_stats[i]+": "+st+"/"+str(self.stats["MAX HP"])+"  "
            elif i < 6:
                stat_str += pk_stats[i]+": "+st+"  "
            elif i == 6:
                stat_str2 += pk_stats[i]+": "+st+"/"+str(self.stats["MAX ENERGY"])+"   "
            elif i == 7:
                stat_str2 += pk_stats[i]+": "+st+"/"+str(self.stats["MAX FRIENDSHIP"])+"   "
        stat_str = "| "+padString(stat_str,76,LEFT)+" |"
        stat_str2 = "| "+padString(stat_str2,51,LEFT)
        stat_str2 += padString("Shiny: "+str(self.is_shiny),25,RIGHT)+" |"

        s_order = "Stat Ordering: "
        for i in self.sorder:
            s_order += pk_stats[i]+", "
        s_order = s_order[:-2]
        s_order = "| "+padString(s_order,76,LEFT)+" |"

        hp_type = "| "+padString("Hidden Power Type: "+pk_types[self.h_power], 30, LEFT)
        
        flav = padString("Likes: "+flavors[self.flavors[0]],26,RIGHT)
        flav += padString("Hates: "+flavors[self.flavors[1]],20,RIGHT)+" |"

        sk_string = ""
        for i in range(len(pk_skills)):
            if self.skills[pk_skills[i].lower()] > 0:
                p_str = pk_skills[i]+": "+str(self.skills[pk_skills[i].lower()])
                sk_string += padString(p_str,25,LEFT)

        print "="*80
        print "*"*80
        print title
        print "*"*80
        print "="*80
        print p_info
        print "-"*80
        print p_owner+padString("Status: "+self.getStatus(),25,CENTER)+n_ar
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
        for m in self.moves:
            m.pprint()
            print ""
        print "\n"
        self.ability.pprint()
        print "\n\n"
        self.nature.pprint()
        if self.item.id_no > 0:
            print "\n"
            self.item.pprint()

    def export(self, ref=""):
        if ref is "":
            if self.owner == "N/A":
                ref = "pokemon/export/"+self.species+"-unclaimed.txt"
            else:
                ref = "pokemon/export/"+self.species+"-"+self.owner+".txt"
        ref = ref.lower()
        ref = ref.replace(" ", "_")
        f = open(ref,'w')
        e_string = ""
        for e in self.element:
            e_string += "["+pk_types[e]+"]"

        title = "* "+padString(self.species+" ("+self.gender+")",26,LEFT)
        title += padString(e_string, 25, CENTER)
        title += padString("#"+str(self.id_no),25,RIGHT)+" *"

        l_info = "| "+padString("Lvl: "+str(self.level),25,LEFT)
        l_info += padString("Exp: "+str(self.exp),26,LEFT)
        l_info += padString("Evolve: "+self.evol,25,RIGHT)+" |"

        p_info = "| "+padString("Nickname: "+self.name,38,LEFT)
        p_info += padString("Height: "+inchToFt(self.height), 19, LEFT)
        p_info += padString("Weight: "+str(self.weight)+"lbs.", 19, RIGHT)+" |"

        p_owner = "| "+padString("Owner: "+self.owner,26,LEFT)

        n_ar = padString("Natural Armor: "+self.n_def,25,LEFT)+" |"

        stat_str = ""
        stat_str2 = ""
        for i in range(8):
            st = str(self.stats[pk_stats[i].upper()])
            if not i:
                stat_str += pk_stats[i]+": "+st+"/"+str(self.stats["MAX HP"])+"  "
            elif i < 6:
                stat_str += pk_stats[i]+": "+st+"  "
            elif i == 6:
                stat_str2 += pk_stats[i]+": "+st+"/"+str(self.stats["MAX ENERGY"])+"   "
            elif i == 7:
                stat_str2 += pk_stats[i]+": "+st+"/"+str(self.stats["MAX FRIENDSHIP"])+"   "
        stat_str = "| "+padString(stat_str,76,LEFT)+" |"
        stat_str2 = "| "+padString(stat_str2,51,LEFT)
        stat_str2 += padString("Shiny: "+str(self.is_shiny),25,RIGHT)+" |"

        s_order = "Stat Ordering: "
        for i in self.sorder:
            s_order += pk_stats[i]+", "
        s_order = s_order[:-2]
        s_order = "| "+padString(s_order,76,LEFT)+" |"

        hp_type = "| "+padString("Hidden Power Type: "+pk_types[self.h_power], 30, LEFT)
        
        flav = padString("Likes: "+flavors[self.flavors[0]],26,RIGHT)
        flav += padString("Hates: "+flavors[self.flavors[1]],20,RIGHT)+" |"

        sk_string = ""
        for i in range(len(pk_skills)):
            if self.skills[pk_skills[i].lower()] > 0:
                p_str = pk_skills[i]+": "+str(self.skills[pk_skills[i].lower()])
                sk_string += padString(p_str,25,LEFT)

        f.write("="*80+"\n")
        f.write("*"*80+"\n")
        f.write(title+"\n")
        f.write("*"*80+"\n")
        f.write("="*80+"\n")
        f.write(p_info+"\n")
        f.write("-"*80+"\n")
        f.write(p_owner+padString("Status: "+self.getStatus(),25,LEFT)+n_ar+"\n")
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
        for m in self.moves:
            m.export(f)
            f.write("\n")
        f.write("\n\n")
        self.ability.export(f)
        f.write("\n\n\n")
        self.nature.export(f)
        if self.item.id_no > 0:
            f.write("\n")
            self.item.export(f)
        f.close()

    def html(self, ref=""):
        global t_ind
        if ref is "":
            if self.owner == "N/A":
                ref = "pokemon/html/"+self.species+"-unclaimed.html"
            else:
                ref = "pokemon/html/"+self.species+"-"+self.owner+".html"
        ref = ref.lower()
        ref = ref.replace(" ", "_")
        f = open(ref,'w')
        htmlHeader(f, self.is_shiny)
        hprint(f,"<div class=\"title\">")
        t_ind+=1
        hprint(f,"<table style=\"width:100%;\">")
        t_ind+=1
        hprint(f,"<tr>")
        t_ind+=1
        hstr = "<td style=\"text-align:left;\""
        hstr+= "><h1>"+self.species
        hstr+= " ("+self.gender+")"+"</h1></td>"
        hprint(f,hstr)
        e_string = ""
        for e in self.element:
            e_string += "["+pk_types[e]+"]"
        hprint(f,"<td style=\"text-align:center;\"><h3>"+e_string+"</h3></td>")
        hstr = "<td style=\"text-align:right;\""
        hstr+= "><h1>#"+str(self.id_no)+"</h1></td>"
        hprint(f,hstr)
        t_ind-=1
        hprint(f,"</tr>")
        t_ind-=1
        hprint(f,"</table>")
        t_ind-=1
        hprint(f,"</div>")
        hprint(f,"<div class=\"cash\">")
        t_ind+=1
        hprint(f,"<div class=\"sub-txt\">")
        t_ind+=1
        hprint(f,"&nbsp;&nbsp;")
        hstr = "<strong>Nickname:</strong> "+self.name+"&nbsp;&nbsp;&nbsp;&nbsp;"
        hprint(f,hstr)
        hstr = "<strong>Owner:</strong> "+self.owner+"&nbsp;&nbsp;&nbsp;&nbsp;"
        hprint(f,hstr)
        hstr = "<strong>Ht:</strong> "+inchToFt(self.height)+"&nbsp;&nbsp;&nbsp;&nbsp;"
        hprint(f,hstr)
        hstr = "<strong>Wt:</strong> "+str(self.weight)+"lbs &nbsp;&nbsp;&nbsp;&nbsp;"
        hprint(f,hstr)
        t_ind-=1
        hprint(f,"</div>")
        t_ind-=1
        hprint(f,"</div>")
        hprint(f,"<div class=\"cash\">")
        t_ind+=1
        hprint(f, "<div class=\"sub-txt\">")
        t_ind+=1
        hprint(f,"&nbsp;&nbsp;")
        hstr = "<strong>Level:</strong> "+str(self.level)+"&nbsp;&nbsp;&nbsp;&nbsp;"
        hprint(f,hstr)
        hstr = "<strong>Exp:</strong> "+str(self.exp)+"&nbsp;&nbsp;&nbsp;&nbsp;"
        hprint(f,hstr)
        hstr = "<strong>Status:</strong> "+cond[self.status]+"&nbsp;&nbsp;&nbsp;&nbsp;"
        hprint(f,hstr)
        hstr = "<strong>Natural Armor:</strong> "+self.n_def+"&nbsp;&nbsp;&nbsp;&nbsp;"
        hprint(f,hstr)
        hstr = "<strong>Evolve:</strong> "+self.evol+"&nbsp;&nbsp;&nbsp;&nbsp;"
        hprint(f,hstr)
        t_ind-=1
        hprint(f,"</div>")
        t_ind-=1
        hprint(f,"</div>")
        hprint(f,"<div class=\"cash\">")
        t_ind+=1
        hprint(f,"<div class=\"sub-txt\">")
        t_ind+=1
        hprint(f,"&nbsp;&nbsp;")
        hstr = "<strong>Hidden Power:</strong> "
        hstr+= pk_types[self.h_power]+"&nbsp;&nbsp;&nbsp;&nbsp;"
        hprint(f,hstr)
        hstr = "<strong>Likes:</strong> "
        hstr+= flavors[self.flavors[0]]+" Foods &nbsp;&nbsp;&nbsp;&nbsp;"
        hprint(f,hstr)
        hstr = "<strong>Hates:</strong> "
        hstr+= flavors[self.flavors[1]]+" Foods &nbsp;&nbsp;&nbsp;&nbsp;"
        hprint(f,hstr)
        t_ind-=1
        hprint(f,"</div>")
        t_ind-=1
        hprint(f,"</div>")
        hprint(f,"<div class=\"stats\">")
        t_ind+=1
        hprint(f,"<div class=\"stat-sub1\">")
        t_ind+=1
        hprint(f,"<div class=\"sub-txt\">")
        t_ind+=1
        for i in range(6):
            if i:
                hstr = "<strong>"+pk_stats[i]+":</strong> "
                hstr+= str(self.stats[pk_stats[i]])
                hstr+= "&nbsp;&nbsp;&nbsp;&nbsp;"
                hprint(f,hstr)
            else:
                hstr = "<strong>"+pk_stats[i]+":</strong> "
                hstr+= str(self.stats[pk_stats[i]])
                hstr+= "/"+str(self.stats["MAX HP"])
                hstr+= "&nbsp;&nbsp;&nbsp;&nbsp;"
                hprint(f,hstr)
        t_ind-=1
        hprint(f,"</div>")
        t_ind-=1
        hprint(f,"</div>")
        hprint(f,"<div class=\"stat-sub2\">")
        t_ind+=1
        hprint(f,"<div class=\"sub-txt\">")
        t_ind+=1
        hstr = "<strong>Energy:</strong> "
        hstr+= str(self.stats["ENERGY"])+"/"+str(self.stats["MAX ENERGY"])
        hstr+= "&nbsp;&nbsp&nbsp;&nbsp"
        hprint(f,hstr)
        hstr = "<strong>Friendship:</strong> "
        hstr+= str(self.stats["FRIENDSHIP"])+"/"+str(self.stats["MAX FRIENDSHIP"])
        hstr+= "&nbsp;&nbsp&nbsp;&nbsp"
        hprint(f,hstr)
        hstr = "<strong>Status:</strong> "
        hstr+= cond[self.status]
        hstr+= "&nbsp;&nbsp&nbsp;&nbsp"
        hprint(f,hstr)
        t_ind-=1
        hprint(f,"</div>")
        t_ind-=1
        hprint(f,"</div>")
        t_ind-=1
        hprint(f,"</div>")
        hprint(f,"<div class=\"section-head\">")
        t_ind+=1
        hprint(f,"<div class=\"sub-txt\">")
        t_ind+=1
        hprint(f,"<h3 class=\"nopad\">Skills</h3>")
        t_ind-=1
        hprint(f,"</div>")
        t_ind-=1
        hprint(f,"</div>")
        hprint(f,"<div class=\"section-body\">")
        t_ind+=1
        hprint(f,"<div class=\"sub-txt\">")
        t_ind+=1
        hprint(f,"<table style=\"width:100%;\">")
        t_ind+=1
        hprint(f,"<tr>")
        t_ind+=1
        counter = 0
        for i in range(len(pk_skills)):
            if self.skills[pk_skills[i].lower()]:
                hstr = "<td><strong>"+pk_skills[i]+":</strong> "
                hstr+= str(self.skills[pk_skills[i].lower()])
                hstr+= "&nbsp;&nbsp&nbsp;&nbsp"+"</td>"
                hprint(f,hstr)
                counter+=1
            if counter == 3:
                t_ind-=1
                hprint(f,"</tr>")
                hprint(f,"<tr>")
                t_ind+=1
                counter = 0
        while(counter < 3):
            hprint(f,"<td></td>")
            counter += 1
        t_ind-=1
        hprint(f,"</tr>")
        t_ind-=1
        hprint(f,"</table>")
        t_ind-=1
        hprint(f,"</div>")
        t_ind-=1
        hprint(f,"</div>")
        hprint(f,"<div class=\"title\">")
        t_ind+=1
        hstr = "<h2 class=\"nopad\" style=\"padding-top:10px;\">Ability</h2>"
        hprint(f,hstr)
        t_ind-=1
        hprint(f,"</div>")
        self.ability.html(f)
        hprint(f,"<div class=\"title\">")
        t_ind+=1
        hstr = "<h2 class=\"nopad\" style=\"padding-top:20px;\">Nature</h2>"
        hprint(f,hstr)
        t_ind-=1
        hprint(f,"</div>")
        self.nature.html(f)
        hprint(f,"<div class=\"title\">")
        t_ind+=1
        hstr = "<h2 class=\"nopad\" style=\"padding-top:20px;\">Item</h2>"
        hprint(f,hstr)
        t_ind-=1
        hprint(f,"</div>")
        self.item.html(f)
        hprint(f,"<div class=\"title\">")
        t_ind+=1
        hstr = "<h2 class=\"nopad\" style=\"padding-top:20px;\">Moveset</h2>"
        hprint(f,hstr)
        t_ind-=1
        hprint(f,"</div>")
        for i in range(len(self.moves)):
            self.moves[i].html(f,i)
        htmlFooter(f)
        f.close()
        

    def save(self, fname=""):
        fentry = ""
        fentry += str(self.id_no)+"|"            # ID No.
        fentry += self.species+"|"               # Species
        fentry += self.name+"|"                  # Name
        fentry += self.gender+"|"                # Gender
        fentry += str(self.status)+"|"           # Status
        fentry += str(self.height)+"|"           # Height
        fentry += str(self.weight)+"|"           # Weight
        for e in self.element:                   # Element
            fentry += str(e)+":"
        fentry = fentry[:-1]
        fentry += "|"
        fentry += self.owner+"|"                 # Owner
        fentry += str(self.level)+"|"            # Level
        fentry += self.evol+"|"                  # Evolution Method
        fentry += str(self.exp)+"|"              # Exp points
        
        for i in range(len(self.stats)):
            fentry += str(self.stats[pk_stats[i].upper()])+":"     # Stats
        fentry = fentry[:-1]
        fentry += "|"
        for so in self.sorder:                   # Stat Order
            fentry += str(so)+":"
        fentry = fentry[:-1]
        fentry += "|"
        for m in self.moves:                     # Moves
            fentry += str(m.id_no)+":"
        fentry = fentry[:-1]
        fentry += "|"
        for i in range(len(self.skills)):        # Skills
            fentry += str(self.skills[pk_skills[i].lower()])+":"
        fentry = fentry[:-1]
        fentry += "|"
        fentry += str(self.ability.id_no)+"|"    # Ability
        fentry += str(self.nature.id_no)+"|"     # Nature
        fentry += str(self.h_power)+"|"          # Hidden Power Type
        fentry += str(self.n_def)+"|"            # Natural Defense Value
        for f in self.flavors:                   # Flavors
            fentry+= str(f)+":"
        fentry = fentry[:-1]
        fentry += "|"
        fentry += str(self.rarity)+"|"           # Rarity
        fentry += str(self.is_shiny)+"|"         # Shiny
        fentry += str(self.item.id_no)+"|"       # Item
        for le in self.learnset:
            fentry += le[0]+":"+le[1]+","
        fentry = fentry[:-1]

        if fname is "":
            fname = "pokemon/saved/"+self.species+"-"
            if self.owner == "N/A":
                fname += "unclaimed"
            else:
                fname += self.owner
            fname += ".txt"
        fname = fname.lower()
        fname = fname.replace(" ", "_")
        f = open(fname,'w')
        f.write(fentry)
        f.close

    def load(self, fname):
        with open("pokemon/saved/"+fname.lower()+".txt") as f:
            content = f.readlines()
        content = [x.strip() for x in content]
        content = content[0].split("|")
        self.id_no = int(content[0])
        self.species = content[1]
        self.name = content[2]
        self.gender = content[3]
        self.status = int(content[4])
        self.height = int(content[5])
        self.weight = float(content[6])
        self.element = [int(i) for i in content[7].split(":")]
        self.owner = content[8]
        self.level = int(content[9])
        self.evol = content[10]
        self.exp = int(content[11])
        l_stats = [int(i) for i in content[12].split(":")]
        for i in range(len(l_stats)):
            self.stats[pk_stats[i].upper()] = l_stats[i]
        self.sorder = [int(i) for i in content[13].split(":")]
        self.moves = [moves[int(i)] for i in content[14].split(":")]
        l_skills = [int(i) for i in content[15].split(":")]
        for i in range(len(l_skills)):
            self.skills[pk_skills[i].lower()] = l_skills[i]
        self.ability = abilities[int(content[16])]
        self.nature = natures[int(content[17])]
        self.h_power = int(content[18])
        self.n_def = content[19]
        self.flavors = [int(i) for i in content[20].split(":")]
        self.rarity = int(content[21])
        if(content[22] == "False"):
            self.is_shiny = False
        else:
            self.is_shiny = True
        self.item = items[int(content[23])]
        self.learnset = []

        if len(content) > 24:
            sl = content[24].split(",")
            for s in sl:
                self.learnset.append(s.split(":")[:])

    def getStatus(self):
        return cond[self.status]
    
    def setStatus(self, new_status):
        new_status = new_status.upper()
        for i in range(len(cond)):
            if cond[i] == new_status:
                self.status = i

    def catch(self, ball_type=0):
        r_mod = [1,1,1,2,2,2,3,3,3,4]
        stat = 0
        if self.status:
            stat = 2
        hp_mod = self.stats["HP"]
        hp_mod /= (self.stats["MAX HP"]*1.0)
        hp_mod *= 3.0
        hp_mod = int(round(hp_mod))
        hp_mod = 3 - hp_mod

        roll = self.rarity + 11 - hp_mod - stat - ball_type
        if self.rarity > 4:
            roll += 2
        return roll

    def calcXP(self, mod=WILD):
        return ((20 + mod) * self.level * self.rarity)

    def giveOrder(self,trainer, owner=True):
        frnd =  max(1,10 - (self.stats["FRIENDSHIP"] / 2.0))
        if not owner:
            frnd = 10
        return skillAttempt(trainer.getSkill("Training"),frnd)

    def setStat(self, s_name, s_mod=0, op=SET):
        if op:
            self.stats[s_name.upper()] += s_mod
        else:
            self.stats[s_name.upper()] = s_mod

    def getStat(self, s_name):
        return self.stats[s_name.upper()]

    def setSkill(self, s_name, s_mod=0, op=SET):
        s_name = s_name.lower().replace(" ","")
        if op:
            self.skills[s_name] += s_mod
        else:
            self.skills[s_name] = s_mod

    def getSkill(self, s_name):
        s_name = s_name.lower().replace(" ","")
        return self.skills[s_name]

    def heal(self):
        self.stats["HP"] = self.stats["MAX HP"]
        self.stats["ENERGY"] = self.stats["MAX ENERGY"]
        for m in self.moves:
            m.pp = m.full_pp
            
            

"""
================================================================================
CLASS HELPER FUNCTIONS
================================================================================
"""
def getGender(genders):
    rand.seed(time.gmtime())
    genders = genders.split(":")
    gen = rand.randint(0,len(genders)-1)
    return genders[gen]

def howMuchXP(lvl):
    sum = 0;
    for i in range(lvl):
        sum += int(round(exp(lvl/28.518)*300))
    return sum

def generatePVector(stars=[5,5,5,5,5,5]):
    t = float(sum(stars))
    for i in range(len(stars)):
        stars[i] /= t
    return stars

def balanceStats(probs = [0.166667, 0.166667, 0.166667, 0.166667, 0.166667, 0.166667]):
    s_stats = [0, 0, 0, 0, 0, 0]
    for i in range(1000):
        s_stats = arrayAdd(s_stats, assignStats(probs), 6)
    s_stats = arrayDiv(s_stats, 1000.0, 6)
    return s_stats

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

def isShiny(num=1):
    for i in range(num):
        chance = rand.randint(1, 8192)
        if chance is 4096:
            return True
        else:
            return False

def skillAttempt(p_skill,skill_l=5):
    rounding = Rounding()
    mod = rounding.BankersRounding(-5*sin((3*pi/2) + p_skill/7.0)+5)
    return int(skill_l + mod)
