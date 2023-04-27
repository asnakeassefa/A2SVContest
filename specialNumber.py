total = int(input())

ans = 0

for _ in range(total):
    len = input()
    nums = list(map(int,input().split()))
    for i,num in enumerate(nums):
        temp = 0
        for j,num2 in enumerate(nums):
            if j == i:
                continue
            else:
                temp ^= num2
        if temp == num:
            ans = num
            break
    print(ans)