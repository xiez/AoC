# source: https://adventofcode.com/2021/day/2

# part 1
loc = []                      # list of commands
with open('./input') as f:
    for ln in f:
        cmd, unit = ln.split(' ')
        loc.append((cmd, int(unit)))

class Position:
    def __init__(self, x=0, y=0, aim=0):
        self.x = x
        self.y = y
        self.aim = aim

class Submarine:
    def __init__(self, init_pos, loc):
        self.pos = init_pos
        self.loc = loc

    def forward(self, unit):
        self.pos.x += unit

    def down(self, unit):
        self.pos.y -= unit

    def up(self, unit):
        self.pos.y += unit
        assert self.pos.y <= 0

    def pilot(self):
        for ele in self.loc:
            command, unit = ele
            method = getattr(self, command)
            method(unit)

    def final_position(self):
        return self.pos.x * abs(self.pos.y)

init_pos = Position()
s = Submarine(init_pos, loc)
s.pilot()

print('What do you get if you multiply your final horizontal position by your final depth?')
print('Answer:', s.final_position())

# part2
class Submarine:
    def __init__(self, init_pos, loc):
        self.pos = init_pos
        self.loc = loc

    def forward(self, unit):
        self.pos.x += unit
        self.pos.y = self.pos.y - (self.pos.aim * unit)

    def down(self, unit):
        self.pos.aim -= unit

    def up(self, unit):
        self.pos.aim += unit

    def pilot(self):
        for ele in self.loc:
            command, unit = ele
            method = getattr(self, command)
            method(unit)

    def final_position(self):
        return self.pos.x * abs(self.pos.y)

init_pos = Position()
s = Submarine(init_pos, loc)
s.pilot()

print('What do you get if you multiply your final horizontal position by your final depth?')
print('Answer:', s.final_position())
