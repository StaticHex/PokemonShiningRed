from asciiml import *
from header import *
from job import *
from modifier import *

"""
================================================================================
CLASS CONSTANTS
================================================================================
"""
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
    
def htmlHeader(f):
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
    t_ind -= 1
    hprint(f,"}")
    hprint(f,".stats {")
    t_ind += 1
    hprint(f, "height: 10%;")
    hprint(f, "border: 1px solid black;")
    hprint(f, "border-radius: 10px;")
    hprint(f, "background: #EEEEEE;")
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
    hprint(f, "background: #EEEEEE;")
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
CHARACTER CLASS
================================================================================
"""
class Character:
    global t_ind
    def __init__(self,fname="",ld=""):
        self.name = ""
        self.owner = ""
        self.height = 0
        self.weight = 0.0
        self.status = 0
        self.stats = {"HP":0,"ATK":0,"DEF":0,"SP. ATK":0,"SP. DEF":0,"SPD":0
                     ,"MAX HP":0,"ENERGY":0,"MAX ENERGY":0,"CHARISMA":0,"MAX CHARISMA":0}
        self.skills = {"hiking":0,"jumping":0,"swimming":0,"climbing":0,"fishing":0,
                       "hunting":0,"farming":0,"training":0,"riding":0,"trapping":0,
                       "poke speak":0,"veterinary":0,"husbandry":0,"tracking":0,
                       "camping":0,"foraging":0,"mining":0,"esp":0,"pharmaceuticals":0,
                       "herbology":0,"cooking":0,"tinkering":0,"sneaking":0,"lockpicking":0,
                       "pickpocketing":0,"instint":0,"fortitude":0,"medicine":0,"performing":0,
                       "mechanic":0,"hacking":0,"investigation":0,"persuasion":0, "intimidation":0,
                       "forecasting":0,"legend lore":0,"perception":0,"sensing":0,"geography":0}
        self.items = []
        self.cash = 0
        self.coins = 0
        self.perks = []
        self.defects = []
        self.job = Job()
        self.notes = []
        if len(fname):
            fname = fname.split("|")
            self.name = fname[0]
            self.owner = fname[1]
            self.height = int(fname[2])
            self.weight = float(fname[3])
            if not fname[4] == "-":
                st_list = fname[4].split(":")
                for i in range(len(pl_stats)):
                    self.stats[pl_stats[i]] = int(st_list[i])
            if not fname[5] == "-":
                sk_list = fname[5].split(":")
                for i in range(len(pl_skills)):
                    self.skills[pl_skills[i]] = int(sk_list[i])
            self.status = int(fname[6])
            if not fname[7] == "-":
                it_list = fname[7].split(",")
                for it in it_list:
                    it = it.split(":")
                    it[1] = int(it[1])
                    self.items.append(it)
            self.cash = int(fname[8])
            self.coins = int(fname[9])
            if not fname[10] == "-":
                pk_list = fname[10].split(":")
                for pk in pk_list:
                    pk = pk.lower().replace(" ","").replace("-","").replace("/","")
                    self.perks.append(perks[pk])
            if not fname[11] == "-":
                df_list = fname[11].split(":")
                for df in df_list:
                    df = df.lower().replace(" ","").replace("-","").replace("/","")
                    self.defects.append(defects[df])
            if not fname[12] == "-":
                jb = fname[12].lower().replace(" ","").replace("-","").replace("/","")
                self.job = jobs[jb]
            if len(fname) > 13:
                nt_list = fname[13].split(":")
                for nt in nt_list:
                    self.notes.append(nt.strip())
        if len(ld):
            self.load(ld)

    def save(self,pref=""):
        outstring = ""
        outstring += self.name + "|"
        outstring += self.owner + "|"
        outstring += str(self.height) + "|"
        outstring += str(self.weight) + "|"
        for i in range(len(pl_stats)):
            outstring += str(self.stats[pl_stats[i]])+":"
        outstring = outstring[:-1]+"|"
        for i in range(len(pl_skills)):
            outstring += str(self.skills[pl_skills[i]])+":"
        outstring = outstring[:-1]+"|"
        outstring += str(self.status)+"|"
        if len(self.items):
            for it in self.items:
                outstring+= it[0] + ":" + str(it[1]) + ","
            outstring = outstring[:-1]+"|"
        else:
            outstring += "-|"
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
        outstring += self.job.name.lower().replace(" ","").replace("-","").replace("/","")
        outstring += "|"
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
        self.__init__(content)

    def pprint(self):
        info = "| "+padString("Owner: "+self.owner,26,LEFT)
        info += padString("Ht: "+inchToFt(self.height),25,CENTER)
        info += padString("Wt: "+str(self.weight)+"lbs",25,RIGHT)+" |"

        st_str = ""
        st_len = [14,25,36,52,68,76]
        for i in range(6):
            if pl_stats[i] == "HP":
                st_str += pl_stats[i]
                st_str += ": "+str(self.stats[pl_stats[i]])
                st_str += "/"+str(self.stats["MAX HP"])
                st_str = padString(st_str,st_len[i],LEFT)
            else:
                st_str += pl_stats[i]
                st_str += ": "+str(self.stats[pl_stats[i]])
                st_str = padString(st_str,st_len[i],LEFT)
        st_str = "| "+st_str+" |"
        st_str2 = "Energy: "+str(self.stats["ENERGY"])+"/"
        st_str2 += str(self.stats["MAX ENERGY"])
        st_str2 = padString(st_str2,26,LEFT)
        st_str2 += "Charisma: "+str(self.stats["CHARISMA"])+"/"
        st_str2 += str(self.stats["MAX CHARISMA"])
        st_str2 = padString(st_str2,51,LEFT)
        st_str2 += padString("Status: "+cond[self.status],25,RIGHT)
        st_str2 = "| "+st_str2+" |"
        csh_str = ""
        csh_str += padString("Cash: "+str(self.cash)+"P",26,LEFT)
        csh_str += padString("Coins: "+str(self.coins),25,LEFT)
        csh_str += padString(" ",25,LEFT)
        csh_str = "| "+csh_str+" |"
        sk_str = ""
        for i in range(len(pl_skills)):
            if self.skills[pl_skills[i]]:
                sk_str += pl_skills[i][0].upper()+pl_skills[i][1:]
                sk_str += ": "+str(self.skills[pl_skills[i]])
                sk_str += "    "
        it_str = ""
        for it in self.items:
            if it[1] > 1:
                it_str += it[0]+" x "+str(it[1])+"    "
            else:
                it_str += it[0]+"    "
        print "="*80
        print "*"*80
        print "* "+padString(self.name,76,LEFT)+" *"
        print "*"*80
        print "="*80
        print "-"*80
        print info
        print "-"*80
        print st_str
        print "-"*80
        print st_str2
        print "-"*80
        print csh_str
        print "-"*80
        print "="*80
        print "| "+padString("Skills",76,CENTER)+" |"
        print "="*80
        print "-"*80
        printWrapped(sk_str,80,0,"| "," |")
        print "-"*80
        print "="*80
        print "| "+padString("Items",76,CENTER)+" |"
        print "="*80
        print "-"*80
        printWrapped(it_str,80,0,"| "," |")
        print "-"*80
        print "="*80
        print "| "+padString("Notes",76,CENTER)+" |"
        print "="*80
        print "-"*80
        for n in self.notes:
            printWrapped("* "+n,80,len("* "),"| "," |")
        self.job.pprint()
        for p in self.perks:
            p.pprint()
        for d in self.defects:
            d.pprint()

    def export(self, ref=""):
        if ref is "":
            if self.owner == "N/A":
                ref = "players/export/"+self.name+"-npc.txt"
            else:
                ref = "players/export/"+self.name+"-"+self.owner+".txt"
        ref = ref.lower()
        ref = ref.replace(" ","_")
        f = open(ref,'w')
        
        info = "| "+padString("Owner: "+self.owner,26,LEFT)
        info += padString("Ht: "+inchToFt(self.height),25,CENTER)
        info += padString("Wt: "+str(self.weight)+"lbs",25,RIGHT)+" |"

        st_str = ""
        st_len = [14,25,36,52,68,76]
        for i in range(6):
            if pl_stats[i] == "HP":
                st_str += pl_stats[i]
                st_str += ": "+str(self.stats[pl_stats[i]])
                st_str += "/"+str(self.stats["MAX HP"])
                st_str = padString(st_str,st_len[i],LEFT)
            else:
                st_str += pl_stats[i]
                st_str += ": "+str(self.stats[pl_stats[i]])
                st_str = padString(st_str,st_len[i],LEFT)
        st_str = "| "+st_str+" |"
        st_str2 = "Energy: "+str(self.stats["ENERGY"])+"/"
        st_str2 += str(self.stats["MAX ENERGY"])
        st_str2 = padString(st_str2,26,LEFT)
        st_str2 += "Charisma: "+str(self.stats["CHARISMA"])+"/"
        st_str2 += str(self.stats["MAX CHARISMA"])
        st_str2 = padString(st_str2,51,LEFT)
        st_str2 += padString("Status: "+cond[self.status],25,RIGHT)
        st_str2 = "| "+st_str2+" |"
        csh_str = ""
        csh_str += padString("Cash: "+str(self.cash)+"P",26,LEFT)
        csh_str += padString("Coins: "+str(self.coins),25,LEFT)
        csh_str += padString(" ",25,LEFT)
        csh_str = "| "+csh_str+" |"
        sk_str = ""
        for i in range(len(pl_skills)):
            if self.skills[pl_skills[i]]:
                sk_str += pl_skills[i][0].upper()+pl_skills[i][1:]
                sk_str += ": "+str(self.skills[pl_skills[i]])
                sk_str += "    "
        it_str = ""
        for it in self.items:
            if it[1] > 1:
                it_str += it[0]+" x "+str(it[1])+"    "
            else:
                it_str += it[0]+"    "

        f.write("="*80+"\n")
        f.write("*"*80+"\n")
        f.write("* "+padString(self.name,76,LEFT)+" *"+"\n")
        f.write("*"*80+"\n")
        f.write("="*80+"\n")
        f.write("-"*80+"\n")
        f.write(info+"\n")
        f.write("-"*80+"\n")
        f.write(st_str+"\n")
        f.write("-"*80+"\n")
        f.write(st_str2+"\n")
        f.write("-"*80+"\n")
        f.write(csh_str+"\n")
        f.write("-"*80+"\n")
        f.write("="*80+"\n")
        f.write("| "+padString("Skills",76,CENTER)+" |"+"\n")
        f.write("="*80+"\n")
        f.write("-"*80+"\n")
        writeWrapped(f,sk_str,80,0,"| "," |")
        f.write("-"*80+"\n")
        f.write("="*80+"\n")
        f.write("| "+padString("Items",76,CENTER)+" |"+"\n")
        f.write("="*80+"\n")
        f.write("-"*80+"\n")
        writeWrapped(f,it_str,80,0,"| "," |")
        f.write("-"*80+"\n")
        f.write("="*80+"\n")
        f.write("| "+padString("Notes",76,CENTER)+" |\n")
        f.write("="*80+"\n")
        f.write("-"*80+"\n")
        for n in self.notes:
            writeWrapped(f,"* "+n,80,len("* "),"| "," |")
        self.job.export(f)
        for p in self.perks:
            p.export(f)
        for d in self.defects:
            d.export(f)

    def html(self, ref=""):
        global t_ind, hprint
        if ref is "":
            if self.owner == "N/A":
                ref = "players/html/"+self.name+"-npc.html"
            else:
                ref = "players/html/"+self.name+"-"+self.owner+".html"
        ref = ref.lower()
        ref = ref.replace(" ","_")
        f = open(ref,'w')
        htmlHeader(f)
        hprint(f,"<div class=\"title\"><h1>"+self.name+"</h1></div>")
        t_ind+=1
        hprint(f,"<div class=\"cash\">")
        t_ind += 1
        hprint(f, "<div class=\"sub-txt\">")
        t_ind += 1
        hprint(f, "<strong>Owner:</strong> "+self.owner+"&nbsp;&nbsp;&nbsp;&nbsp;")
        hprint(f, "<strong>Ht:</strong> "+inchToFt(self.height)+"&nbsp;&nbsp;&nbsp;&nbsp;")
        hprint(f, "<strong>Wt:</strong> "+str(self.weight)+"lbs"+"&nbsp;&nbsp;&nbsp;&nbsp;")
        t_ind-=1
        hprint(f, "</div>")
        t_ind-=1
        hprint(f, "</div>")
        hprint(f, "<div class=\"stats\">")
        t_ind+=1
        hprint(f, "<div class=\"stat-sub1\">")
        t_ind+=1
        hprint(f, "<div class=\"sub-txt\">")
        t_ind+=1
        hstr = "<strong>HP:</strong> "
        hstr += str(self.stats["HP"])+"/"+str(self.stats["MAX HP"])
        hstr += "&nbsp;&nbsp;&nbsp;&nbsp;"
        hprint(f, hstr)
        for i in range(1,6):
            hstr = "<strong>"+pl_stats[i]+":</strong>"
            hstr += str(self.stats[pl_stats[i]])
            hstr += "&nbsp;&nbsp;&nbsp;&nbsp;"
            hprint(f, hstr)
        t_ind-=1
        hprint(f, "</div>")
        t_ind-=1
        hprint(f, "</div>")
        hprint(f, "<div class=\"stat-sub2\">")
        t_ind+=1
        hprint(f, "<div class=\"sub-txt\">")
        t_ind+=1
        hstr = "<strong>Energy:</strong> "
        hstr += str(self.stats["ENERGY"])+"/"+str(self.stats["MAX ENERGY"])
        hstr += "&nbsp;&nbsp;&nbsp;&nbsp;"
        hprint(f, hstr)
        hstr = "<strong>Charisma:</strong> "
        hstr += str(self.stats["CHARISMA"])+"/"+str(self.stats["MAX CHARISMA"])
        hstr += "&nbsp;&nbsp;&nbsp;&nbsp;"
        hprint(f, hstr)
        hstr = "<strong>Status:</strong> "
        hstr += cond[self.status]
        hprint(f, hstr)
        t_ind-=1
        hprint(f, "</div>")
        t_ind-=1
        hprint(f, "</div>")
        t_ind-=1
        hprint(f, "</div>")
        hprint(f, "<div class=\"cash\">")
        t_ind+=1
        hprint(f, "<div class=\"sub-txt\">")
        t_ind+=1
        hstr = "<strong>Cash:</strong> "
        hstr+= str(self.cash)+"P"
        hstr+= "&nbsp;&nbsp;&nbsp;&nbsp;"
        hprint(f, hstr)
        hstr = "<strong>Coins:</strong> "
        hstr+= str(self.coins)
        hstr+= "&nbsp;&nbsp;&nbsp;&nbsp;"
        hprint(f, hstr)
        t_ind-=1
        hprint(f, "</div>")
        t_ind-=1
        hprint(f, "</div>")
        hprint(f, "<div class=\"section-head\">")
        t_ind+=1
        hprint(f, "<div class=\"sub-txt\">")
        t_ind+=1
        hprint(f, "<h3 class=\"nopad\">Skills</h3>")
        t_ind-=1
        hprint(f, "</div>")
        t_ind-=1
        hprint(f, "</div>")
        hprint(f, "<div class=\"section-body\">")
        t_ind+=1
        hprint(f, "<div class=\"sub-txt\">")
        t_ind+=1
        hprint(f, "<table style=\"width: 100%;\">")
        t_ind+=1
        hprint(f, "<tr>")
        t_ind+=1
        sk_count = 0
        for i in range(len(pl_skills)):
            if self.skills[pl_skills[i]]:
                hstr = "<td><strong>"+pl_skills[i]+":</strong> "
                hstr += str(self.skills[pl_skills[i]])
                hstr += "&nbsp;&nbsp;&nbsp;&nbsp;</td>"
                hprint(f, hstr)
                sk_count += 1
            if sk_count and not (sk_count % 3):
                t_ind-=1
                hprint(f, "</tr>")
                hprint(f, "<tr>")
                t_ind+=1
                sk_count = 0
        while sk_count < 3:
            hprint(f, "<td></td>")
            sk_count+=1
        t_ind-=1
        hprint(f, "</tr>")
        t_ind-=1
        hprint(f, "</table>")
        t_ind-=1
        hprint(f, "</div>")
        t_ind-=1
        hprint(f, "</div>")
        if len(self.items):
            hprint(f, "<div class=\"section-head\">")
            t_ind+=1
            hprint(f, "<div class=\"sub-txt\">")
            t_ind+=1
            hprint(f, "<h3 class=\"nopad\">Items</h3>")
            t_ind-=1
            hprint(f, "</div>")
            t_ind-=1
            hprint(f, "</div>")
            hprint(f, "<div class=\"section-body\">")
            t_ind+=1
            hprint(f, "<div class=\"sub-txt\">")
            t_ind+=1
            hprint(f, "<table style=\"width: 100%;\">")
            t_ind+=1
            hprint(f, "<tr>")
            t_ind+=1
            it_count = 0
            for it in self.items:
                hstr = "<td>"+it[0]
                if it[1] > 1:
                    hstr += " x "+str(it[1])
                hstr += "&nbsp;&nbsp;&nbsp;&nbsp;</td>"
                hprint(f, hstr)
                it_count += 1
                if it_count and not (it_count % 3):
                    t_ind-=1
                    hprint(f, "</tr>")
                    hprint(f, "<tr>")
                    t_ind+=1
                    it_count = 0
            while it_count < 3:
                hprint(f, "<td></td>")
                it_count+=1
            t_ind-=1
            hprint(f, "</tr>")
            t_ind-=1
            hprint(f, "</table>")
            t_ind-=1
            hprint(f, "</div>")
            t_ind-=1
            hprint(f, "</div>")
        if len(self.notes):
            if not self.notes[0] == "":
                hprint(f, "<div class=\"section-head\">")
                t_ind+=1
                hprint(f, "<div class=\"sub-txt\">")
                t_ind+=1
                hprint(f, "<h3 class=\"nopad\">Notes</h3>")
                t_ind-=1
                hprint(f, "</div>")
                t_ind-=1
                hprint(f, "</div>")
                hprint(f, "<div class=\"section-body\">")
                t_ind+=1
                hprint(f, "<div class=\"sub-txt\">")
                t_ind+=1
                hprint(f, "<ul>")
                t_ind+=1
                for nt in self.notes:
                    hprint(f,"<li>"+nt+"</li>")
                hprint(f, "</ul>")
                t_ind-=1
                hprint(f, "</div>")
                t_ind-=1
                hprint(f, "</div>")
        hprint(f,"<div class=\"title\">")
        t_ind+=1
        hstr = "<h2 class=\"nopad\" style=\"padding-top:20px;\">Class</h2>"
        hprint(f,hstr)
        t_ind-=1
        hprint(f,"</div>")
        self.job.html(f)
        pnum = 0
        if len(self.perks):
            hprint(f,"<div class=\"title\">")
            t_ind+=1
            hstr = "<h2 class=\"nopad\" style=\"padding-top:20px;\">Perks</h2>"
            hprint(f,hstr)
            t_ind-=1
            hprint(f,"</div>")
            for pe in self.perks:
                pe.html(f,pnum,PERK)
                pnum+=1
        if len(self.defects):
            hprint(f,"<div class=\"title\">")
            t_ind+=1
            hstr = "<h2 class=\"nopad\" style=\"padding-top:20px;\">Defects</h2>"
            hprint(f,hstr)
            t_ind-=1
            hprint(f,"</div>")
            for de in self.defects:
                de.html(f,pnum,DEFECT)
                pnum+=1
        htmlFooter(f)
        f.close()
        
    def getStatus(self):
        return cond[self.status]
    
    def setStatus(self, new_status):
        new_status = new_status.upper()
        for i in range(len(cond)):
            if cond[i] == new_status:
                self.status = i

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
            
            
        

                
        
