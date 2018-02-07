def communitySplits(graph, weight=None):
		"""
		Compute the splits for the formation of communities.

		Parameters
		----------
		graph -  A networkx graph of digraph.
		weight (string) - If None, all edge weights are considered equal.
			Otherwise holds the name of the edge attribute used as weight


		Returns
		-------
		The graph with weak edges removed.


		Usage
		-----
		>>> G = nx.path_graph(10)
		>>> out = GirvanNewman(G)
		>>> comm = out.communities(G, weight=None)
		>>> for x in comm:
				print x
		"""

		nConnComp = nx.number_connected_components(graph)
		nComm = nConnComp

		while (nComm <= nConnComp):
			betweenness = nx.edge_betweenness_centrality(graph, weight=weight)
			if (len(betweenness.values()) != 0 ):
				max_betweenness = max(betweenness.values())
			else:
				break
			for u,v in betweenness.iteritems():
				if float(v) == max_betweenness:
					# print u,v
					graph.remove_edge(u[0], u[1])
			nComm = nx.number_connected_components(graph)
		return graph