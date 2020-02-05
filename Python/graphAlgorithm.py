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

     
