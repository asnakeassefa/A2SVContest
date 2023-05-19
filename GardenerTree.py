from collections import defaultdict,deque

total = int(input())
for _ in range(total):
    input()
    length, k = map(int,input().split())
    graph= defaultdict(set)
    indeg = [0] * length

    for _ in range(length-1):
        node1,node2 = map(int,input().split())
        graph[node1].add(node2)
        graph[node2].add(node1)
        indeg[node1-1] += 1
        indeg[node2-1] += 1

    
    queue = deque()
    count = 0
    visited = set()
    popped = 0
    for i,val in enumerate(indeg):
        if val <= 1:
            popped += 1
            queue.append(i)
            visited.add(i)
    
    count = 1
    while queue:
        if count >= k:
            break
        queueLength = len(queue)

        for _ in range(queueLength):
            node = queue.popleft()
            for val in graph[node+1]:
                if val-1 not in visited:
                    indeg[val-1] -= 1
                    if indeg[val-1] <= 1:
                        popped += 1
                        queue.append(val-1)
                        visited.add(val-1)
                
        count += 1
    
    if length - popped > 0:
        print(length-popped)
    else:
        print(0)