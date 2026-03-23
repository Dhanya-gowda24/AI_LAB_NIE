# Iterative Deepening Depth First Search (IDDFS) with user input

# Depth-Limited Search (DLS)
def dls(graph, start, target, limit):
    if start == target:
        return True
    if limit <= 0:
        return False
    for neighbor in graph.get(start, []):
        if dls(graph, neighbor, target, limit - 1):
            return True
    return False

# Iterative Deepening DFS
def iddfs(graph, start, target, max_depth):
    for depth in range(max_depth + 1):
        print(f"Searching at depth {depth}...")
        if dls(graph, start, target, depth):
            return True
    return False

# Build graph from user input
graph = {}
n = int(input("Enter number of vertices: "))
for i in range(n):
    vertex = input(f"Enter name of vertex {i+1}: ")
    graph[vertex] = []

e = int(input("Enter number of edges: "))
for i in range(e):
    u = input(f"Enter edge {i+1} start vertex: ")
    v = input(f"Enter edge {i+1} end vertex: ")
    graph[u].append(v)

print("\nGraph adjacency list:")
for key in graph:
    print(key, ":", graph[key])

# Run IDDFS
start = input("\nEnter start node: ")
target = input("Enter target node: ")
max_depth = int(input("Enter maximum depth to search: "))

found = iddfs(graph, start, target, max_depth)

if found:
    print(f"\nTarget {target} found within depth {max_depth}.")
else:
    print(f"\nTarget {target} not found within depth {max_depth}.")


'''
output

Enter number of vertices: 4
Enter name of vertex 1: a
Enter name of vertex 2: b
Enter name of vertex 3: c
Enter name of vertex 4: d
Enter number of edges: 3
Enter edge 1 start vertex: a
Enter edge 1 end vertex: b
Enter edge 2 start vertex: a
Enter edge 2 end vertex: c
Enter edge 3 start vertex: b
Enter edge 3 end vertex: d

Graph adjacency list:
a : ['b', 'c']
b : ['d']
c : []
d : []

Enter start node: a
Enter target node: d
Enter maximum depth to search: 3
Searching at depth 0...
Searching at depth 1...
Searching at depth 2...

Target d found within depth 3.
'''
