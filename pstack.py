from asciiml import *
from pokemon import *
"""
================================================================================
POKESTACK CLASS
================================================================================
"""
class PokeStack:
    def __init__(self,ref=""):
        self.stack = []
        if len(ref):
            self.loadAll(ref)

    def push(self, pk, name=""):
        if len(name):
            self.stack.append([pk,name])
        else:
            if pk.owner == "N/A":
                self.stack.append([pk,pk.species+"-"+"unclaimed"])
            else:
                self.stack.append([pk,pk.species+"-"+pk.owner])

    def pop(self,pos=-1):
        if pos == -1:
            self.stack = self.stack[:pos]
        elif pos == 0:
            self.stack = self.stack[1:]
        else:
            self.stack = self.stack[:pos]+self.stack[pos+1:]

    def top(self, pos=-1):
        return self.stack[pos][0]

    def flush(self):
        self.stack = []
                
    def setName(self,i,name):
        self.stack[i][1] = name

    def addRef(self,i,ref):
        self.stack[i-1][1] = ref+"-"+self.stack[i-1][1]

    def update(self):
        for s in self.stack:
            if s[0].owner == "N/A":
                s[1] = s[0].species+"-"+"unclaimed"
            else:
                s[1] = s[0].species+"-"+s[0].owner

    def pprint(self):
        if len(self.stack):
            line = 2*len("| ") + 3 + 16 + len(" | ") + 32
            print '-'*line
            i = 0
            for s in self.stack:
                st = "| "+padString(str(i),3, LEFT)
                st += padString(s[0].species,16,LEFT)+" | "
                st += padString(s[1],32,LEFT)+" |"
                print st
                print "-"*line
                i += 1

    def save(self,ref=""):
        for s in self.stack:
            if len(ref):
                s[0].save("pokemon/saved/"+ref+"-"+s[1]+".txt")
                s[1] = ref+"-"+s[1]
            else:
                s[0].save("pokemon/saved/"+s[1]+".txt")

    def export(self,ref=""):
        for s in self.stack:
            s[0].export("pokemon/export/"+s[1]+".txt")

    def html(self):
        for s in self.stack:
            s[0].html("pokemon/html/"+s[1]+".html")

    def heal(self):
        for s in self.stack:
            s[0].heal()

    def loadAll(self,ref=""):
        self.stack = []
        sav = getSaved()
        for s in sav:
            pk = Pokemon(ld=s)
            if ref+"-" in s:
                self.push(pk,s)

"""
================================================================================
CLASS HELPER FUNCTIONS
================================================================================
"""
def getSaved():
    saved = [i[:-4] for i in listdir("pokemon/saved")]
    return saved[:]
        
