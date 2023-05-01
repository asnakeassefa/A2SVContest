class Solution:
    def DFS(self,bombs,currBomb,visited,ans):
        if currBomb in visited:
            return
        visited.add(currBomb)
        for bomb in bombs[currBomb]:
            if bomb not in visited:
                self.DFS(bombs,bomb,visited,ans)
                ans[0] += 1
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        ans = 1
        temp = 0
        detonated = defaultdict(list)
        for i,currBomb in enumerate(bombs):
            for j,bomb in enumerate(bombs):
                if i != j:
                    x = (currBomb[0] - bomb[0]) ** 2
                    y = (currBomb[1]- bomb[1]) ** 2
                    if (sqrt(x+y)) <= currBomb[2]:
                        detonated[(tuple(currBomb),i)].append((tuple(bomb),j))
        
        for i,currBomb in enumerate(bombs):
            temp = [1]
            self.DFS(detonated,(tuple(currBomb),i),set(),temp)
            ans = max(ans,temp[0])
        return ans