class Solution:
    def inbound(self,mat,row,col):
        return 0<= row<len(mat) and 0<=col<len(mat[0])
    
    def bfs(self,mat,queue,visited,ans):
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        count = 0
        while queue:
            count += 1
            length = len(queue)
            for _ in range(length):
                cell = queue.popleft()
                for row,col in directions:
                    x = cell[0] + row
                    y = cell[1] + col
                    if (x,y) not in visited and self.inbound(mat,x,y):
                        queue.append([x,y])
                        visited.add((x,y))
                        ans[x][y] = count
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        visited = set()
        queue = deque()
        ans = [[0] * len(mat[0]) for i in range(len(mat))]
        print(ans)
        for i,rowVal in enumerate(mat):
            for j,colVal in enumerate(rowVal):
                if colVal == 0:
                    visited.add((i,j))
                    queue.append([i,j])
        self.bfs(mat,queue,visited,ans)
        return ans