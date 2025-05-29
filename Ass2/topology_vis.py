import yaml
import networkx as nx
import matplotlib.pyplot as plt

# Load inventory YAML
with open('/Users/eric/projects/mit/mn521/Ass2/inventory.yaml') as f:
    inventory = yaml.safe_load(f)

G = nx.Graph()

# Add nodes by group
for group in inventory['all']['children']:
    for node in inventory['all']['children'][group]['hosts']:
        G.add_node(node, group=group)

# Add links (example, customize as needed)
links = [
    ('core1', 'agg1'), ('core1', 'agg2'),
    ('core2', 'agg1'), ('core2', 'agg2'),
    ('agg1', 'acc1'), ('agg2', 'acc2'),
    ('acc1', 'srv1'), ('acc1', 'srv2'),
    ('acc2', 'srv3'), ('acc2', 'srv4')
]
G.add_edges_from(links)

# Draw
colors = {'core':'red', 'aggregation':'orange', 'access':'blue', 'servers':'green'}
node_colors = [colors[G.nodes[n]['group']] for n in G.nodes]
nx.draw(G, with_labels=True, node_color=node_colors, node_size=1500, font_size=10)
plt.savefig('datacenter_topology.png')
plt.show()