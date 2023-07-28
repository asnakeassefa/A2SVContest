import heapq

total = int(input())

num1= list(map(int,input().split()))
num2 = list(map(int,input().split()))
for i in range(total):
    num2[i] = -num2[i]
num1.sort(reverse=True)
heapq.heapify(num2)
ans = 0
i = 0
length = len(num1)
for num in num1:
    if num > -num2[0]:
        ans += 1
        heapq.heappush(num2,-num)
    else:
        heapq.heappop(num2)

print(ans)