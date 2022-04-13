import heapq

from collections import defaultdict

#This class represents a undirected graph using adjacency list representation
class Graph:

	def __init__(self,vertices):
		self.V= vertices #No. of vertices
		self.graph = defaultdict(set) # default dictionary to store graph


	# function to add an edge to graph
	def addEdge(self,u,v):
		self.graph[u].add(v)
		
	def removeEdge(self,u,v):
	    self.graph[u].remove(v)

	# A utility function to find the subset of an element i
	def find_parent(self, parent,i):
		if parent[i] == -1:
			return i
		if parent[i]!= -1:
			return self.find_parent(parent,parent[i])

	# A utility function to do union of two subsets
	def union(self,parent,x,y):
		parent[x] = y



	# The main function to check whether a given graph
	# contains cycle or not
	def isCyclic(self):
		
		# Allocate memory for creating V subsets and
		# Initialize all subsets as single element sets
		parent = [-1]*(self.V)

		# Iterate through all edges of graph, find subset of both
		# vertices of every edge, if both subsets are same, then
		# there is cycle in graph.
		for i in self.graph:
			for j in self.graph[i]:
				x = self.find_parent(parent, i)
				y = self.find_parent(parent, j)
				if x == y:
				    return True
				self.union(parent,x,y)

class Solution:
    def union(self, parent, i, j):
        parent[i] = j
        
    def getParent(self, parent, i):
        if parent[i] == -1:
            return i
        return self.getParent(parent, parent[i])
        
    def isCycle(self, edges, n):
        print(edges)
        parent = [-1] * n
        for i, j in edges:
            if self.getParent(parent, i) == self.getParent(parent, j):
                return True
            self.union(parent, i, j)
        print(parent)
        return False
    
    def minCostConnectPoints(self, points):
        n = len(points)
        edges = []
        for i in range(n):
            for j in range(i + 1, n):
                a, b = points[i]
                c, d = points[j]
                dist = abs(c - a) + abs(d - b)
                heapq.heappush(edges, (dist, i, j))
        minedges = []
        op = 0
        g = Graph(n)
        while len(minedges) < n - 1:
            if len(edges) > 0:
                currdist, i, j = heapq.heappop(edges)
                curredges = minedges + [(i, j)]
                g.addEdge(i,j)
                if not g.isCyclic():
                    minedges.append((i, j))
                    op += currdist
                else:
                    g.removeEdge(i,j)
        return op