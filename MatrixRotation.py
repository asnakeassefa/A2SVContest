total = int(input())

for _ in range(total):
    num1 = list(map(int,input().split()))
    num2 = list(map(int,input().split()))
    res = False
    for i in range(4):
        if num1[0] < num2[0] and num1[0] < num1[1] and num1[1]<num2[1] and num2[0] < num2[1]:
            res = True
            break
        else:
            temp = num1[0]
            num1[0] = num2[0]
            num2[0] = num2[1]
            num2[1] = num1[1]
            num1[1] = temp
            
    if res:
        print("YES")
    else:
        print("NO")
