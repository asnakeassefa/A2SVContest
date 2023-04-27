total = int(input())

for _ in range(total):
    length, x = map(int,input().split())

    nums = list(map(int,input().split()))

    ans = x * (x+1) // 2
    for num in nums:
        if num <= x:
            ans -= (num*2)
    print(ans)