def dijkstra(graph,src,dest,visited,distances,predecessors):
    """ calculates a shortest path tree routed in src
    """    
    # a few sanity checks
    if src not in graph:
        raise TypeError('the root of the shortest path tree cannot be found in the graph')
    if dest not in graph:
        raise TypeError('the target of the shortest path cannot be found in the graph')    
    # ending condition
    if src == dest:
        # We build the shortest path and display it
        if dest not in distances:
            distances[dest] = 0
        path=[]
        pred=dest
        while pred != None:
            path.append(pred)
            pred=predecessors.get(pred,None)
        pathList = []
        pathList.append(str(path))
        pathList.append(distances[dest])
        return pathList

    else :     
        # if it is the initial  run, initializes the cost
        if not visited: 
            distances[src]=0
        # visit the neighbors
        for neighbor in graph[src] :
            if neighbor not in visited:
                new_distance = distances[src] + graph[src][neighbor]
                if new_distance < distances.get(neighbor,float('inf')):
                    distances[neighbor] = new_distance
                    predecessors[neighbor] = src
        # mark as visited
        visited.append(src)
        # now that all neighbors have been visited: recurse                         
        # select the non visited node with lowest distance 'x'
        # run Dijskstra with src='x'
        unvisited={}
        for k in graph:
            if k not in visited:
                unvisited[k] = distances.get(k,float('inf'))        
        x=min(unvisited, key=unvisited.get)
        return dijkstra(graph,x,dest,visited,distances,predecessors)
        


if __name__ == "__main__":
	import sys
	import itertools
	
	graph = {
	'cope': {'cope': 0, 'gun': 11, 'admin': 12, 'handi': 15},
        'gun': {'cope': 11, 'gun': 0, 'eco': 2, 'admin': 3.5, 'handi': 5.7, 'fivea': .5},
        'eco': {'gun': 2, 'eco': 0, 'skills': 1, 'health': 1.9, 'admin': 3, 'fivea': 1.8, 'five': .6},
        'skills': {'eco': 1, 'skills': 0, 'health': 1.4, 'dan': 3.7, 'five': 2.2, 'six': .7, 'seven': .6},
        'archery': {'archery': 0, 'fivea': 2, 'five': 1.9, 'six': 1, 'seven': 2.1},
	'health': {'eco': 1.9, 'skills': 1.4, 'health': 0, 'admin': 2, 'dining': 2.3, 'aqua': 4.1, 'dan': 4.4, 'seven': 2.3},
        'admin': {'cope': 12, 'gun': 3.5, 'eco': 3, 'health': 2, 'admin': 0, 'dining': 1, 'handi': 2.8, 'four': 2.4},
	'dining': {'health': 2.3, 'admin': 1, 'dining': 0, 'aqua': 2.6, 'handi': 2.7, 'four': 1.8},
	'aqua': {'health': 4.1, 'dining': 2.6, 'aqua': 0, 'handi': 3.01},
	'handi': {'cope': 15, 'gun': 5.7, 'admin': 2.8, 'dining': 2.7, 'aqua': 3.01, 'handi': 0, 'two': 1.4, 'three': 1, 'four': .5},
	'dan': {'skills': 3.7, 'health': 4.4, 'dan': 0, 'ftown': 1.7, 'seven': .8, 'bunk': 1, 'eight': 2.2},
	'ftown': {'dan': 1.7, 'ftown': 0, 'bunk': 1.8, 'eight': 1.7, 'nine': 1.9},
	'kiwanis': {'ftown': 1.2, 'kiwanis': 0, 'nine': 1.7, 'ten': 1.8},
	'one': {'one': 0, 'two': 1, 'fourteen': 300},
	'two': {'handi': 1.4, 'one': 1, 'two': 0, 'three': .7},
	'three': {'handi': 1, 'two': .7, 'three': 0},
	'four': {'admin': 2.4, 'dining': 1.8, 'handi': .5, 'four': 0},
	'fivea': {'gun': .5, 'eco': 1.8, 'archery': 2, 'fivea': 0, 'five': .4},
	'five': {'eco': .6, 'skills': 2.2, 'archery': 1.9, 'fivea': .4, 'five': 0},
	'six': {'skills': .7, 'archery': 1, 'six': 0, 'seven': 2},
	'seven': {'skills': .6, 'archery': 2.1, 'health': 2.3, 'dan': .8, 'six': 2, 'seven': 0},
	'bunk': {'dan': 1, 'ftown': 1.8, 'bunk': 0, 'eight': .3},
	'eight': {'dan': 2.2, 'ftown': 1.7, 'bunk': .3, 'eight': 0},
	'nine': {'ftown': 1.9, 'kiwanis': 1.7, 'nine': 0},
	'ten': {'kiwanis': 1.8, 'ten': 0, 'eleven': 2.6, 'twelve': 6},
	'eleven': {'ten': 2.6, 'eleven': 0, 'twelve': 2.5, 'thirteen': 5.5},
	'twelve': {'ten': 6, 'eleven': 2.5, 'twelve': 0},
	'thirteen': {'eleven': 5.5, 'thirteen': 0, 'fourteen': 2},
	'fourteen': {'one': 300, 'thirteen': 2, 'fourteen': 0}}
	
	campSite = sys.argv[1]
	badge1 = sys.argv[2]
	badge2 = sys.argv[3]
	badge3 = sys.argv[4]
	badge4 = sys.argv[5]
	badge5 = sys.argv[6]
	badge6 = sys.argv[7]
	badgeList = [badge1, badge2, badge3, badge4, badge5, badge6]
	newBadgeList = []
	for t in itertools.permutations(badgeList, 6):
		l = list(t)
		l.insert(0, 'dining')
		l.insert(0, campSite)
		l.insert(5, 'dining')
		l.append(campSite)
		newBadgeList.append(l)

	shortList = []
	shortLength = 9999

	for i in newBadgeList:
		length = 0
		j = 0
		for j in range(0, len(i) - 1):
			pathList = dijkstra(graph, i[j], i[j + 1], [], {}, {})
			length += pathList[1]
		if length < shortLength:
			shortLength = length
			shortList = i
	shortLength = round(shortLength, 1)	

	print(str(shortList) + '\n' + str(shortLength))
