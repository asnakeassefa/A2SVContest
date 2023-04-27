

Range = int(input())
newArray = [i%2 for i in range(Range + 2)]

newArray[1] = 0
newArray[2] = 1

d = 3
while d * d <= (Range + 1):
    j = d
    while d * j <= (Range + 1):
        if newArray[d*j]:
            newArray[d*j] = 0
        j += 1
    d += 2
newArray = newArray[2:]
for i in range(2,Range):
    if not newArray[i]:
        newArray[i] = 2

print(len(set(newArray)))
print(*newArray)