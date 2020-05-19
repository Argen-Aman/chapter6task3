import random

class Hero:
    def __init__(self, name, team):
        self.name = name
        self.team = team
        self.level = 0

    def levelup(self, team_size):
        self.level = team_size / 1000


class Soldier:
    def __init__(self, id, team):
        self.id = id
        self.team = team

    def follow_the_hero(self, hero):
        print(f'Soldier with ID {self.id} follows {hero.name}.')

teams = [1, 2]
targaryen = []
lannister = []

daenerys = Hero('Daenerys Targaryen', targaryen)
cersei = Hero('Cersei Lannister', lannister)
soldiers = []

for i in range(1,100001):
    soldiers.append(Soldier(i, random.choice(teams)))

for i in soldiers:
    if i.team == 1:
        targaryen.append(i)
    else:
        lannister.append(i)

daenerys.levelup(len(targaryen))
cersei.levelup(len(lannister))

print(f'House Targaryen with {len(targaryen)} warriors and 3 dragons ~VS~ House Lannister in King\'s Landing with {len(lannister)} warriors.')

print('# 1 dragon = +10 to level.\n# King\'s Landing = +15 to level.\n')

print ('Daenerys\' level: %.2f.\nCersei\'s level: %.2f.\n' %(daenerys.level + 3 * 10, cersei.level + 15))

if daenerys.level + 3 * 10 > cersei.level + 15:
    random.choice(targaryen).follow_the_hero(daenerys)
else:
    random.choice(targaryen).follow_the_hero(cersei)
