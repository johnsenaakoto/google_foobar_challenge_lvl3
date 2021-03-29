def solution(maze):
    w, h = len(maze[0]), len(maze)
    num_el = w * h
    
    min_dist = 1000
    
    for m in all_maps(maze):
        g_maze = buildGraph(m)
        min_dist = min(ShortestDistance(g_maze, 0, (num_el - 1), num_el), min_dist)
        
        if min_dist == w + h - 1:
            return min_dist+1
    
    return min_dist+1

# source and dest
def add_edge(adj, src, dest):
 
    adj[src].append(dest)
    adj[dest].append(src) 
    

#   builds graph from maze
def buildGraph(maze):
    
    rows = len(maze)
    cols = len(maze[0])
    
    board = [[0 for _ in range(cols)] for _ in range(rows)]
    
    counter = 0
    for i in range(rows):
        for j in range(cols):
            board[i][j] = counter;
            counter += 1
    
    # number of vertices in graph
    v = rows * cols
    graph = [[] for i in range(v)];
    
    
    for i in range(rows):
        for j in range(cols):
            node = board[i][j]
            
            if not(maze[i][j]):
            
                # make all possible node connections
                row = [1, -1, 0, 0]
                col = [0, 0, -1, 1]
                loc_row = [r + i for r in row]
                loc_col = [c + j for c in col]
                
                for n in range(4):
                    if (loc_row[n] >= 0 and loc_row[n] < rows) and (loc_col[n] >= 0 and loc_col[n] < cols):
                        neighbor = board[loc_row[n]][loc_col[n]]
                        if not(maze[loc_row[n]][loc_col[n]]):
                            add_edge(graph, node, neighbor)
    return(graph)

   
#   Breadth First Search
def BFS(adj, src, dest, v, pred, dist):
 
    # a queue to maintain queue of vertices whose
    # adjacency list is to be scanned as per normal
    # DFS algorithm
    queue = []
  
    # boolean array visited[] which stores the
    # information whether ith vertex is reached
    # at least once in the Breadth first search
    visited = [False for i in range(v)]
  
    # initially all vertices are unvisited
    # so v[i] for all i is false
    # and as no path is yet constructed
    # dist[i] for all i set to infinity
    for i in range(v):
 
        dist[i] = 1000000
        pred[i] = -1
     
    # now source is first to be visited and
    # distance from source to itself should be 0
    visited[src] = True
    dist[src] = 0
    queue.append(src)
  
    # standard BFS algorithm
    while (len(queue) != 0):
        u = queue[0]
        queue.pop(0)
        for i in range(len(adj[u])):
         
            if (visited[adj[u][i]] == False):
                visited[adj[u][i]] = True
                dist[adj[u][i]] = dist[u] + 1
                pred[adj[u][i]] = u
                queue.append(adj[u][i])
  
                # We stop BFS when we find
                # destination.
                if (adj[u][i] == dest):
                    return True
  
    return False;



#   Finds the shortest distance between a source tile and a destination tile
def ShortestDistance(adj, s, dest, v):
     
    # predecessor[i] array stores predecessor of
    # i and distance array stores distance of i
    # from s
    pred=[0 for i in range(v)]
    dist=[0 for i in range(v)]
  
    if (BFS(adj, s, dest, v, pred, dist) == False):
        i=0
  
    # vector path stores the shortest path
    path = []
    crawl = dest
    crawl = dest
    path.append(crawl)
     
    while (pred[crawl] != -1):
        path.append(pred[crawl])
        crawl = pred[crawl]
     
    # distance from source is in distance array
    return(dist[dest])

#Iterator for maze modifications
def all_maps(maze):
    
    yield maze
    
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j]:
                copy = [[col for col in row] for row in maze]
                copy[i][j] = 0
                yield copy
                

'''maze = [[0, 1, 1, 0], 
        [0, 0, 0, 1], 
        [1, 1, 0, 0], 
        [1, 1, 1, 0],]#Answer 7'''

'''maze = [[0, 0, 0, 0, 0],
        [1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1],
        [0, 0, 0, 0, 0]] #Answer 17'''

'''maze = [[0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 1],
        [0, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0]] #Answer 21'''
    
maze = [[0, 0, 0, 0, 0, 0], 
        [1, 1, 1, 1, 1, 0], 
        [0, 0, 0, 0, 0, 0], 
        [0, 1, 1, 1, 1, 1], 
        [0, 1, 1, 1, 1, 1], 
        [0, 0, 0, 0, 0, 0]]

    
print(solution(maze))
