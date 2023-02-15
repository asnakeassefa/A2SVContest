boyslen = int(input())
boys = list(map(int,input().split()))
girlslen = int(input())
girls = list(map(int,input().split()))

boys.sort()
girls.sort()

ptr1 = 0
ptr2 = 0
ans = 0
while ptr1 < boyslen and ptr2 < girlslen:
    if abs(boys[ptr1] - girls[ptr2]) <= 1:
        ans += 1
        ptr1 += 1
        ptr2 += 1
    elif boys[ptr1] > girls[ptr2] and boys[ptr1] - girls[ptr2] >= 2:
        ptr2 += 1
    elif boys[ptr1] < girls[ptr2] and girls[ptr2] - boys[ptr1] >= 2:
        ptr1 += 1

print(ans)
