class UnionFind:
    def __init__(self, n):
        self.rep = {i:i for i in range(n+1)}
        self.size = {i:1 for i in range(n+1)}
    def find(self, x):
        stack = [x]
        while x != self.rep[x]:
            x = self.rep[x]
            stack.append(self.rep[x])
        
        while stack:
            self.rep[stack.pop()] = x
        return x
    def union(self, x, y):
        xrep = self.find(x)
        yrep = self.find(y)

        if xrep == yrep:
            return
        if self.size[xrep] > self.size[yrep]:
            self.rep[yrep] = xrep
            self.size[xrep] += self.size[yrep]
        else:
            self.rep[xrep] = yrep
            self.size[yrep] += self.size[xrep]
    def findSize(self,x):
        return self.size[self.find(x)]
    def connected(self, x, y):
        return self.find(x) == self.find(y)
    
total ,nextinput = map(int,input().split())

UF = UnionFind(total)

for _ in range(nextinput):
    nums = list(map(int,input().split()))
    length = nums[0]
    for i in range(2,length+1):
        UF.union(nums[1],nums[i])
ans = []
for i in range(1,total+1):
    ans.append(UF.findSize(i))

print(*ans)