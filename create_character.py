from header import *
from character import *

p = Character()
p.name = "Keith"
p.height = 68
p.weight = 130
#p.owner = "Travis"
p.job = jobs["camperpicnicker"]
p.status = 0
p.stats["HP"] = 136
p.stats["MAX HP"] = 136
p.stats["ATK"] = 68
p.stats["DEF"] = 102
p.stats["SP. ATK"] = 34
p.stats["SP. DEF"] = 34
p.stats["SPD"] = 34
p.stats["ENERGY"] = 100
p.stats["MAX ENERGY"] = 100
p.stats["CHARISMA"] = 10
p.stats["MAX CHARISMA"] = 20
p.setSkill("Training",15,SET)
p.setSkill("Poke Speak",15,SET)
p.setSkill("Perception",10,SET)
p.setSkill("Camping",10,SET)
p.setSkill("Forecasting",10,SET)
p.setSkill("Hiking",10,SET)
p.setSkill("Climbing",10,SET)
p.setSkill("Hunting",2,SET)
p.setSkill("Foraging",2,SET)
p.setSkill("Cooking",2,SET)
p.setSkill("Instinct",2,SET)
p.notes.append("1 die added to attack rolls when battling in the forest")
p.notes.append("Roll advantage when using the instinct skill.")
p.cash = 1000
p.coins = 0
p.perks.append(findPerk("Pressure Player"))
p.items.append(("Compass",1))
p.items.append(("Binoculars",1))
p.items.append(("Radio",1))
p.items.append(("PPHC",1))
p.save()
