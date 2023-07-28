total = int(input())

num1 = list(map(int,input().split()))
num2 = list(map(int,input().split()))

num1.sort()
num2.sort()
length = len(num1)
score = 0

while num1:
    num = num1.pop()
    if num <= num2[-1]:
        score += 1
        num2.pop()
if score > length//2:
    print("YES")
else:
    print('NO')