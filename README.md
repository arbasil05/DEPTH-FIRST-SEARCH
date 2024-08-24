# BREADTH-FIRST-SEARCH

## ExpNo 3: Implement Breadth First Search Traversal of a Graph

### Name: Abdur Rahman Basil A H
### Register Number: 212223040002

### Aim:
To Implement Breadth First Search Traversal of a Graph using Python 3.

### Theory:
Breadth-First Traversal (or Search) for a graph is similar to the Breadth-First Traversal of a tree. The only catch here is that, unlike trees, graphs may contain cycles, so we may come to the same node again. To avoid processing a node more than once, we divide the vertices into two categories:
1. Visited
2. Not Visited

A Boolean visited array is used to mark the visited vertices. For simplicity, it is assumed that all vertices are reachable from the starting vertex. BFS uses a queue data structure for traversal.

**How does BFS work?**  
Starting from the root, all the nodes at a particular level are visited first, and then the next level nodes are traversed until all the nodes are visited.  
To do this, a queue is used. All the adjacent unvisited nodes of the current level are pushed into the queue, and the current-level nodes are marked visited and popped from the queue.

**Illustration:**  
Let us understand the working of the algorithm with the help of the following example.

**Step1:** Initially, queue and visited arrays are empty.

**Step2:** Push node 0 into the queue and mark it visited.

**Step 3:** Remove node 0 from the front of the queue, visit the unvisited neighbors, and push them into the queue.

**Step 4:** Remove node 1 from the front of the queue, visit the unvisited neighbors, and push them into the queue.

**Step 5:** Remove node 2 from the front of the queue, visit the unvisited neighbors, and push them into the queue.

**Step 6:** Remove node 3 from the front of the queue, visit the unvisited neighbors, and push them into the queue.  
As we can see, every neighbor of node 3 is visited, so move to the next node that is at the front of the queue.

**Step 7:** Remove node 4 from the front of the queue, visit the unvisited neighbors, and push them into the queue.  
As we can see, every neighbor of node 4 is visited, so move to the next node that is at the front of the queue.  
Now, the queue becomes empty, so terminate this process of iteration.

### Algorithm:
1. Construct a Graph with Nodes and Edges.
2. Breadth First Search uses a Queue and iterates through the Queue for Traversal.
3. Insert a Start Node into the Queue.
4. Find its Successors or neighbors and check whether the node is visited or not.
5. If not visited, add it to the Queue. Else, continue.
6. Iterate steps 4 and 5 until all nodes are visited, and there are no more unvisited nodes.

### Program:
```python
from collections import deque
from collections import defaultdict

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
```
<h3>Sample Input</h3>
<hr>
7 9 <BR>
A B <BR>
A C <BR>
A F <BR>
C E <BR>
C F <BR>
C D <BR>
D E <BR>
D G <BR>
G F <BR>
<hr>
<h3>Sample Output</h3>
<hr>
['A', 'B', 'C', 'F', 'E', 'D', 'G']

<hr>

<hr>
<h3>Sample Input</h3>
<hr>
5 6 <BR>
0 1 <BR>
0 2 <BR>
1 2 <BR>
1 3 <BR>
2 4 <BR>
3 4 <BR>
<hr>
<h3>Sample Output</h3>
<hr>
['0', '1', '2', '3', '4']
<hr>
<h3>Result:</h3>
['A', 'B', 'C', 'F', 'E', 'D', 'G']
<hr>
<p>Thus,a Graph was constructed and implementation of Breadth First Search for the same graph was done successfully.</p>
