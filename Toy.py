from collections import defaultdict

n,m = map(int,input().split())

prices = list(map(int,input().split()))

prices.sort()

toys = defaultdict(int)

for i in range(m):
    toys[input()] += 1

nums = []
for val in toys.values():
    nums.append(val)

nums.sort(reverse = True)
ans = 0
for i in range(len(nums)):
    ans += (prices[i] * nums[i])
res = []
res.append(ans)
ans = 0
for i in range(len(nums)):
    ans += (prices[-(i+1)] * nums[i])
res.append(ans)
print(*res)
