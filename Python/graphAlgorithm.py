from collections import deque
graph = {}
graph['you'] = ['alice','bob','jam']
graph['alice'] = ['david','jack','rose']
graph['bob'] = ['tom','tompson','rick']
graph['jam'] = ['lee','jay']
graph['david'] = ['mac','nick']
graph['jack'] = ['ruby']
graph['rose'] = ['tom','lee']
graph['tom'] = ['litter']
graph['tompson'] = ['ray']
graph['rick'] = ['nee']
graph['lee'] = []
graph['jay'] = []

def person_is_mongo(name):
    return name[0] == "m"

def search(name):
    search_deque = deque()
    search_deque += graph[name]
    searched = []
    while search_deque:
        person = search_deque.popleft()
        if person not in searched:
            if person_is_mongo(person):
                print(person + "is a mongo businessman")
                return True 
            else:
                searched.append(person)
                search_deque += graph[person]
    return None 

# ====================================== #
# =========Dijkstra algorithm=========== #
# ====================================== #
graph = {}
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2
graph["a"] = {}
graph["a"]["final"] = 1
graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["final"] = 5
graph["final"] = {}
infinity = float("inf")
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["final"] = infinity 
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["final"] = None 
proceesed = []
def find_lowest_cost_nodes(costs):
    lowest_cost = infinity 
    lowest_cost_node =None 
    for node in costs: 
        cost = costs[node] 
        if cost < lowest_cost and node is not proceesed: 
            lowest_cost = cost 
            lowest_cost_node = node 
    return lowest_cost_node 

node = find_lowest_cost_nodes(costs)
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost 
            parents[n] = node 
    proceesed.append(node) 
    node = find_lowest_cost_nodes(costs)


