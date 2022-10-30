import random
from time import sleep

class Human:
    def __init__(self):
        self.human = [[" ", "o", " "], ["/", "|", "\\"], ["/", " ", "\\"]]
        self.front = False
        self.commandmap = {
            "left hand to head": self.leftHandToHead,
            "left hand to hip": self.leftHandToHip,
            "left hand to start": self.leftHandToStart,
            "left leg in": self.leftLegIn,
            "left leg out": self.leftLegOut,
            "right hand to head": self.rightHandToHead,
            "right hand to hip": self.rightHandToHip,
            "right hand to start": self.rightHandToStart,
            "right leg in": self.rightLegIn,
            "right leg out": self.rightLegOut,
            "turn": self.turn,
        }

    def print(self):
        if self.front:
            print("\n".join("".join(r) for r in self.human))
        else:
            cmap = {"/": "\\", "\\": "/", "o": "o", "|": "|",
                    "<": ">", ">": "<", "(": ")", ")": "(", " ": " "}
            print("\n".join("".join([cmap[c]
                  for c in r[::-1]]) for r in self.human))

    def command(self, s):
        self.commandmap[s]()

    def getHand(self, left, k):
        l = ["/", "(", "<"]
        r = ["\\", ")", ">"]
        if left:
            return l[k]
        return r[k]

    def getLeg(self, left, k):
        l = ["/", "<"]
        r = ["\\", ">"]
        if left:
            return l[k]
        return r[k]

    def turn(self):
        self.front = not self.front

    def leftHandToHead(self):
        self.human[0][0] = " "
        self.human[1][0] = " "
        self.human[0][0] = self.getHand(True, 1)

    def leftHandToStart(self):
        self.human[0][0] = " "
        self.human[1][0] = " "
        self.human[1][0] = self.getHand(True, 0)

    def leftHandToHip(self):
        self.human[0][0] = " "
        self.human[1][0] = " "
        self.human[1][0] = self.getHand(True, 2)

    def leftLegIn(self):
        self.human[2][0] = self.getLeg(True, 1)

    def leftLegOut(self):
        self.human[2][0] = self.getLeg(True, 0)

    def rightHandToHead(self):
        self.human[0][2] = " "
        self.human[1][2] = " "
        self.human[0][2] = self.getHand(False, 1)

    def rightHandToStart(self):
        self.human[0][2] = " "
        self.human[1][2] = " "
        self.human[1][2] = self.getHand(False, 0)

    def rightHandToHip(self):
        self.human[0][2] = " "
        self.human[1][2] = " "
        self.human[1][2] = self.getHand(False, 2)

    def rightLegIn(self):
        self.human[2][2] = self.getLeg(False, 1)

    def rightLegOut(self):
        self.human[2][2] = self.getLeg(False, 0)


commands = ['left hand to head', 'left hand to hip', 'left hand to start', 'left leg in', 'left leg out',
            'right hand to head', 'right hand to hip', 'right hand to start', 'right leg in', 'right leg out', 'turn']

human = Human()

prev = None

while True:
    print("\033[H\033[J", end="")
    step = random.choice(commands)
    while step == prev:
        step = random.choice(commands)
    prev = step
    human.command(step)
    human.print()
    sleep(0.4)