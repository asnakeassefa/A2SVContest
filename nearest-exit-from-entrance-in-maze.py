class Solution:
    def inbound(self,x,y,grid):
        return 0<=x<len(grid) and 0<=y<len(grid[0])
    def bfs(self,maze,visited,entrance):
        queue = deque([entrance])
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        count = 0
        while queue:
            length = len(queue)
            count += 1
            for _ in range(length):
                node = queue.popleft()
                for row,col in directions:
                    x = row + node[0]
                    y = col + node[1]
                    if self.inbound(x,y,maze) and (x,y) not in visited and maze[x][y] == ".":
                        if x == 0 or y == 0 or x == len(maze)-1 or y == len(maze[0])-1:
                            return count
                    if (x,y) not in visited and self.inbound(x,y,maze) and maze[x][y] == ".":
                        queue.append([x,y])
                        visited.add((x,y))
        return -1
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        visited = set()
        visited.add(tuple(entrance))
        return self.bfs(maze,visited,entrance)