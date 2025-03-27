import matplotlib.pyplot as plt
import networkx as nx
import random

G = nx.Graph()

# Define nodes
categories = [
    "Linear Data Structures", "Tree-Based Structures", 
    "Graph-Based Structures", "Hashing Structures", 
    "Distributed Structures"
]

examples = [
    "Arrays", "Linked Lists", "Stacks", "Queues", 
    "Binary Search Trees", "B-Trees", "AVL Trees",
    "Adjacency Lists", "Graph Neural Networks", 
    "Hash Tables", "Bloom Filters",
    "Distributed Hash Tables", "Distributed File Systems"
]

# Add nodes
G.add_nodes_from(categories + examples)

# Define edges for hierarchy
edges = [
    ("Linear Data Structures", "Arrays"),
    ("Linear Data Structures", "Linked Lists"),
    ("Linear Data Structures", "Stacks"),
    ("Linear Data Structures", "Queues"),
    ("Tree-Based Structures", "Binary Search Trees"),
    ("Tree-Based Structures", "B-Trees"),
    ("Tree-Based Structures", "AVL Trees"),
    ("Graph-Based Structures", "Adjacency Lists"),
    ("Graph-Based Structures", "Graph Neural Networks"),
    ("Hashing Structures", "Hash Tables"),
    ("Hashing Structures", "Bloom Filters"),
    ("Distributed Structures", "Distributed Hash Tables"),
    ("Distributed Structures", "Distributed File Systems")
]

G.add_edges_from(edges)

# Assign random colors for each category and edge styles
node_colors = ["#FFB6C1" if node in categories else "#ADD8E6" for node in G.nodes]
edge_colors = ["#FFA07A" if edge[0] in categories else "#90EE90" for edge in G.edges]
edge_styles = ["dashed" if edge[0] in categories else "solid" for edge in G.edges]

# Plot the graph using a circular layout
plt.figure(figsize=(16, 10))
pos = nx.circular_layout(G)
nx.draw(G, pos, with_labels=True, node_size=3000, node_color=node_colors, font_size=9, font_weight="bold", edge_color=edge_colors)

for i, (u, v) in enumerate(G.edges()):
    nx.draw_networkx_edges(G, pos, edgelist=[(u, v)], style=edge_styles[i])

plt.title("Colorful Classification of Data Structures for Large-Scale Machine Learning")
plt.show()
