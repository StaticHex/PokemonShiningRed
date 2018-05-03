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

h_tab = "    "
t_ind = 2

def hprint(f,ln=""):
    f.write(t_ind*h_tab+ln+"\n")
    
"""
================================================================================
JOB CLASS
================================================================================
"""
class Job:
    def __init__(self,mstring=""):
        self.name = "N/A"
        self.type = "N/A"
        self.description = "N/A"
        self.stat_mods = []
        self.skill_mods = []
        self.cash = 0
        self.benefits = []
        self.penalties = []

        if len(mstring):
            mstring = mstring.split("|")
            self.name = mstring[0]
            self.type = mstring[1]
            self.description = mstring[2]
            if not mstring[3] == "-":
                st_mod = mstring[3].split(",")
                for st in st_mod:
                    self.stat_mods.append(st.split(":")[:])
            if not mstring[4] == "-":
                sk_mod = mstring[4].split(",")
                for sk in sk_mod:
                    self.skill_mods.append(sk.split(":")[:])
            self.cash = int(mstring[5])
            if not mstring[6] == "-":
                self.benefits = mstring[6].split(":")[:]
            if not mstring[7] == "-":
                self.penalties = mstring[7].split(":")[:]

    def pprint(self):
        header = "="*80+"\n"+"*"*80 + "\n"
        header += "* "+padString(self.name,76,LEFT)+" *\n"
        header += "*"*80 + "\n" + "="*80 + "\n" + "-"*80 + "\n"
        job_type = "| "+padString("Type: "+self.type,76,LEFT)+" |\n"+("-")*80
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

        if self.cash:
            csh += str(self.cash)+"P"
            csh = "| "+padString(csh,76,LEFT)+" |"
            
        print header+job_type
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
            print "| "+padString("Starting Cash",76,CENTER)+" |"
            print "="*80
            print csh
            print "-"*80
        if len(self.benefits):
            print "="*80
            print "| "+padString("Benefits",76,CENTER)+" |"
            print "="*80
            for b in self.benefits:
                printWrapped("* "+b,80,len("* "),"| "," |")
            print "-"*80
        if len(self.penalties):
            print "="*80
            print "| "+padString("Penalties",76,CENTER)+" |"
            print "="*80
            for p in self.penalties:
                printWrapped("* "+p,80,len("* "),"| "," |")
            print "-"*80

    def export(self,f):
        header = "="*80+"\n"+"*"*80 + "\n"
        header += "* "+padString(self.name,76,LEFT)+" *\n"
        header += "*"*80 + "\n" + "="*80 + "\n" + "-"*80 + "\n"
        job_type = "| "+padString("Type: "+self.type,76,LEFT)+" |\n"+("-")*80
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

        if self.cash:
            csh += str(self.cash)+"P"
            csh = "| "+padString(csh,76,LEFT)+" |"
            
        f.write(header+job_type+"\n")
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
            f.write("| "+padString("Starting Cash",76,CENTER)+" |"+"\n")
            f.write("="*80+"\n")
            f.write(csh+"\n")
            f.write("-"*80+"\n")
        if len(self.benefits):
            f.write("="*80+"\n")
            f.write("| "+padString("Benefits",76,CENTER)+" |"+"\n")
            f.write("="*80+"\n")
            for b in self.benefits:
                writeWrapped(f,"* "+b,80,len("* "),"| "," |")
            f.write("-"*80+"\n")
        if len(self.penalties):
            f.write("="*80+"\n")
            f.write("| "+padString("Penalties",76,CENTER)+" |"+"\n")
            f.write("="*80+"\n")
            for p in self.penalties:
                writeWrapped(f,"* "+p,80,len("* "),"| "," |")
            f.write("-"*80+"\n")

    def html(self, f):
        global t_ind
        hstr = "<div class=\"section-head\" "
        hstr += "style=\"background:#CCCCFF;\" "
        hstr += "onclick=\"hide(\'t_job\')\">"
        hprint(f, hstr)
        t_ind+=1
        hprint(f, "<div class=\"sub-txt\">")
        t_ind+=1
        hprint(f, "<h3 class=\"nopad\">"+self.name+"</h3>")
        t_ind-=1
        hprint(f, "</div>")
        t_ind-=1
        hprint(f, "</div>")
        hstr = "<div class=\"section-body\" style=\"display:none;\" "
        hstr+= "id=\"t_job\">"
        hprint(f, hstr)
        t_ind+=1
        hstr = "<div class=\"sub-section\" "
        hstr += "style=\"border-bottom: 1px solid black;\">"
        hprint(f, hstr)
        t_ind+=1
        hprint(f, "<strong>Trainer Type:</strong> "+self.type)
        t_ind-=1
        hprint(f, "</div>")
        hprint(f, "<div class=\"sub-section\">")
        t_ind+=1
        hprint(f,self.description)
        t_ind-=1
        hprint(f, "</div>")
        hprint(f, "<div class=\"sub-header\">")
        t_ind+=1
        hprint(f, "<h3 class=\"nopad\">Starting Cash</h3>")
        t_ind-=1
        hprint(f, "</div>")
        hprint(f, "<div class=\"sub-section\">")
        t_ind+=1
        hprint(f,str(self.cash)+"P")
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
        if len(self.benefits):
            hprint(f, "<div class=\"sub-header\">")
            t_ind+=1
            hprint(f, "<h3 class=\"nopad\">Benefits</h3>")
            t_ind-=1
            hprint(f, "</div>")
            hprint(f, "<div class=\"sub-section\">")
            t_ind+=1
            hprint(f, "<ul>")
            t_ind+=1
            for be in self.benefits:
                hprint(f,"<li>"+be+"</li>")
            t_ind-=1
            hprint(f,"</ul>")
            t_ind-=1
            hprint(f,"</div>")
        if len(self.penalties):
            hprint(f, "<div class=\"sub-header\">")
            t_ind+=1
            hprint(f, "<h3 class=\"nopad\">Penalties</h3>")
            t_ind-=1
            hprint(f, "</div>")
            hprint(f, "<div class=\"sub-section\">")
            t_ind+=1
            hprint(f, "<ul>")
            t_ind+=1
            for pe in self.penalties:
                hprint(f,"<li>"+pe+"</li>")
            t_ind-=1
            hprint(f,"</ul>")
            t_ind-=1
            hprint(f,"</div>")
            t_ind-=1
        hprint(f,"</div>")
                
        
