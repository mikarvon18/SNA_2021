import matplotlib.pyplot as plt
import networkx as nx
import pickle
import collections
import numpy as np
import powerlaw


#with open ('data-May-20-2021--00-20__5-5-5-2-5.txt', 'rb') as fp:
#    list_of_all = pickle.load(fp)

#with open ('data-May-20-2021--19-02__5-5-3-5-5.txt', 'rb') as fp:
#    list_of_all = pickle.load(fp)

with open ('data-May-20-2021--13-03__10-10-10-10-10.txt', 'rb') as fp:
    list_of_all = pickle.load(fp)



#labels = {}
digraph = True



G = nx.DiGraph()
Gn = nx.Graph()


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


for num, top_subreddit in enumerate(top_subreddits):
	for linked_subreddits in list_of_all:
		if top_subreddit[0] == linked_subreddits[0]:
			if linked_subreddits[1] not in target_list[num]:
				target_list[num].append(linked_subreddits[1])



for num, top_subreddit in enumerate(target_list):
	for linked_subreddits in list_of_all:
		#print(linked_subreddits)
		spoint = linked_subreddits[1]
		epoint = linked_subreddits[2]
		#print(f"top_subreddit[0]: {top_subreddit[0]} --- linked_subreddits[0]: {linked_subreddits[0]}, epoint: {epoint}, top_subreddit[num]: {top_subreddit[num]}")
		if top_subreddit[0] == linked_subreddits[0] and epoint in top_subreddit:
			G.add_edge(spoint, epoint)
			Gn.add_edge(spoint, epoint)


def getAverage(lista):
	totalnum = 0
	for i in lista:
		totalnum += i[1]
	return (totalnum / len(lista))
def getAverageDict(lista):
	#print(f"len of lista: {len(lista)}")
	totalnum = 0
	for i in [*lista.values()]:
		totalnum += i
	return (totalnum / len(lista))

def calculateVariance(lista):
	lst = []
	for i in lista:
		lst.append(i[1])
	return np.var(lst)

def calculateVarianceDict(lista):
	lst = []
	for i in [*lista.values()]:
		lst.append(i)
	return np.var(lst)

print(f"Total number of edges (before cleaning the data): {len(list_of_all)}")
print(f"Total number of edges: {G.number_of_edges()}")
print(f"Total number of nodes: {G.number_of_nodes()}")
print()
	
in_degree = G.in_degree()
#print(in_degree)
print(f"AVERAGE IN DEGREE: {getAverage(in_degree)}")
print(f"VARIANCE OF IN DEGREE: {calculateVariance(in_degree)}")
print()

in_degree_centrality = nx.in_degree_centrality(G)
print(f"AVERAGE IN DEGREE CENTRALITY: {getAverageDict(in_degree_centrality)}")
print(f"VARIANCE IN DEGREE CENTRALITY: {calculateVarianceDict(in_degree_centrality)}")
print()

out_degree = G.out_degree()
print(f"AVERAGE OUT DEGREE: {getAverage(out_degree)}")
print(f"VARIANCE OF OUT DEGREE: {calculateVariance(out_degree)}")
print()

out_degree_centrality = nx.out_degree_centrality(G)
print(f"AVERAGE OUT DEGREE CENTRALITY: {getAverageDict(out_degree_centrality)}")
print(f"VARIANCE OUT DEGREE CENTRALITY: {calculateVarianceDict(out_degree_centrality)}")
print()

betweenness_centrality = nx.betweenness_centrality(G)
print(f"AVERAGE BETWEENNESS CENTRALITY: {getAverageDict(betweenness_centrality)}")
print(f"VARIANCE OF BETWEENNESS CENTRALITY: {calculateVarianceDict(betweenness_centrality)}")
print()

closeness_centrality = nx.closeness_centrality(G)
print(f"AVERAGE CLOSENESS CENTRALITY: {getAverageDict(closeness_centrality)}")
print(f"VARIANCE OF CLOSENESS CENTRALITY: {calculateVarianceDict(closeness_centrality)}")
print()

print(f"AVERAGE CLUSTERING COEFFICIENT: {nx.average_clustering(G)}")
clustering = nx.clustering(G)
print()
#print(clustering)

	


#print(f"LENGTH OF WHOLE LIST: {len(list_of_all)}")
print(f"NUMBER OF CONNECTED COMPONENTS: {nx.number_connected_components(Gn)}")
Gcc = Gn.subgraph(sorted(nx.connected_components(Gn), key=len, reverse=True)[0])
print(f"SIZE OF GIANT COMPONENT: {len(Gcc)}")
print(f"DIAMETER OF GIANT COMPONENT: {nx.diameter(Gcc)}")
#Gcc = G.subgraph(sorted(nx.connected_components(G), key=len, reverse=True)[0])
#print(Gcc)
#nx.draw(G, font_size=16, with_labels=True, edge_color='gray', width=0.5)

#nx.draw(Gcc, font_size=16, with_labels=True, edge_color='gray', width=0.5)
#plt.show()



#*********************

#DRAWING THE HISTOGRAM

#*********************
degree_sequence = sorted([d for n, d in G.in_degree()], reverse=True)  # degree sequence
degreeCount = collections.Counter(degree_sequence)
deg, cnt = zip(*degreeCount.items())

fig, ax = plt.subplots()
plt.bar(deg, cnt, width=0.80, color="b")

plt.title("In Degree Histogram")
plt.ylabel("Count")
plt.xlabel("In Degree")
ax.set_xticks([d + 0.4 for d in deg])
ax.set_xticklabels(deg)

# draw graph in inset
plt.axes([0.4, 0.4, 0.5, 0.5])
#Gcc = G.subgraph(sorted(nx.connected_components(G), key=len, reverse=True)[0])
pos = nx.spring_layout(G)
plt.axis("off")

#APPLY LOGARITHMIC SCALE
#ax.set_yscale('log')
#ax.set_xscale('log')
nx.draw_networkx_nodes(G, pos, node_size=20)
nx.draw_networkx_labels(G, pos)
nx.draw_networkx_edges(G, pos, alpha=0.4)
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
