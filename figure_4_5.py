# Conceptual Diagram for Real-World Applications and Data Structures
import networkx as nx
import matplotlib.pyplot as plt

# Creating the Graph
G = nx.DiGraph()

# Nodes for Applications and Data Structures
applications = ['Recommendation Systems', 'Fraud Detection', 'Medical Diagnosis', 'Social Media Analysis']
data_structures = ['Graph', 'Hash Table', 'Bloom Filter', 'B-Tree', 'Distributed Hash Table']

# Adding nodes
G.add_nodes_from(applications, type='Application')
G.add_nodes_from(data_structures, type='Data Structure')

# Adding connections
edges = [
    ('Recommendation Systems', 'Graph'),
    ('Recommendation Systems', 'Hash Table'),
    ('Fraud Detection', 'Bloom Filter'),
    ('Fraud Detection', 'Hash Table'),
    ('Medical Diagnosis', 'B-Tree'),
    ('Medical Diagnosis', 'Distributed Hash Table'),
    ('Social Media Analysis', 'Graph'),
    ('Social Media Analysis', 'Distributed Hash Table')
]
G.add_edges_from(edges)

# Visualization
pos = nx.spring_layout(G, seed=42)
node_colors = ['skyblue' if node in applications else 'lightgreen' for node in G.nodes]
nx.draw(G, pos, with_labels=True, node_color=node_colors, node_size=3000, font_size=10, font_weight='bold')
plt.title('Conceptual Diagram of Real-World Applications and Data Structures')
plt.show()


# Bar Chart for Distribution of Data Structures Across Industries
data = {'Graph': 30, 'Hash Table': 25, 'Bloom Filter': 15, 'B-Tree': 20, 'Distributed Hash Table': 10}
plt.figure(figsize=(8,5))
plt.bar(data.keys(), data.values(), color=['blue', 'orange', 'green', 'red', 'purple'])
plt.xlabel('Data Structures')
plt.ylabel('Usage Percentage (%)')
plt.title('Distribution of Data Structures Across Industries')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
