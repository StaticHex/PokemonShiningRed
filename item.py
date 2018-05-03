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

    def pprint(self):
        title = "* "+padString(self.name,38,LEFT)+padString("#"
                    +str(self.id_no),38,RIGHT)+" *"
        price = padString("Buy Price: "+self.cost, 30, LEFT)
        price += padString("Sell Price: "+self.sell,46,LEFT)
        
        fling = padString("Fling Damage: "+str(self.fling_dmg),30,LEFT)
        fling += padString("Fling Effect: "+self.fling_effect,46,LEFT)
        
        natural_gift = padString("Natural Gift Damage: "+str(self.nature_dmg),30,LEFT)
        natural_gift += padString("Natural Gift Type: "+self.nature_type,46,LEFT)

        
        print "*"*80
        print title
        print "*"*80
        print "| "+price+" |"
        print "-"*80
        print "| "+fling+" |"
        print "-"*80
        print "| "+natural_gift+" |"
        print "-"*80
        desc = self.description
        printWrapped("Description: "+desc, 80,
                     len("Description: "), "| ", " |")
        print "-"*80

    def export(self, f):
        title = "* "+padString(self.name,38,LEFT)+padString("#"
                    +str(self.id_no),38,RIGHT)+" *"
        price = padString("Buy Price: "+self.cost, 30, LEFT)
        price += padString("Sell Price: "+self.sell,46,LEFT)
        
        fling = padString("Fling Damage: "+str(self.fling_dmg),30,LEFT)
        fling += padString("Fling Effect: "+self.fling_effect,46,LEFT)
        
        natural_gift = padString("Natural Gift Damage: "+str(self.nature_dmg),30,LEFT)
        natural_gift += padString("Natural Gift Type: "+self.nature_type,46,LEFT)

        
        f.write("*"*80+"\n")
        f.write(title+"\n")
        f.write("*"*80+"\n")
        f.write("| "+price+" |"+"\n")
        f.write("-"*80+"\n")
        f.write("| "+fling+" |"+"\n")
        f.write("-"*80+"\n")
        f.write("| "+natural_gift+" |"+"\n")
        f.write("-"*80+"\n")
        desc = self.description
        writeWrapped(f,"Description: "+desc, 80,
                     len("Description: "), "| ", " |")
        f.write("-"*80+"\n")

    def html(self, f):
        global t_ind
        if self.id_no:
            hstr = "<div class=\"section-head\" "
            hstr+= "style=\"background: #FFFFCC;\" "
            hstr+= "onclick=\"hide('item');\">"
            hprint(f,hstr)
            t_ind+=1
            hstr = "<h3 class=\"nopad\">"
            hstr+= self.name+"</h3>"
            hprint(f,hstr)
            t_ind-=1
            hprint(f,"</div>")
            hstr = "<div class=\"section-body\" "
            hstr+= "style=\"display: none;\" id=\"item\">"
            hprint(f,hstr)
            t_ind+=1
            hstr = "<div class=\"sub-section\" "
            hstr+= "style=\"border-bottom:1px solid black;\">"
            hprint(f,hstr)
            t_ind+=1
            hstr = "<strong>Buy Price:</strong> "
            hstr+= str(self.cost)+"P &nbsp;&nbsp;&nbsp;&nbsp;"
            hprint(f,hstr)
            hstr = "<strong>Sell Price:</strong> "
            hstr+= str(self.sell)+"P &nbsp;&nbsp;&nbsp;&nbsp;"
            hprint(f,hstr)
            t_ind-=1
            hprint(f,"</div>")
            hstr = "<div class=\"sub-section\" "
            hstr+= "style=\"border-bottom:1px solid black;\">"
            hprint(f,hstr)
            t_ind+=1
            hstr = "<strong>Fling Damage:</strong> "
            hstr+= str(self.fling_dmg)+"&nbsp;&nbsp;&nbsp;&nbsp;"
            hprint(f,hstr)
            hstr = "<strong>Fling Effect:</strong> "
            hstr+= self.fling_effect+"&nbsp;&nbsp;&nbsp;&nbsp;"
            hprint(f, hstr)
            t_ind-=1
            hprint(f,"</div>")
            hstr = "<div class=\"sub-section\" "
            hstr+= "style=\"border-bottom:1px solid black;\">"
            hprint(f, hstr)
            t_ind+=1
            hstr = "<strong>Natural Gift Damage:</strong> "
            hstr+= str(self.nature_dmg)+"&nbsp;&nbsp;&nbsp;&nbsp;"
            hprint(f,hstr)
            hstr = "<strong>Natural Gift Effect:</strong> "
            hstr+= self.nature_type+"&nbsp;&nbsp;&nbsp;&nbsp;"
            hprint(f,hstr)
            t_ind-=1
            hprint(f,"</div>")
            hprint(f,"<div class=\"sub-section\">")
            t_ind+=1
            hprint(f,self.description)
            t_ind-=1
            hprint(f,"</div>")
            t_ind-=1
            hprint(f,"</div>")
        else:
            hstr = "<div class=\"section-head\" "
            hstr+= "style=\"background: #FFFFCC;\" "
            hstr+= "onclick=\"hide('item');\">"
            hprint(f,hstr)
            t_ind+=1
            hstr = "<h3 class=\"nopad\">"
            hstr+= "None</h3>"
            hprint(f,hstr)
            t_ind-=1
            hprint(f,"</div>")
