import requests
import networkx as nx
import matplotlib.pyplot as plt
import json
import sys
api = 'https://banks.data.fdic.gov/api'

endpoint = '/institutions'


params = {'filters': 'ACTIVE:1',
          'sort_by':'STNAME',
          'fields': 'NAME,ADDRESS,CITY,STNAME,COUNTY,ZIP,STCNTY,LATITUDE,LONGITUDE,ACTIVE',
          'limit':250
          }
        #   'sort by':'STNAME'}

response = requests.get(api+endpoint, params=params,)

data = response.json()['data']


# print(data)
# sys.exit(-1)
# first_name = data[0]['data']['NAME']

# print(first_name)

G = nx.DiGraph()


# banks_by_state = {}

for line in data:
    bank_name = line['data']['NAME']
    branch_name = f"{line['data']['CITY']}, {line['data']['STNAME']}"
    state_name = line['data']['STNAME']  

    G.add_node(bank_name, type='bank')
    # G.add_node(branch_name, type='branch', state=state_name) 
    G.add_edge(bank_name, state_name)





    # state_name = line['data']['STNAME']
    # bank_name = line['data']['NAME']

    # if state_name not in G:
    #     G.add_node(state_name, type='state')
    #     banks_by_state[state_name] = set()

    # # Add the bank as a node and create an edge to the state node
    # G.add_node(bank_name, type='bank')
    # G.add_edge(state_name, bank_name)
    # banks_by_state[state_name].add(bank_name)






    # bank_name = line['data']['NAME']
    # branch_name = f"{line['data']['CITY']}, {line['data']['STNAME']}"
    # state_name = line['data']['STNAME']  

    # G.add_node(bank_name, type='bank')
    # G.add_node(branch_name, type='branch', state=state_name) 
    # G.add_edge(bank_name, branch_name)



pos = nx.spring_layout(G, seed=42)
plt.figure(figsize=(10, 8))
nx.draw(G, pos, with_labels=True, node_size=200, width =.5, font_size = 3,node_color='skyblue')
# plt.show()
nx.write_graphml(G,'banktest.graphml')