class UnionFind:
    def __init__(self):
        self.rep = {chr(ord('a')+i):chr(ord('a')+i) for i in range(27)}
    
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
        if self.rep[xrep] < self.rep[yrep]:
            self.rep[yrep] = xrep
        else:
            self.rep[xrep] = yrep
        
    def connected(self, x, y):
        return self.find(x) == self.find(y)

length = int(input())

word1 = input()
word2 = input()

UF = UnionFind()
ans = []
for i in range(length):
    if not UF.connected(word1[i],word2[i]):
        ans.append((word1[i],word2[i]))
        UF.union(word2[i],word1[i])

print(len(ans))
for val in ans:
    print(*val)