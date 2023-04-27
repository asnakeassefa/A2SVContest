num = int(input())
ans = 0
while num > 2:
    ans += num & 1
    num >>= 1
print(ans+1)