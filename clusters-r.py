# -*- coding: utf-8 -*-
"""
Created on Sat May 05 12:45:00 2018

@author: Ksenia
"""

import json
import networkx as nx
import matplotlib.pyplot as plt

with open("test.json") as data_file:
    data=json.load(data_file, encoding="windows-1251")
    
for i in clustered:
    allChannels[i]['wc'] = clustered[i]['wc']
    allChannels[i]['le'] = clustered[i]['le']
    allChannels[i]['eb'] = clustered[i]['eb']
    
G = nx.DiGraph()
# add nodes from channels
for i in allChannels:
    if allChannels[i]['name'] == ' ':
        print('kek')
    G.add_node(allChannels[i]['name'], label=allChannels[i]['name'],
               title=allChannels[i]['name'], 
               subscribers=allChannels[i]['subscribers'],
               videos=allChannels[i]['videos'],
               views=allChannels[i]['views'],
               wc=allChannels[i]['wc'],
               le=allChannels[i]['le'],
               eb=allChannels[i]['eb'])

# create list of edges
names = []
for i in allChannels:
    name = allChannels[i]['name']
    names.append(name)
edges = []
for i in allChannels:
    try:
        related = allChannels[i]['playlistAuthors']
        for r in related:
            if r in names:
                if r != allChannels[i]['name']:
                    if r == '':
                        print 'here'
                    else:
                        pair = (allChannels[i]['name'], r)
                        edges.append(pair)
    except:
        pass

# add edges
G.add_edges_from(edges)

## dynamic
hypecamp_dates = data['hypecamp_dates']
dates_dict = {}
for date in hypecamp_dates:
    for c in hypecamp_dates[date]:
        if c in dates_dict:
            pass
        else:
            dates_dict[c] = date
nx.set_node_attributes(G, dates_dict, 'hypecampstart')  

veet1_dates = data['veet1_dates']
dates_dict = {}
for date in veet1_dates:
    for c in veet1_dates[date]:
        if c in dates_dict:
            pass
        else:
            dates_dict[c] = date
nx.set_node_attributes(G, dates_dict, 'veet1start')  

veet2_dates = data['veet2_dates']
dates_dict = {}
for date in veet2_dates:
    for c in veet2_dates[date]:
        if c in dates_dict:
            pass
        else:
            dates_dict[c] = date
nx.set_node_attributes(G, dates_dict, 'veet2start')  

versus_dates = data['versus_dates']
dates_dict = {}
for date in versus_dates:
    for c in versus_dates[date]:
        if c in dates_dict:
            pass
        else:
            dates_dict[c] = date
nx.set_node_attributes(G, dates_dict, 'versusstart') 

cola_dates = data['cola_dates']
dates_dict = {}
for date in cola_dates:
    for c in cola_dates[date]:
        if c in dates_dict:
            pass
        else:
            dates_dict[c] = date
nx.set_node_attributes(G, dates_dict, 'colastart')   

lizzka_dates = data['lizzka_dates']
dates_dict = {}
for date in lizzka_dates:
    for c in lizzka_dates[date]:
        if c in dates_dict:
            pass
        else:
            dates_dict[c] = date
nx.set_node_attributes(G, dates_dict, 'lizzkastart')  

blockers_dates = data['blockers_dates']
dates_dict = {}
for date in blockers_dates:
    for c in blockers_dates[date]:
        if c in dates_dict:
            pass
        else:
            dates_dict[c] = date
nx.set_node_attributes(G, dates_dict, 'blockersstart')  

rostar_dates = data['rostar_dates']
dates_dict = {}
for date in rostar_dates:
    for c in rostar_dates[date]:
        if c in dates_dict:
            pass
        else:
            dates_dict[c] = date
nx.set_node_attributes(G, dates_dict, 'rostarstart')

klinsky_dates = data['klinsky_dates']
dates_dict = {}
for date in klinsky_dates:
    for c in klinsky_dates[date]:
        if c in dates_dict:
            pass
        else:
            dates_dict[c] = date
nx.set_node_attributes(G, dates_dict, 'klinskystart')    

# write to gexf
nx.write_gexf(G, "final.gexf", encoding="utf-8")
