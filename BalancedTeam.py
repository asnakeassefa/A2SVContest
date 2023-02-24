length = int(input())

num = list(map(int,input().split()))

ans = 1
temp = 1
ptr1 = 0
ptr2 = 1

num.sort()
while ptr2 < length:
    if num[ptr2] - num[ptr1] <= 5:
        ptr2 += 1
        temp += 1
    else:
        ptr1 += 1
        temp -= 1
    ans = max(ans,temp)
print(ans)
