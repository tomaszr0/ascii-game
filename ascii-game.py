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
        for y in range(len(self.map)):
            line = ""
            for x in range(len(self.map[y])):
                if self.player['x'] == x and self.player['y'] == y:
                    line += "P"
                else:
                    line += self.mapNodeTypes[self.map[y][x]]["character"]
            print(line)
    # def printMap /

    def main(self):
        while 1:
            print ("Legend:\nP\tplayer")
            for a in self.mapNodeTypes:
                print (a['character'] + "\t" + a['name'])
            print("\n")
            self.printMap()
            print("\nWhat do you want to do? (Type one of the commands in the square brackets)\n[N]\tMove north\n[E]\tMove east\n[S]\tMove south\n[W]\tMove west\n")
            command = input(">> ").upper()
            if command == 'N':
                self.player['y'] -= 1
            if command == 'E':
                self.player['x'] += 1
            if command == 'S':
                self.player['y'] += 1
            if command == 'W':
                self.player['x'] -= 1
                
    
    # def main /
    
# class gameEngine /

game = gameEngine()





