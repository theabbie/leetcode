import math
import os

cx, cy = [int(x) for x in input("center?").split()]
r = int(input("r?"))
n = int(input("n?"))
k = int(input("k?"))

commands = []

for o in range(k):
    # offset = eval(input("Offset?"))
    # if offset == "":
    #    break
    offset = o / k
    for i in range(n):
        ang1 = math.radians((offset + i) * 360 / n)
        ang2 = math.radians((offset + i + 1) * 360 / n)
        x1, y1 = r * math.cos(ang1), r * math.sin(ang1)
        x2, y2 = r * math.cos(ang2), r * math.sin(ang2)
        commands.append("input touchscreen swipe {} {} {} {}".format(cx + x1, cy + y1, cx + x2, cy + y2))
    os.system('adb shell "' + " && ".join(commands) + '"')
