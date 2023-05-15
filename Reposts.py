from collections import defaultdict, deque

total = int(input())
values = defaultdict(list)
for _ in range(total):
    inValue =list(map(str, input().split(" ")))
    values[inValue[2].lower()] .append(inValue[0].lower())

mainqueue = deque(["polycarp"])

def bfs(queue):
    visited = set(queue)
    count = 0
    while queue:
        count += 1
        length = len(queue)
        for _ in range(length):
            val = queue.popleft()
            reports = values[val]
            for report in reports:
                if report not in visited:
                    queue.append(report)
                    visited.add(report)
    return count
print(bfs(mainqueue))