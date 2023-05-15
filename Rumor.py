from collections import defaultdict, deque
import heapq

n,m = map(int, input().split())
golds = list(map(int,input().split()))
store = defaultdict(list)

for _ in range(m):
    x,k = map(int,input().split())
    store[x].append(k)
    store[k].append(x)

visited = set()
queue  = deque()

ans = 0
for i in range(1,n+1):
    if  i not in visited:
        queue.append(i)
        Min_val = golds[i-1]
        while queue:
            node = queue.popleft()
            visited.add(node)
            Min_val = min(Min_val, golds[node-1])
            for val in store[node]:
                if val not in visited:
                    queue.append(val)
        ans += Min_val
print(ans)