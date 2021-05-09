import time
import random


class gameEngine:
    # settings
    width = 32
    height = 16
    # setting /
    
    mapNodeTypes = [       
        {"name": "ground", "character": "-", "traversable": 1},
        {"name": "water", "character": "&", "traversable": 0},
        {"name": "bridge", "character": "|", "traversable": 1},
        {"name": "rock", "character": "#", "traversable": 0},
        {"name": "tree", "character": "T", "traversable": 0},
        ]
    map = []
    player = {"x": 5, "y": height-3}
    mobs = {}
    
    def __init__(self):
        print("generating map...")
        # generate ground
        for y in range(self.height):
            self.map.append([])
            for x in range(self.width):
                self.map[y].append(0)
        #generate ground /

        #generate river
        yMin = self.height//2 - 2
        yMax = self.height//2
        xBridge = self.width*2//3 + random.randint(-2,2)
        x = 0
        y = random.randint(yMin,yMax)
        lastChange = 0
        while x < self.width:
            if x == xBridge or x == xBridge+1:
                nodeType = 2
            else:
                nodeType = 1
            self.map[y][x] = nodeType
            self.map[y+1][x] = nodeType
            if x - lastChange > 3 and (x < xBridge - 2 or x > xBridge + 3):
                lastChange = x
                y += random.randint(-1,1)
                if y > yMax:
                    y = yMax
                elif y < yMin:
                    y = yMin
            x += 1
        #generate river /

        self.main()
    # def _init_ /

    def printMap(self):
        msg = ""
        for y in range(len(self.map)):
            line = ""
            for x in range(len(self.map[y])):
                if self.player['x'] == x and self.player['y'] == y:
                    line += "P"
                else:
                    line += self.mapNodeTypes[self.map[y][x]]["character"]
            msg += line + "\n"
        return msg
    # def printMap /

    def main(self):
        while 1:
            msg, commands = self.travel()
            msg += "\nWhat do you want to do? (Type one of the commands in the square brackets)\n"
            options = []
            for cmd in commands:
                msg += '['+cmd['letter']+']\t' + cmd['desc'] + '\n'
                options.append(cmd['letter'])
            msg += "\n>> "
            
            while 1:
                command = input(msg).upper()
                if command in options:
                    break
                print('Enter the correct command.')
                time.sleep(1)
            self.travel(1, command)
    # def main /

    def travel(self, mode = 0, cmd = ""):
        if mode == 0:
            msg = ""
            msg += ("Legend:\nP\tplayer\n")
            for a in self.mapNodeTypes:
                msg += (a['character'] + "\t" + a['name']) + "\n"
            msg += ("\n")
            msg += self.printMap()

            commands = []
            x = self.player['x']
            y = self.player['y']
            m = self.map
            t = self.mapNodeTypes
            if y > 0:
                if t[m[y-1][x]]['traversable'] == 1:
                    commands.append({'letter':'W', 'desc':'move North'})
            if y < self.height-1:
                if t[m[y+1][x]]['traversable'] == 1:
                    commands.append({'letter':'S', 'desc':'move South'})
            if x > 0:
                if t[m[y][x-1]]['traversable'] == 1:
                    commands.append({'letter':'A', 'desc':'move West'})
            if x < self.width-1:
                if t[m[y][x+1]]['traversable'] == 1:
                    commands.append({'letter':'D', 'desc':'move East'})
            return msg, commands
        
        if cmd == 'W':
            self.player['y'] -= 1
        elif cmd == 'D':
            self.player['x'] += 1
        elif cmd == 'S':
            self.player['y'] += 1
        elif cmd == 'A':
            self.player['x'] -= 1
    # def travel /
    
# class gameEngine /

game = gameEngine()





