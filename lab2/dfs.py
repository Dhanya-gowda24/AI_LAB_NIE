# Depth First Search (DFS) with user input

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=" ")
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Build the graph from user input
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

# Show the graph
print("\nGraph adjacency list:")
for key in graph:
    print(key, ":", graph[key])

# Run DFS
start = input("\nEnter starting vertex for DFS: ")
print("DFS Traversal:")
dfs(graph, start)

'''
output

Enter number of vertices: 4
Enter name of vertex 1: a
Enter name of vertex 2: b
Enter name of vertex 3: c
Enter name of vertex 4: d
Enter number of edges: 4
Enter edge 1 start vertex: a
Enter edge 1 end vertex: b
Enter edge 2 start vertex: a
Enter edge 2 end vertex: c
Enter edge 3 start vertex: b
Enter edge 3 end vertex: d
Enter edge 4 start vertex: c
Enter edge 4 end vertex: d

Graph adjacency list:
a : ['b', 'c']
b : ['d']
c : ['d']
d : []

Enter starting vertex for DFS: a
DFS Traversal:
a b d c
'''
