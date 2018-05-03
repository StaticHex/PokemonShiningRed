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
MOVE CLASS
================================================================================
"""
class Move:
    id_no = 0
    name = ""
    element = 0
    category = ""
    pp = 0
    full_pp = 0
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
            self.full_pp = int(entry[5])
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

    def pprint(self):
        title = "* "+padString(self.name,38,LEFT)
        title += padString("#"+str(self.id_no), 38, RIGHT)+" *"

        classifier = "| "+padString("Element: "+pk_types[self.element],
                                    38, LEFT);
        classifier += padString("Category: "+self.category,38, LEFT)+" |"

        pp_info = "| "+padString("PP: "+str(self.pp),25,LEFT)
        pp_info += padString("Max PP: "+str(self.max_pp),25,LEFT)
        pp_info += padString("PP Rate: "+str(self.pp_rate),26,LEFT)+" |"

        move_info = "| "+padString("Power: "+self.power, 38, LEFT)
        move_info += padString("Accuracy: "+self.accuracy, 38, LEFT)+" |"

        cont_info = "| "+padString("Category: "+self.c_category, 25, LEFT)
        cont_info += padString("Appeal Points: "+str(self.c_points), 25, LEFT)
        cont_info += padString("Jam Points: "+str(self.c_jam),26,LEFT)+" |"

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
        desc = self.description
        printWrapped("Description: "+desc, 80,
                     len("Description: "), "| ", " |")
        print "="*80
        print "| "+padString("Contest Info", 76, CENTER)+" |"
        print "="*80
        print cont_info
        print "-"*80
        desc = self.c_description
        printWrapped("Description: "+desc, 80,
                len("Description: "), "| ", " |")
        print "="*80

    def export(self, f):
        title = "* "+padString(self.name,38,LEFT)
        title += padString("#"+str(self.id_no), 38, RIGHT)+" *"

        classifier = "| "+padString("Element: "+pk_types[self.element],
                                    38, LEFT);
        classifier += padString("Category: "+self.category,38, LEFT)+" |"

        pp_info = "| "+padString("PP: "+str(self.pp),25,LEFT)
        pp_info += padString("Max PP: "+str(self.max_pp),25,LEFT)
        pp_info += padString("PP Rate: "+str(self.pp_rate),26,LEFT)+" |"

        move_info = "| "+padString("Power: "+self.power, 38, LEFT)
        move_info += padString("Accuracy: "+self.accuracy, 38, LEFT)+" |"

        cont_info = "| "+padString("Category: "+self.c_category, 25, LEFT)
        cont_info += padString("Appeal Points: "+str(self.c_points), 25, LEFT)
        cont_info += padString("Jam Points: "+str(self.c_jam),26,LEFT)+" |"

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
        desc = self.description
        writeWrapped(f,"Description: "+desc, 80,
                     len("Description: "), "| ", " |")
        f.write("="*80+"\n")
        f.write("| "+padString("Contest Info", 76, CENTER)+" |"+"\n")
        f.write("="*80+"\n")
        f.write(cont_info+"\n")
        f.write("-"*80+"\n")
        desc = self.c_description
        writeWrapped(f,"Description: "+desc, 80,
                len("Description: "), "| ", " |")
        f.write("="*80+"\n")

    def html(self, f, mov=0):
        global t_ind
        if mov:
            mov = str(mov)
            hstr = "<div class=\"moveset-middle\" "
            hstr+= "onclick=\"hide(\'move"+mov+"\');\">"
        else:
            mov = str(mov)
            hstr = "<div class=\"moveset-top\" "
            hstr+= "onclick=\"hide(\'move"+mov+"\');\">"
        hprint(f,hstr)
        t_ind+=1
        hprint(f,"<table style=\"width:100%;\">")
        t_ind+=1
        hprint(f,"<tr>")
        t_ind+=1
        hprint(f,"<td style=\"text-align:left;\">")
        t_ind+=1
        hprint(f,"<h3 class=\"nopad\">"+self.name+"</h3>")
        t_ind-=1
        hprint(f,"</td>")
        hprint(f,"<td style=\"text-align:right;\">")
        t_ind+=1
        hstr = "<h3 class=\"nopad\">"
        hstr+= str(self.pp)+" PP</h3>"
        hprint(f,hstr)
        t_ind-=1
        hprint(f,"</td>")
        t_ind-=1
        hprint(f,"</tr>")
        t_ind-=1
        hprint(f,"</table>")
        t_ind-=1
        hprint(f,"</div>")
        hstr = "<div class=\"moveset-body\" "
        hstr+= "style=\"display:none;\" "
        hstr+= "id=\"move"+mov+"\">"
        hprint(f, hstr)
        t_ind+=1
        hprint(f, "<div class=\"sub-header\">")
        t_ind+=1
        hprint(f, "<h4 class=\"nopad\">Battle Info</h4>")
        t_ind-=1
        hprint(f,"</div>")
        hstr = "<div class=\"sub-section\" "
        hstr+= "style=\"border-bottom: 1px solid black;\">"
        hprint(f, hstr)
        t_ind+=1
        hstr = "<strong>Max PP:</strong>"
        hstr+= str(self.max_pp)+"&nbsp;&nbsp;&nbsp;&nbsp;"
        hprint(f, hstr)
        hstr = "<strong>PP Rate:</strong> "
        hstr+= str(self.pp_rate)+"&nbsp;&nbsp;&nbsp;&nbsp;"
        hprint(f, hstr)
        hstr = "<strong>Power:</strong> "
        hstr+= str(self.power)+"&nbsp;&nbsp;&nbsp;&nbsp;"
        hprint(f, hstr)
        hstr = "<strong>Accuracy:</strong> "
        hstr+= str(self.accuracy)+"&nbsp;&nbsp;&nbsp;&nbsp;"
        hprint(f, hstr)
        t_ind-=1
        hprint(f,"</div>")
        hstr = "<div class=\"sub-section\" "
        hstr+= "style=\"border-bottom: 1px solid black;\">"
        hprint(f, hstr)
        t_ind+=1
        hstr = "<strong>Type:</strong> "
        hstr+= pk_types[self.element]+"&nbsp;&nbsp;&nbsp;&nbsp;"
        hprint(f, hstr)
        hstr = "<strong>Category:</strong> "
        hstr+= self.category+"&nbsp;&nbsp;&nbsp;&nbsp;"
        hprint(f, hstr)
        t_ind-=1
        hprint(f,"</div>")
        hprint(f,"<div class=\"sub-section\">")
        t_ind+=1
        hprint(f,self.description)
        t_ind-=1
        hprint(f,"</div>")
        hprint(f,"<div class = \"sub-header\">")
        t_ind+=1
        hprint(f,"<h4 class=\"nopad\">Contest Info</h4>")
        t_ind-=1
        hprint(f,"</div>")
        hstr = "<div class=\"sub-section\" "
        hstr+= "style=\"border-bottom: 1px solid black;\">"
        hprint(f, hstr)
        t_ind+=1
        hstr = "<strong>Category:</strong> "
        hstr+= self.c_category+"&nbsp;&nbsp;&nbsp;&nbsp;"
        hprint(f, hstr)
        hstr = "<strong>Appeal Points:</strong> "
        hstr+= str(self.c_points)+"&nbsp;&nbsp;&nbsp;&nbsp;"
        hprint(f, hstr)
        hstr = "<strong>Jam Points:</strong> "
        hstr+= str(self.c_jam)+"&nbsp;&nbsp;&nbsp;&nbsp;"
        hprint(f, hstr)
        t_ind-=1
        hprint(f,"</div>")
        hprint(f,"<div class=\"sub-section\">")
        t_ind+=1
        hprint(f,self.c_description)
        t_ind-=1
        hprint(f,"</div>")
        t_ind-=1
        hprint(f,"</div>")
        
        
        
