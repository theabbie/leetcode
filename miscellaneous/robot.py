t = int(input())


class Robot:
    def __init__(self):
        self.robot = [[" ", "o", " "], ["/", "|", "\\"], ["/", " ", "\\"]]
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
            print("\n".join("".join(r) for r in self.robot))
        else:
            cmap = {"/": "\\", "\\": "/", "o": "o", "|": "|",
                    "<": ">", ">": "<", "(": ")", ")": "(", " ": " "}
            print("\n".join("".join([cmap[c]
                  for c in r[::-1]]) for r in self.robot))

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
        self.robot[0][0] = " "
        self.robot[1][0] = " "
        self.robot[0][0] = self.getHand(True, 1)

    def leftHandToStart(self):
        self.robot[0][0] = " "
        self.robot[1][0] = " "
        self.robot[1][0] = self.getHand(True, 0)

    def leftHandToHip(self):
        self.robot[0][0] = " "
        self.robot[1][0] = " "
        self.robot[1][0] = self.getHand(True, 2)

    def leftLegIn(self):
        self.robot[2][0] = self.getLeg(True, 1)

    def leftLegOut(self):
        self.robot[2][0] = self.getLeg(True, 0)

    def rightHandToHead(self):
        self.robot[0][2] = " "
        self.robot[1][2] = " "
        self.robot[0][2] = self.getHand(False, 1)

    def rightHandToStart(self):
        self.robot[0][2] = " "
        self.robot[1][2] = " "
        self.robot[1][2] = self.getHand(False, 0)

    def rightHandToHip(self):
        self.robot[0][2] = " "
        self.robot[1][2] = " "
        self.robot[1][2] = self.getHand(False, 2)

    def rightLegIn(self):
        self.robot[2][2] = self.getLeg(False, 1)

    def rightLegOut(self):
        self.robot[2][2] = self.getLeg(False, 0)


for testcase in range(t):
    n = int(input())
    robot = Robot()
    for cm in range(n):
        s = input()
        if s.startswith("say "):
            print(s[4:])
            continue
        else:
            robot.command(s)
            robot.print()