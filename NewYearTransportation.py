n,t = map(int,input().split())

nums = list(map(int,input().split()))

num = 1
ans = False
while num < n:
    if num == t:
        ans = True
        break
    if num >= len(nums)+1:
        break
    num += nums[num-1]

if num == t:
    ans = True

if ans:
    print("YES")
else:
    print("NO")