import matplotlib.pyplot as plt
import networkx as nx

G = nx.DiGraph()

# Nodes
G.add_nodes_from(["Data Collection", "Data Preprocessing", "Efficient Data Structures", "Feature Engineering", "Model Training", "Model Evaluation", "Deployment"])

# Edges
G.add_edges_from([
    ("Data Collection", "Data Preprocessing"),
    ("Data Preprocessing", "Efficient Data Structures"),
    ("Efficient Data Structures", "Feature Engineering"),
    ("Feature Engineering", "Model Training"),
    ("Model Training", "Model Evaluation"),
    ("Model Evaluation", "Deployment")
])

# Plot
plt.figure(figsize=(10, 6))
labels = {node: node for node in G.nodes}
nx.draw(G, with_labels=True, labels=labels, node_size=3000, node_color="skyblue", font_size=10, font_weight="bold", edge_color="gray")
plt.title("Conceptual Flowchart of Large-Scale Machine Learning Pipeline")
plt.show()
