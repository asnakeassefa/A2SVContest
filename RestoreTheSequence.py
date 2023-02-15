total = int(input())

for _ in range(total):
    length = int(input())
    nums = list(map(int,input().split()))
    ptr1 = 0
    ptr2 = length -1
    ans = []
    while ptr1 <= ptr2:
        ans.append(nums[ptr1])
        if ptr1 != ptr2:
            ans.append(nums[ptr2])
        ptr1 += 1
        ptr2 -= 1
    print(*ans)
