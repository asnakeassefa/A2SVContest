from collections import defaultdict

total = int(input())

for _ in range(total):
    length, cost = map(int,input().split())

    nums = list(map(int,input().split()))

    orbits = defaultdict(int)
    for num in nums:
        orbits[num] += 1
    
    ans = 0
    for value in orbits.values():
        ans += min(value,cost)

    print(ans)