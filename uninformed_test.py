import networkx as nx
import matplotlib.pyplot as plt
from bfs import bfs
from dfs import dfs
from id_dfs import iddfs 

# graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': [],
    'G': []
}

# Count maximum depth of the tree (for IDDFS)
def get_max_depth(graph, start):
    visited = set()
    stack = [(start, 0)]
    max_depth = 0
    
    while stack:
        node, depth = stack.pop()
        if depth > max_depth:
            max_depth = depth
        if node not in visited:
            visited.add(node)
            for neighbor in graph.get(node, []):
                stack.append((neighbor, depth + 1))
    return max_depth

# directed graph
G = nx.DiGraph()

# edges
for node, neighbors in graph.items():
    for neighbor in neighbors:
        G.add_edge(node, neighbor)

# Draw
plt.figure(figsize=(6, 5))
pos = nx.spring_layout(G)

nx.draw(
    G, pos,
    with_labels=True,
    node_color='lightblue',
    node_size=2000,
    font_size=12,
    font_weight='bold',
    arrows=True
)

plt.title("Graph Representation")
plt.show()

# Defining start node
start_node = 'A'

# Calculate max depth for IDDFS
max_depth = get_max_depth(graph, start_node)

# Function calls
print("BFS:", bfs(graph, start_node))
print("DFS:", dfs(graph, start_node))
print("IDDFS:", iddfs(graph, start_node, max_depth))