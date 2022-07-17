ctr = {"a":295793,"b":63941,"c":152981,"d":113192,"e":376456,"f":39238,"g":82627,"h":92368,"i":313008,"j":5456,"k":26814,"l":194915,"m":105208,"n":251437,"o":251596,"p":113663,"q":5883,"r":246143,"s":250284,"t":230895,"u":131496,"v":33075,"w":22407,"x":10493,"y":70581,"z":14757}

from collections import Counter
import heapq

class Node:
    def __init__(self, char = None, left = None, right = None):
        self.char = char
        self.left = left
        self.right = right

    def __gt__(self, node):
        return True

class Huffman:
    def getLookup(s):
        ctr = Counter(s)
        heap = []
        for c, count in ctr.items():
            heapq.heappush(heap, (count, Node(char = c)))
        while len(heap) > 1:
            a, anode = heapq.heappop(heap)
            b, bnode = heapq.heappop(heap)
            heapq.heappush(heap, (a + b, Node(left = anode, right = bnode)))
        rootctr, root = heapq.heappop(heap)
        lookup = {}
        nodes = [(root, "")]
        while len(nodes) > 0:
            curr, currpath = nodes.pop()
            if curr:
                if curr.char != None:
                    lookup[curr.char] = currpath
                nodes.append((curr.left, currpath + "0"))
                nodes.append((curr.right, currpath + "1"))
        return lookup

    def invlookup(lookup):
        inv = {}
        for c, code in lookup.items():
            inv[code] = c
        return inv

    def encode(s, lookup):
        return "".join([lookup[c] for c in s])

    def decode(encoded, lookup):
        n = len(encoded)
        decoded = []
        i = 0
        for j in range(n + 1):
            if encoded[i:j] in lookup:
                decoded.append(lookup[encoded[i:j]])
                i = j
        return "".join(decoded)

s = "".join([c * n for c, n in ctr.items()])
lookup = Huffman.getLookup(s)
print(lookup)
