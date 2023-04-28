class Solution:
    def bfs(self,target):
        visited = set((0,1))
        queue = deque([(0,1)])
        count = 0
        while queue:
            length = len(queue)

            for _ in range(length):
                vertice = queue.popleft()
                if vertice[0] == target:
                    return count
                val = (vertice[0] + vertice[1])
                speed = (vertice[1]) * 2

                if (val,speed) not in visited and val > -1:
                    queue.append((val,speed))
                    visited.add((val,speed))

                val = vertice[0]
                if vertice[1] > 0:
                    speed = -1
                else:
                    speed = 1
                if (val,speed) not in visited and val > -1:
                    queue.append((val,speed))
                    visited.add((val,speed))
            count +=1
            
    def racecar(self, target: int) -> int:
        return self.bfs(target)