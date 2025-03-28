

def findSumMinDistance(times, n, k):

    ## define an array of distance to each node
    dist_arr = [-1] * (n + 1)

    ## build an adjcancy graph out of the times array
    adjacancy_list = [None] * (n + 1)

    for edge in times:
        if not adjacancy_list[edge[0]]:
            adjacancy_list[edge[0]] = []
        adjacancy_list[edge[0]].append((edge[1], edge[2]))

    print(adjacancy_list)
    ##return sum of minimum  time to each node

    adjacancy_list[0] = []
    ## the source node k is being appended
    adjacancy_list[0].append(k)
    dist_arr[k] = 0
    sum = 0
    while len(adjacancy_list[0]) > 0:
        curr_node = adjacancy_list[0].pop(0)
        print(curr_node)
        ## were saying its visited here
        # dist_arr[curr_node] = 0
        if not adjacancy_list[curr_node]:
            continue

        for edge in adjacancy_list[curr_node]:
            print(curr_node ,edge)
            
            if dist_arr[edge[0]] == -1:
                dist_arr[edge[0]] = dist_arr[curr_node] + edge[1]
                adjacancy_list[0].append(edge[0])
        
        ## the distance to each in node in the directed graph
        ## the index is the key of node
        print(adjacancy_list[0])
    print(dist_arr)

    return max(dist_arr[1:])



findSumMinDistance([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 1)
findSumMinDistance([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 3)
print(findSumMinDistance([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2))
# Hao Mack Yang ⚙.
# Snapshot
# Mic
# Cam
# Share
# Snapshot
# Chat
# Today
# Hao Mack Yang ⚙.06:49 PM
# empty_graph[edge[0]].append(edge[1], edge[2])
# The graph is not directly implemented. It is implemented as an adjacency list and auxiliary array
# empty_graph[0] = []
# empty_graph[0].append(k)
# dist_arr[k] = 0
# u.pop(0)
# cur_node = empty_graph[0].pop(0)
# dist[cur_node] = 0
# if not adjacency_list[curr_node]
# for edge in adjacency_list[curr_node]:
# empty_graph[0].append(edge[0])
# dist_arr[k] = edge[1]