total = int(input())

for _ in range(total):
    base,num = map(int,input().split())
    i = 0
    ans = 0
    while num:
        ans += (base ** i) * (num & 1)
        num >>= 1
        i += 1
    print(ans%((10 ** 9) + 7))