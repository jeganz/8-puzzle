# states={
#     'a':[
#         [2, 8, 3],
#         [1, 6, 4],
#         [7, 0, 5]
#     ],
#     'b':[
#         [2, 8, 3],
#         [1, 6, 4],
#         [0, 7, 5]
#     ],
#     'c':[
#         [2, 8, 3],
#         [1, 0, 4],
#         [7, 6, 5]
#     ],
#     'd':[
#         [2, 8, 3],
#         [1, 6, 4],
#         [7, 5, 0]
#     ],
#     'e':[
#         [2, 8, 3],
#         [0, 1, 4],
#         [7, 6, 5]
#     ],
#     'f':[
#         [2, 0, 3],
#         [1, 8, 4],
#         [7, 6, 5]
#     ],
#     'g':[
#         [2, 8, 3],
#         [1, 4, 0],
#         [7, 6, 5]
#     ],
#     'h':[
#         [0, 8, 3],
#         [2, 1, 4],
#         [7, 6, 5]
#     ],
#     'i':[
#         [2, 8, 3],
#         [7, 1, 4],
#         [0, 6, 5]
#     ],
#     'j':[
#         [0, 2, 3],
#         [1, 8, 4],
#         [7, 6, 5]
#     ],
#     'k':[
#         [2, 3, 0],
#         [1, 8, 4],
#         [7, 6, 5]
#     ],
#     'l':[
#         [1, 2, 3],
#         [0, 8, 4],
#         [7, 6, 5]
#     ],
#     'm':[
#         [1, 2, 3],
#         [8, 0, 4],
#         [7, 6, 5]
#     ],
#     'n':[
#         [1, 2, 3],
#         [7, 8, 4],
#         [0, 6, 5]
#     ],
# }
# graph={
#     'a': [('b', 1), ('c', 1),('d', 1)],
#     'b': [],
#     'c': [('e', 2), ('f', 2),('g', 2)],
#     'd': [],
#     'e': [('h', 3), ('i', 3)],
#     'f': [('j', 3), ('k', 3)],
#     'g': [],
#     'h': [],
#     'i': [],
#     'j': [('l', 4)],
#     'k': [],
#     'l': [ ('m', 5),('n', 5)],
#     'm': [],
#     'n': [],
# }
states={
    '1':[
        [2, 8, 3],
        [1, 6, 4],
        [7, 0, 5]
    ],
}

statecount=1
start='1'
stop=[
        [1, 2, 3],
        [8, 0, 4],
        [7, 6, 5]
    ]
def heuristic(n):
    h_dist=0
    m=states[n]
    s=stop
    for i in range(3):
        for j in range(3):
            if m[i][j]!=s[i][j]:
                h_dist+=1
    return h_dist
def aStarAlgo(start_node, stop_node):
    open_set = set(start_node)
    closed_set = set()
    g = {}               #store distance from starting node
    parents = {}         # parents contains an adjacency map of all nodes
    g[start_node] = 0
    parents[start_node] = start_node
    while len(open_set) > 0:
        n = -1
        for v in open_set:
            if (n == -1 or (g[v] + heuristic(v) < g[n] + heuristic(n))):
                n = v
        if states[n] == stop_node:
            pass
        else:
            for (m, weight) in get_neighbors(n,g[n]):
                if m not in open_set and m not in closed_set:
                    open_set.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight
                #for each node m,compare its distance from start i.e g(m) to the
                #from start through n node
                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n
                        if m in closed_set:
                            closed_set.remove(m)
                            open_set.add(m)
        if n == -1:
            print('Path does not exist!')
            return None

        # if the current node is the stop_node then we begin reconstructin the path from it to the start_node
        if states[n] == stop_node:
            path = []
            while parents[n] != n:
                path.append(n)
                n = parents[n]
            path.append(start_node)
            path.reverse()
            print('Path found:')
            return path
        open_set.remove(n)
        closed_set.add(n)



import copy

def get_neighbors(m,w):
    global statecount
    m=states[m]
    l = []
    x, y = 0, 0
    f = 0
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] == 0:
                x, y = i, j
                f = 1
                break
        if f == 1:
            break

    if y - 1 >= 0:
        new_matrix = copy.deepcopy(m)
        new_matrix[x][y], new_matrix[x][y - 1] = new_matrix[x][y - 1], new_matrix[x][y]
        if new_matrix not in list(states.values()):
            statecount+=1
            node=str(statecount+1)
            states[node]=new_matrix
            l.append((node,w+1))

    if y + 1 <= 2:
        new_matrix = copy.deepcopy(m)
        new_matrix[x][y], new_matrix[x][y + 1] = new_matrix[x][y + 1], new_matrix[x][y]
        if new_matrix not in list(states.values()):
            statecount+=1
            node=str(statecount+1)
            states[node]=new_matrix
            l.append((node,w+1))

    if x - 1 >= 0:
        new_matrix = copy.deepcopy(m)
        new_matrix[x - 1][y], new_matrix[x][y] = new_matrix[x][y], new_matrix[x - 1][y]
        if new_matrix not in list(states.values()):
            statecount+=1
            node=str(statecount+1)
            states[node]=new_matrix
            l.append((node,w+1))

    if x + 1 <= 2:
        new_matrix = copy.deepcopy(m)
        new_matrix[x + 1][y], new_matrix[x][y] = new_matrix[x][y], new_matrix[x + 1][y]
        if new_matrix not in list(states.values()):
            statecount+=1
            node=str(statecount+1)
            states[node]=new_matrix
            l.append((node,w+1))
    print(l)
    return l
    
def printMat(m):
    for i in m:
        for j in i:
            print(j,' ',end='')
        print()

#tree n path cost from user
a=aStarAlgo(start,stop)
sol=[]
for i in a:
    sol.append(states[i])
    printMat(states[i])
    print()
print(sol)