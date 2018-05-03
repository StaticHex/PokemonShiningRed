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

PERK = 0
DEFECT = 1

h_tab = "    "
t_ind = 2

def hprint(f,ln=""):
    f.write(t_ind*h_tab+ln+"\n")
    
"""
================================================================================
MODIFIER CLASS
================================================================================
"""
class Modifier:
    def __init__(self,mstring):
        self.name = "N/A"
        self.m_type = "N/A"
        self.skill_mods = []
        self.stat_mods = []
        self.cash_mods = 0
        self.effects = []
        self.description = "N/A"
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
        if not mstring[5] == "-":
            self.effects = mstring[5].split(":")
        self.description = mstring[6]

    def pprint(self):
        p_stats = {"HP":"HP","ATK":"ATK","DEF":"DEF","SP. ATK":"SP. ATK",
                   "SP. DEF":"SP. DEF","SPD":"SPD","CHARISMA":"Charisma"}
        header = "="*80+"\n"+"*"*80 + "\n"
        header += "* "+padString(self.name,76,LEFT)+" *\n"
        header += "*"*80 + "\n" + "="*80 + "\n" + "-"*80 + "\n"
        mod_type = "| "+padString("Type: "+self.m_type,76,LEFT)+" |\n"+("-")*80
        st_mods = ""
        sk_mods = ""
        csh = ""
        for st in self.stat_mods:
            st_mods += st[0]+": "
            if(st[1] > 0):
                st_mods += "+"
            st_mods += str(st[1])+"     "

        for sk in self.skill_mods:
            sk_mods += sk[0]+": "
            if(sk[1] > 0):
                sk_mods += "+"
            sk_mods += str(sk[1])+"     "

        if self.cash_mods:
            if self.cash_mods > 0:
                csh += "+"
            csh += str(self.cash_mods)+"P"
            csh = "| "+padString(csh,76,LEFT)+" |"
            
        print header+mod_type
        printWrapped(self.description,80,0,"| "," |")
        print "-"*80
        if len(st_mods):
            print "="*80
            print "| "+padString("Stat Mods",76,CENTER)+" |"
            print "="*80
            printWrapped(st_mods,80,0,"| "," |")
            print "-"*80
        if len(sk_mods):
            print "="*80
            print "| "+padString("Skill Mods",76,CENTER)+" |"
            print "="*80
            printWrapped(sk_mods,80,0,"| "," |")
            print "-"*80
        if len(csh):
            print "="*80
            print "| "+padString("Cash Mods",76,CENTER)+" |"
            print "="*80
            print csh
            print "-"*80
        if len(self.effects):
            print "="*80
            print "| "+padString("Effects",76,CENTER)+" |"
            print "="*80
            for ef in self.effects:
                printWrapped("* "+ef,80,len("* "),"| "," |")
            print "-"*80
            
    def export(self, f):
        p_stats = {"HP":"HP","ATK":"ATK","DEF":"DEF","SP. ATK":"SP. ATK",
                   "SP. DEF":"SP. DEF","SPD":"SPD","CHARISMA":"Charisma"}
        header = "="*80+"\n"+"*"*80 + "\n"
        header += "* "+padString(self.name,76,LEFT)+" *\n"
        header += "*"*80 + "\n" + "="*80 + "\n" + "-"*80 + "\n"
        mod_type = "| "+padString("Type: "+self.m_type,76,LEFT)+" |\n"+("-")*80
        st_mods = ""
        sk_mods = ""
        csh = ""
        for st in self.stat_mods:
            st_mods += st[0]+": "
            if(st[1] > 0):
                st_mods += "+"
            st_mods += str(st[1])+"     "

        for sk in self.skill_mods:
            sk_mods += sk[0]+": "
            if(sk[1] > 0):
                sk_mods += "+"
            sk_mods += str(sk[1])+"     "

        if self.cash_mods:
            if self.cash_mods > 0:
                csh += "+"
            csh += str(self.cash_mods)+"P"
            csh = "| "+padString(csh,76,LEFT)+" |"
            
        f.write(header+mod_type+"\n")
        writeWrapped(f,self.description,80,0,"| "," |")
        f.write("-"*80+"\n")
        if len(st_mods):
            f.write("="*80+"\n")
            f.write("| "+padString("Stat Mods",76,CENTER)+" |"+"\n")
            f.write("="*80+"\n")
            writeWrapped(f,st_mods,80,0,"| "," |")
            f.write("-"*80+"\n")
        if len(sk_mods):
            f.write("="*80+"\n")
            f.write("| "+padString("Skill Mods",76,CENTER)+" |"+"\n")
            f.write("="*80+"\n")
            writeWrapped(f,sk_mods,80,0,"| "," |")
            f.write("-"*80+"\n")
        if len(csh):
            f.write("="*80+"\n")
            f.write("| "+padString("Skill Mods",76,CENTER)+" |"+"\n")
            f.write("="*80+"\n")
            f.write(csh+"\n")
            f.write("-"*80+"\n")
        if len(self.effects):
            f.write("="*80+"\n")
            f.write("| "+padString("Effects",76,CENTER)+" |"+"\n")
            f.write("="*80+"\n")
            for ef in self.effects:
                writeWrapped(f,"* "+ef,80,len("* "),"| "," |")
            f.write("-"*80+"\n")

    def html(self, f, nextmod=0, ty=0):
        #col = "#FFCCDD"
        col = "#CCFFDD"
        if ty:
            #col = "#CCFFDD"
            col = "#FFCCDD"
        global t_ind
        hstr = "<div class=\"section-head\" "
        hstr+= "onclick=\"hide(\'t_mod"+str(nextmod)+"\')\">"
        hprint(f,hstr)
        t_ind+=1
        hprint(f,"<div class=\"sub-txt\" style=\"background: "+col+"\">")
        t_ind+=1
        hprint(f,"<h3 class=\"nopad\">"+self.name+"</h3>")
        t_ind-=1
        hprint(f,"</div>")
        t_ind-=1
        hprint(f,"</div>")
        hstr = "<div class=\"section-body\" "
        hstr+= "style=\"display:none;\" id=\"t_mod"+str(nextmod)+"\">"
        hprint(f,hstr)
        t_ind+=1
        hstr = "<div class=\"sub-section\" "
        hstr+= "style=\"border-bottom: 1px solid black;\">"
        hprint(f,hstr)
        t_ind+=1
        hstr = "<strong>Type:</strong> "
        hstr+= self.m_type
        hprint(f,hstr)
        t_ind-=1
        hprint(f,"</div>")
        hprint(f,"<div class=\"sub-section\">")
        t_ind+=1
        hprint(f,self.description)
        t_ind-=1
        hprint(f, "</div>")
        if self.cash_mods:
            hprint(f, "<div class=\"sub-header\">")
            t_ind+=1
            hprint(f, "<h3 class=\"nopad\">Cash Mods</h3>")
            t_ind-=1
            hprint(f, "</div>")
            hprint(f, "<div class=\"sub-section\">")
            t_ind+=1
            cm_str = ""
            if self.cash_mods > 0:
                cm_str += "+"
            cm_str+= str(self.cash_mods)+"P"
            hprint(f, cm_str)
            t_ind-=1
            hprint(f,"</div>")
        if len(self.stat_mods):
            hprint(f, "<div class=\"sub-header\">")
            t_ind+=1
            hprint(f, "<h3 class=\"nopad\">Stat Mods</h3>")
            t_ind-=1
            hprint(f, "</div>")
            hprint(f, "<div class=\"sub-section\">")
            t_ind+=1
            hprint(f, "<table>")
            t_ind+=1
            hprint(f, "<tr>")
            t_ind+=1
            counter = 0
            for st in self.stat_mods:
                hstr = "<td><strong>"+st[0]+":</strong> "
                if st[1] > 0:
                    hstr += "+"
                hstr += str(st[1])
                hstr += "&nbsp;&nbsp;&nbsp;&nbsp;</td>"
                hprint(f,hstr)
                counter += 1
                if counter and not (counter % 3):
                    t_ind-=1
                    hprint(f,"</tr>")
                    hprint(f,"<tr>")
                    t_ind+=1
            while counter < 3:
                hprint(f,"<td></td>")
                counter += 1
            t_ind-=1
            hprint(f,"</tr>")
            t_ind-=1
            hprint(f,"</table>")
            t_ind-=1
            hprint(f,"</div>")
        if len(self.skill_mods):
            hprint(f, "<div class=\"sub-header\">")
            t_ind+=1
            hprint(f, "<h3 class=\"nopad\">Skill Mods</h3>")
            t_ind-=1
            hprint(f, "</div>")
            hprint(f, "<div class=\"sub-section\">")
            t_ind+=1
            hprint(f, "<table>")
            t_ind+=1
            hprint(f, "<tr>")
            t_ind+=1
            counter = 0
            for sk in self.skill_mods:
                hstr = "<td><strong>"+sk[0]+":</strong> "
                if sk[1] > 0:
                    hstr += "+"
                hstr += str(sk[1])
                hstr += "&nbsp;&nbsp;&nbsp;&nbsp;</td>"
                hprint(f,hstr)
                counter += 1
                if counter and not (counter % 3):
                    t_ind-=1
                    hprint(f,"</tr>")
                    hprint(f,"<tr>")
                    t_ind+=1
            while counter < 3:
                hprint(f,"<td></td>")
                counter += 1
            t_ind-=1
            hprint(f,"</tr>")
            t_ind-=1
            hprint(f,"</table>")
            t_ind-=1
            hprint(f,"</div>")
        if len(self.effects):
            hprint(f, "<div class=\"sub-header\">")
            t_ind+=1
            hprint(f, "<h3 class=\"nopad\">Effects</h3>")
            t_ind-=1
            hprint(f, "</div>")
            hprint(f, "<div class=\"sub-section\">")
            t_ind+=1
            hprint(f, "<ul>")
            t_ind+=1
            for ef in self.effects:
                hprint(f,"<li>"+ef+"</li>")
            t_ind-=1
            hprint(f,"</ul>")
            t_ind-=1
            hprint(f,"</div>")
        t_ind-=1
        hprint(f,"</div>")
        nextmod += 1
            
