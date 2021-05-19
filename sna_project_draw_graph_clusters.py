import matplotlib.pyplot as plt
import networkx as nx
import pickle
import collections


with open ('data-May-20-2021--00-20__5-5-5-2-5.txt', 'rb') as fp:
    list_of_all = pickle.load(fp)

labels = {}

G = nx.DiGraph()


#print(list_of_all)

#list_of_all = [["mehu", "kakka", "kekkonen"], ["mehu", "kekkonen", "himpula"], ["juoma", "kasvi", "koira"]]

"""
for lista in linked_subreddits:
	for index, subreddit in enumerate(lista):
		if index > 0:
			spoint = str(lista[0])
			epoint = str(subreddit)
			G.add_edge(spoint, epoint)
"""
top_subreddits = [[]]
first_val = list_of_all[0][0]
#print("first", first_val)
top_subreddits[0].append(first_val)
top_subreddits.append([])
#print(top_subreddits)
i = 1
target_list_all = []
for linked_subreddits in list_of_all:
	if linked_subreddits[1] not in target_list_all:
		target_list_all.append(linked_subreddits[1])
	if linked_subreddits[0] != first_val:
		first_val = linked_subreddits[0]
		top_subreddits[i].append(first_val)
		top_subreddits.append([])
		
		i += 1
top_subreddits.pop()
target_list = list(top_subreddits)
#print(top_subreddits)
#print(target_list_all)

for num, top_subreddit in enumerate(top_subreddits):
	for linked_subreddits in list_of_all:
		if top_subreddit[0] == linked_subreddits[0]:
			if linked_subreddits[1] not in target_list[num]:
				target_list[num].append(linked_subreddits[1])


#print(target_list)
#print()
for i in list_of_all:
	print(i)

for num, top_subreddit in enumerate(target_list):
	for linked_subreddits in list_of_all:
		#print(linked_subreddits)
		spoint = linked_subreddits[1]
		epoint = linked_subreddits[2]
		#print(f"top_subreddit[0]: {top_subreddit[0]} --- linked_subreddits[0]: {linked_subreddits[0]}, epoint: {epoint}, top_subreddit[num]: {top_subreddit[num]}")
		if top_subreddit[0] == linked_subreddits[0] and epoint in top_subreddit:
			G.add_edge(spoint, epoint)
"""			
for linked_subreddits in list_of_all:
	spoint = linked_subreddits[1]
	epoint = linked_subreddits[2]
	if epoint in target_list:
		G.add_edge(spoint, epoint)
"""
#print(top_subreddits)
nx.draw_random(G, font_size=16, with_labels=True, edge_color='gray', width=0.5)
plt.show()

"""
for i in G.nodes():
	#print(G.degree[i])
	if G.degree[i] > 15:
		labels[i] = i
"""
"""
print(list(G.nodes()))

d = dict(G.degree)

#Gcc = G.subgraph(sorted(nx.connected_components(G), key=len, reverse=True)[0])
pos = nx.spring_layout(G)

nx.draw(G, pos, font_size=16, with_labels=False, edge_color='gray', width=0.5, node_size=[v * 10 for v in d.values()])
nx.draw_networkx_labels(G,pos,labels,font_size=16,font_color='r')
#nx.draw_networkx_edges(G, pos, alpha=0.4)
plt.show()
"""

#for i in G.nodes():
	#print(G.degree[i])
#	if G.degree[i] > 1:
#		node_list.append(i)
#print(node_list)
#G.remove_edges_from(list(G.edges))
#nx.draw_random(G, font_size=16, with_labels=True, edge_color='gray', width=0.5, node_size=[v * 100 for v in d.values()])
#for p in pos:  # raise text positions
#    pos[p][1] += 0.07
#nx.draw_networkx_labels(G, pos)
#plt.show()
