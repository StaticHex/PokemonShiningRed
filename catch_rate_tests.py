# HP CONSTANTS
def catch(ball_type = 15, hp_mod=0, STATUS=0, RARITY=1):
    r_mod = [1,1,1,2,2,2,3,3,3,4]
    roll = ball_type - (hp_mod*3 + 2*STATUS) + RARITY
    roll += r_mod[RARITY-1]
    roll = max(1, min(20, roll))
    return int(roll)

status = ['NORM', 'AFFL']
hp = ['FULL','HIGH','MID','LOW']

for i in range(1,11):
    print "RARITY:",i
    for j in range(2):
        print "STATUS:",status[j]
        for k in range(4):
            print "HP =",hp[k],
            for l in range(1,4):
                print catch(l*5,k,j,i),
            print ""
        
