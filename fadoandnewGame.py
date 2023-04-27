
n,m,k = map(int,input().split())
nums = []
for i in range(m+1):
    nums.append(int(input()))
num = nums[-1]
ans = 0
for i in range(m):
    xor = nums[i] ^ num
    temp = 0
    while xor:
        if xor & 1:
            temp += 1
        xor >>= 1
    if temp <= k:
        ans += 1
print(ans)