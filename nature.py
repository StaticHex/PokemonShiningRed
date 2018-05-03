from asciiml import *
"""
================================================================================
HEADER: HAVE TO HAVE THIS HERE TO AVOID CIRCULAR DEPENDENCIES
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

"""
================================================================================
LOCAL HTML IMPORTS
================================================================================
"""
h_tab = "    "
t_ind = 2

def hprint(f,ln=""):
    global t_ind
    f.write(t_ind*h_tab+ln+"\n")
    
""" 
================================================================================
NATURE CLASS
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

    def pprint(self):
        title = "* "+padString(self.name,38,LEFT)
        title += padString("#"+str(self.id_no),38,RIGHT)+" *"

        stat_string = ""
        if self.stat_mods[0] != "-":
            for mod in self.stat_mods:
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
        if self.skill_mods[0] != "-":
            for mod in self.skill_mods:
                tup = mod.split(":")
                skill_string += pk_skills[int(tup[0])]+": "
                if int(tup[1]) > 0:
                    skill_string += "+"
                skill_string += tup[1]+"     "
        else:
            skill_string = "-"

        desc = self.description
        print "*"*80
        print title
        print "*"*80
        printWrapped("Stat Mods: "+stat_string, 80, len("Stat Mods: "),"| ", " |")
        print "-"*80
        printWrapped("Skill Mods: "+skill_string, 80, len("Skill Mods: "), "| ", " |")
        print "-"*80
        printWrapped("Description: "+desc, 80, len("Description: "), "| ", " |")
        print "-"*80
        
    def export(self,f):
        title = "* "+padString(self.name,38,LEFT)
        title += padString("#"+str(self.id_no),38,RIGHT)+" *"

        stat_string = ""
        if self.stat_mods[0] != "-":
            for mod in self.stat_mods:
                tup = mod.split(":")
                if(int(tup[0]) < 6):
                    stat_string += pk_stats[int(tup[0])]+": "
                else:
                    stat_string += "FRND: "
                if int(tup[1]) > 0:
                    stat_string += "+"
                stat_string += tup[1]+"     "
        else:
            stat_string = "-"

        skill_string = ""
        if self.skill_mods[0] != "-":
            for mod in self.skill_mods:
                tup = mod.split(":")
                skill_string += pk_skills[int(tup[0])]+": "
                if int(tup[1]) > 0:
                    skill_string += "+"
                skill_string += tup[1]+"     "
        else:
            skill_string = "-"

        desc = self.description
        f.write("*"*80+"\n")
        f.write(title+"\n")
        f.write("*"*80+"\n")
        writeWrapped(f,"Stat Mods: "+stat_string, 80, len("Stat Mods: "),"| ", " |")
        f.write("-"*80+"\n")
        writeWrapped(f,"Skill Mods: "+skill_string, 80, len("Skill Mods: "), "| ", " |")
        f.write("-"*80+"\n")
        writeWrapped(f,"Description: "+desc, 80, len("Description: "), "| ", " |")
        f.write("-"*80);

    def html(self, f):
        global t_ind
        hstr = "<div class=\"section-head\" "
        hstr+= "style=\"background: #CCFFDD;\" "
        hstr+= "onclick=\"hide(\'nat\');\">"
        hprint(f, hstr)
        t_ind+=1
        hstr ="<h3 class=\"nopad\">"
        hstr+= self.name+"</h3>"
        hprint(f,hstr)
        t_ind-=1
        hprint(f,"</div>")
        hstr = "<div class=\"section-body\" "
        hstr+= "style=\"display: none;\" id=\"nat\">"
        hprint(f,hstr)
        t_ind+=1
        if not self.stat_mods[0] == "-":
            hprint(f,"<div class=\"sub-header\">")
            t_ind+=1
            hprint(f,"<h4 class=\"nopad\">Stat Mods</h4>")
            t_ind-=1
            hprint(f,"</div>")
            hprint(f,"<div class=\"sub-section\">")
            t_ind+=1
            hprint(f,"<table style=\"width: 100%;\">")
            t_ind+=1
            hprint(f,"<tr>")
            counter=0
            for st in self.stat_mods:
                st = [int(i) for i in st.split(":")]
                hstr = "<td><strong>"+pk_stats[st[0]]+":</strong> "
                hstr+= str(st[1])
                hstr+= "&nbsp;&nbsp;&nbsp;&nbsp;</td>"
                hprint(f,hstr)
                counter+=1
                if counter == 3:
                    t_ind-=1
                    hprint(f,"</tr>")
                    hprint(f,"<tr>")
                    t_ind+=1
                    counter=0
            while counter < 3:
                hprint(f,"<td></td>")
                counter+=1
            t_ind-=1
            hprint(f,"</tr>")
            t_ind-=1
            hprint(f,"</table>")
            t_ind-=1
            hprint(f,"</div>")
        if not self.skill_mods[0] == "-":
            hprint(f,"<div class=\"sub-header\">")
            t_ind+=1
            hprint(f,"<h4 class=\"nopad\">Skill Mods</h4>")
            t_ind-=1
            hprint(f,"</div>")
            hstr = "<div class=\"sub-section\">"
            hprint(f,hstr)
            t_ind+=1
            hprint(f, "<table style=\"width: 100%;\">")
            t_ind+=1
            hprint(f,"<tr>")
            t_ind+=1
            counter=0
            for sk in self.skill_mods:
                sk = [int(i) for i in sk.split(":")]
                hstr = "<td><strong>"+pk_skills[sk[0]]+":</strong> "
                hstr+= str(sk[1])
                hstr+= "&nbsp;&nbsp;&nbsp;&nbsp;</td>"
                hprint(f,hstr)
                counter+=1
                if counter == 3:
                    t_ind-=1
                    hprint(f,"</tr>")
                    hprint(f,"<tr>")
                    t_ind+=1
                    counter=0
            while counter < 3:
                hprint(f,"<td></td>")
                counter+=1
            t_ind-=1
            hprint(f,"</tr>")
            t_ind-=1
            hprint(f,"</table>")
            t_ind-=1
            hprint(f,"</div>")
        if not self.skill_mods[0] == "-" or not self.stat_mods[0] == "-":
            hstr = "<div class=\"sub-section\" "
            hstr+= "style=\"border-top: 1px solid black;\">"
            hprint(f,hstr)
        else:
            hprint(f,"<div class=\"sub-section\">")
        t_ind+=1
        hprint(f,self.description)
        t_ind-=1
        hprint(f,"</div>")
        t_ind-=1
        hprint(f,"</div>")
