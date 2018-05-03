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
LOCAL HTML FUNCTIONS
================================================================================
"""
h_tab = "    "
t_ind = 2

def hprint(f,ln=""):
    global t_ind
    f.write(t_ind*h_tab+ln+"\n")
    
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

    def pprint(self):
        title = "* "+padString(self.name,38,LEFT)
        title += padString("#"+str(self.id_no),38,RIGHT)+" *"
        desc = self.description
        print "*"*80
        print title
        print "*"*80
        printWrapped("Description: "+desc, 80,
                len("Description: "), "| ", " |")
        print "-"*80
        
    def export(self, f):
        title = "* "+padString(self.name,38,LEFT)
        title += padString("#"+str(self.id_no),38,RIGHT)+" *"
        desc = self.description
        f.write("*"*80+"\n")
        f.write(title+"\n")
        f.write("*"*80+"\n")
        writeWrapped(f,"Description: "+desc, 80,
                len("Description: "), "| ", " |")
        f.write("-"*80+"\n")

    def html(self, f):
        global t_ind
        hstr = "<div class=\"section-head\" "
        hstr+= "style=\"background: #FFCCDD;\" "
        hstr+= "onclick=\"hide(\'abil\');\">"
        hprint(f,hstr)
        t_ind+=1
        hstr = "<h3 class=\"nopad\">"
        hstr+= self.name+"</h3>"
        hprint(f,hstr)
        t_ind-=1
        hprint(f,"</div>")
        hstr = "<div class=\"section-body\" "
        hstr+="style=\"display: none;\" "
        hstr+="id=\"abil\">"
        hprint(f,hstr)
        t_ind+=1
        hprint(f,"<div class=\"sub-section\">")
        t_ind+=1
        hprint(f,self.description)
        t_ind-=1
        hprint(f,"</div>")
        t_ind-=1
        hprint(f,"</div>")
