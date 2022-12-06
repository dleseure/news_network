#   from pyvis.network import Network
import pyvis
from pyvis.network import Network
import pandas as pd
#   import os

#   Define work folder
#   os.chdir("E:\\Work1\\Network_project\\test_data")

got_net = Network(height="2000px", width="100%", bgcolor="#222222", font_color="white")

# set the physics layout of the network
got_net.barnes_hut()
got_data = pd.read_csv("g2_scores.csv")

sources = str(got_data['source'])
targets = str(got_data['target'])
weights = str(got_data['weight'])

edge_data = zip(sources, targets, weights)

for e in edge_data: 
    src = e[0]
    dst = e[1]
    w = e[2]

    got_net.add_node(src, src, title=src)
    got_net.add_node(dst, dst, title=dst)
    got_net.add_edge(src, dst, value=w)

neighbor_map = got_net.get_adj_list()

# add neighbor data to node hover data
for node in got_net.nodes:
    node["title"] += " Neighbors:<br>" + "<br>".join(neighbor_map[node["id"]])
    node["value"] = len(neighbor_map[node["id"]])

got_net.show("g_scores.html")