from collections import deque




def inbound(row,col,grids):
    return 0<= row<len(grids) and 0<= col <len(grids[0])

def bfs(mat,visited):
    directions = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,1),(1,-1),(-1,-1)]
    queue =deque([(0,0)])
    while queue:
        cell = queue.popleft()
        for row,col in directions:
            x = cell[0] + row
            y = cell[1] + col
            if (x,y) == (1,len(mat[0])-1):
                return "YES"
            if (x,y) not in visited and inbound(x,y,mat):
                queue.append((x,y))
                visited.add((x,y))
    return "NO"

total = int(input())

for i in range(total):
    n = int(input())
    grid = []
    temp = []
    value = input()
    visited1 = set()
    for i,val in enumerate(value):
        temp.append(int(val))
        if int(val) == 1:
            visited1.add((0,i))
    grid.append(temp[:])
    temp = []
    value  = input()
    for i,val in enumerate(value):
        if int(val) == 1:
            visited1.add((1,i))
        temp.append(int(val))
    grid.append(temp[:])

    print(bfs(grid,visited1))