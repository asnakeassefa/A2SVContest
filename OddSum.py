total = int(input())

nums = list(map(int,input().split()))
newNums = set(nums)

if len(newNums) > 1:
    nums.sort()
    print(*nums)
else:
    print(-1)
