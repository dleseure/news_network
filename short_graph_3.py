''' short_graph_2.py

    Takes data from a small number of articles obtained via Newscatcher
    and produces a directed graph based on comparison of every pair
    of articles.  Direction is determined by the published date:
    from the earlier article to the later article.  The size of the edge
    is determined by how similar the two articles are: 1 meaning
    they are identical, 0 meaning they are not simiar
'''
from pyvis.network import Network
import pandas as pd
# import os

#   Define work folder
# os.chdir("E:\\Work1\\Network_project\\test_data")

got_net = Network(height="2500px", width="100%", directed=True,     \
                  bgcolor="#222222", font_color="white")

# set the physics layout of the network
got_net.barnes_hut(central_gravity=0.8)
got_data = pd.read_csv("top_scores_2.csv")

sources = got_data['source']
targets = got_data['target']
weights = got_data['weight']

edge_data = zip(sources, targets, weights)

for e in edge_data:
    src = e[0]
    dst = e[1]
    w = e[2]
    got_net.add_node(src, src, title=src)
    got_net.add_node(dst, dst, title=dst)
    got_net.add_edge(src, dst, value=w, arrowStrikethrough=False)

neighbor_map = got_net.get_adj_list()

# add neighbor data to node hover data
for node in got_net.nodes:
    node["title"] += " Neighbors:<br>" + "<br>".join(neighbor_map[node["id"]])
    node["value"] = len(neighbor_map[node["id"]])

got_net.show("top_scores_2.html")
