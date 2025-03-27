import matplotlib.pyplot as plt
import networkx as nx

# Create a directed graph
G = nx.DiGraph()

# Nodes: Categories of data structures
categories = [
    "Linear Data Structures", 
    "Tree-Based Structures", 
    "Graph-Based Structures", 
    "Hashing Structures", 
    "Distributed Structures"
]

# Nodes: Characteristics and Use Cases
characteristics = [
    "Sequential Processing", "Efficient Search", 
    "Hierarchical Data Management", "Network Analysis", 
    "Data Indexing", "Scalability", 
    "Fault Tolerance", "Fast Retrieval"
]

# Adding nodes
G.add_nodes_from(categories + characteristics)

# Define edges to show relationships
edges = [
    ("Linear Data Structures", "Sequential Processing"),
    ("Tree-Based Structures", "Efficient Search"),
    ("Tree-Based Structures", "Hierarchical Data Management"),
    ("Graph-Based Structures", "Network Analysis"),
    ("Hashing Structures", "Data Indexing"),
    ("Hashing Structures", "Fast Retrieval"),
    ("Distributed Structures", "Scalability"),
    ("Distributed Structures", "Fault Tolerance")
]

G.add_edges_from(edges)

# Plotting the graph
plt.figure(figsize=(14, 10))
pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, with_labels=True, node_size=3500, node_color="lightblue", font_size=10, font_weight="bold", edge_color="gray")
plt.title("Categorization of Data Structures Based on Characteristics and Use Cases")
plt.show()
