from collections import defaultdict


total = int(input())

for _ in range(total):
    v, E = map(int, input().split())
    graph = defaultdict(list)
    ans = defaultdict(int)
    x = 0
    y = 0
    for _ in range(E):
        val1,val2 = map(int , input().split())
        graph[val1].append(val2)
        graph[val2].append(val1)

    for value in graph.values():
        ans[len(value)] += 1
    if len(ans) == 2:
        for key,val in ans.items():
           if key != 1:
               x = key
               y = key - 1
    elif len(ans) == 3:
        for key,val in ans.items():
            if val == 1:
                x = key
            if key != 1  and val != 1:
                y = key-1
    
    print(x,y)