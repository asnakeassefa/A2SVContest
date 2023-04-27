from collections import defaultdict


total = int(input())

nums = list(map(int,input().split()))
adj = defaultdict(int)

for i,num in enumerate(nums):
    adj[(i,num)] = ((num-1,nums[num-1]))

visited = set()
ans = "NO"

newList = [key for key,val in adj.items()]

# print(adj)
for num in newList:
    secNum = adj[num]
    sectwo = adj[secNum]
    if adj[sectwo] == num:
        ans = "YES"
        break

print(ans)