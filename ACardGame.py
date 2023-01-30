length = int(input())
nums = list(map(int,input().split()))
 
wube = 0
Henok = 0
ptr1 = 0
ptr2 = length - 1
 
if length % 2 == 0:
    while ptr1 < ptr2:
        if nums[ptr1] < nums[ptr2]:
            wube += nums[ptr2]
            ptr2 -= 1
        else:
            wube += nums[ptr1]
            ptr1 += 1
 
        if ptr1 <= ptr2 and nums[ptr1] < nums[ptr2]:
            Henok += nums[ptr2]
            ptr2 -= 1
        elif ptr1 <= ptr2:
            Henok += nums[ptr1]
            ptr1 += 1
    print(wube, end = " ")
    print(Henok)
else:
    while ptr1 <= ptr2:
        if nums[ptr1] < nums[ptr2]:
            wube += nums[ptr2]
            ptr2 -= 1
        else:
            wube += nums[ptr1]
            ptr1 += 1
 
        if ptr1 <= ptr2 and nums[ptr1] < nums[ptr2]:
            Henok += nums[ptr2]
            ptr2 -= 1
        elif ptr1 <= ptr2:
            Henok += nums[ptr1]
            ptr1 += 1
    print(wube, end = " ")
    print(Henok)
