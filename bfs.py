from collections import deque
from collections import defaultdict

'''
Input example:
V E
FOR EVERY EDGE
U V
7 9
A B
A C
A F
C E
C F
C D
D E
D G
G F
'''

def bfs(graph, start, visited, path):
    queue = deque()
    path.append(start) 
    queue.append(start)  
    visited[start] = True  
    
    while len(queue) != 0:
        tmpnode = queue.popleft()  
        
    
        for neighbour in graph[tmpnode]:
            if not visited[neighbour]: 
                queue.append(neighbour)  
                visited[neighbour] = True  
                path.append(neighbour) 
    
    return path


graph = defaultdict(list)

v, e = map(int, input().split())


for i in range(e):
    u, v = input().split() 
    graph[u].append(v) 
    graph[v].append(u)  


start = 'A'

path = []
visited = defaultdict(bool)

traversed_path = bfs(graph, start, visited, path)


print(traversed_path)
