import gzip
import tarfile
from StringIO import StringIO
from os.path import exists

from os import listdir
from urllib import urlopen

import networkx as nx
import numpy as np
import pandas as pd


#url = 'http://snap.stanford.edu/data/facebook_combined.txt.gz'
url = 'https://github.com/AllenDowney/ThinkComplexity2/blob/master/code/facebook_combined.txt.gz?raw=true'
inmemory = StringIO(urlopen(url).read())
with gzip.GzipFile(fileobj=inmemory, mode='rb') as f:
    G = nx.read_edgelist(f, nodetype=int)
    L = len(G.edges())
    N = len(G.nodes())
    print "Number of vertices N =  ", N, "\nNumber of edges L = ", L

if not exists("facebook"):
    try:
        url_fb_data = 'http://snap.stanford.edu/data/facebook.tar.gz'
        stream_fb_data = urlopen(url_fb_data)
        with tarfile.open(fileobj=stream_fb_data, mode='r|gz') as tar:
            tar.extractall(path='.')
    except Exception as e:
        print "Error: ", str(e)

for filename in listdir("facebook"):
    if filename.endswith(".edges"):
        content = pd.read_csv(filepath_or_buffer="facebook/" + filename,
                              delim_whitespace=True, names=['start_node', 'end_node'])
        print "Ego-network of user ", filename.split('.')[0]
        print "Number of edges: ", content.shape[0]
        print "Number of nodes: ", len(set(np.unique(content["start_node"])).union(
            set(np.unique(content['end_node'])))), "\n"
        # with open("facebook/" +filename) as f:
