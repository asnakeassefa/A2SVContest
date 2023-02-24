length = int(input())

num = list(map(int,input().split()))

ptr = 1
ans = 1
temp = 1
while ptr < length:
    if num[ptr-1] <= num[ptr]:
        temp += 1
    else:
        ans = max(ans,temp)
        temp = 1
    ptr += 1
ans = max(ans,temp)
print(ans)
