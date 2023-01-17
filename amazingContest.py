Total = int(input())

records = list(map(int,input().split()))

amazing = 0
for i in range(1,Total):
    val = records[:i]
    val.sort()
    if records[i] > val[-1]:
        amazing += 1
    elif records[i] < val[0]:
        amazing += 1
print(amazing)
