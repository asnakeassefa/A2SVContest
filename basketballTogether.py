total,target = map(int,input().split())
nums = list(map(int,input().split()))
nums.sort()

counter = 0
last = total - 1
ans = 0
num = 0
for i in range(total):
    num += nums[last]
    if num > target:
        total -= 1
        ans += 1
        last -= 1
        num = 0
print(ans)
