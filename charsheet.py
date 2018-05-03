import random as rand

def printline(token=" "):
    l = ""
    for i in range(80):
        l += token
    print l

def expandToLine(string=""):
    while(len(string) < 78):
        string += " "
    return string

def printCharSheet():
    n = "*" + expandToLine(" Pokemon: Shining Red Version") + "*"
    printline("*")
    print n
    printline("*")
    print "BASIC CHARACTER INFORMATION"
    printline("-")
    print ""
    print "Name: ____________________ Height: _____ Weight: _____"
    print ""
    print "Owner (Player): ___________________"
    printline("-")
    print "STATS"
    printline("-")
    print "HP: _______ ATK: _______ DEF: _______"
    print ""
    print "SP. ATK: _______ SP. DEF: _______ SPD: ______"
    print ""
    print "Energy: __100/100__ Charisma:_______"
    print ""
    print "______P ______coins"
    printline("-")
    print "SKILLS"
    printline("-")
    for i in range(25):
        print "_________________________ _______"
    print ""
    printline("-")
    print "PERKS"
    printline("-")
    for i in range(10):
        print "_________________________________"
    printline("-")
    print "ITEMS"
    printline("-")
    for i in range(10):
        print "_________________________________"
    printline("-")
    print "NOTES"
    printline("-")
    for i in range(10):
        print "_________________________________"

def getIndex(probs = [0.166667, 0.166667, 0.166667, 0.166667, 0.166667, 0.166667]):
    s = 0.0
    p = rand.random()
    for i in range(6):
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

def generatePVector(stars=[5,5,5,5,5,5]):
    t = float(sum(stars))
    for i in range(len(stars)):
        stars[i] /= t
    return stars
    
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

def balanceStats(probs = [0.166667, 0.166667, 0.166667, 0.166667, 0.166667, 0.166667]):
    s_stats = [0, 0, 0, 0, 0, 0]
    for i in range(1000):
        s_stats = arrayAdd(s_stats, assignStats(probs), 6)
    s_stats = arrayDiv(s_stats, 1000.0, 6)
    return s_stats

def levelUpRoll():
    return [rand.randint(1,4)-1,rand.randint(1,4)-1,rand.randint(1,4)-1,rand.randint(1,4)-1,rand.randint(1,4)-1,rand.randint(1,4)-1]

def genStats(stats=[3,3,3,3,3,3], level=1):
    # Generate level 1 pokemon with base stats
    p_vec = generatePVector(stats)
    newStats = balanceStats(p_vec)
    ns2 = newStats[:]
    m = max(ns2)    
    prim_stat = []
    for i in range(len(ns2)):
        if ns2[i] == m:
            prim_stat.append(i)
            ns2[i] = -1
    m = max(ns2)
    sec_stat = []
    for i in range(len(ns2)):
        if ns2[i] == m:
            sec_stat.append(i)

    # Level up pokemon's stats based on the passed level
    for i in range(level-1):
        lup_stats = levelUpRoll()
        mSt = max(lup_stats)
        assigned = [1,1,1,1,1,1]
        p_ind = prim_stat[rand.randint(0,len(prim_stat)-1)]
        newStats[p_ind] += mSt
        assigned[p_ind] = 0
        lup_stats[lup_stats.index(mSt)] = -1
        
        mSt = max(lup_stats)
        s_ind = sec_stat[rand.randint(0,len(sec_stat)-1)]
        newStats[s_ind] += mSt
        assigned[s_ind] = 0
        lup_stats[lup_stats.index(mSt)] = -1
        while(max(assigned)):
            idx = rand.randint(0, len(lup_stats)-1)
            if(assigned[idx]):
                newStats[idx] += lup_stats[idx]
                assigned[idx] = 0

    # TODO: Calculate pokemon moves
    # TODO: Calculate pokemon skills
    print newStats
        
    
        

        
    


