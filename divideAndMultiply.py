total = int(input())

for _ in range(total):
    length = int(input())
    nums = list(map(int,input().split()))
    two = 1
    newlist = [0] * length
    for i,num in enumerate(nums):
        d = 1
        while d * d <= num:
            j = 2
            while num % j == 0:
                two *= j
                num//=j
            j += 1
            d += 1
        newlist[i] = num
    Max = max(newlist)
    Sum = sum(newlist) - Max
    ans = Max * two
    ans += Sum
    print(ans)