def topological(graph):
    visited = {}
    stack = []
    curr = list(graph.keys())[0]
    recstack = []
    while len(stack) < len(graph.keys()):

