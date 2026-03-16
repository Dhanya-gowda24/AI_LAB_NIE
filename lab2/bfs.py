from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    
    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=" ")   # Print traversal order
            visited.add(node)
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    queue.append(neighbor)

# --- User Input Section ---
graph = {}
n = int(input("Enter number of nodes: "))

for i in range(n):
    node = input(f"Enter node {i+1} name: ")
    neighbors = input(f"Enter neighbors of {node} (space-separated): ").split()
    graph[node] = neighbors

start = input("Enter starting node: ")

print("BFS Traversal:")
bfs(graph, start)

'''
output

Enter number of nodes: 4
Enter node 1 name: a
Enter neighbors of a (space-separated): b c
Enter node 2 name: b
Enter neighbors of b (space-separated): c
Enter node 3 name: c
Enter neighbors of c (space-separated): d
Enter node 4 name: d
Enter neighbors of d (space-separated):
Enter starting node: a
BFS Traversal:
a b c d
'''
