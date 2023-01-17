
values = list(map(int,input().split()))
remain = 0
if abs(values[0] - values[1]) > 0:
    remain = 1
ans = 2*(min(values[0],values[1])) + (2 * values[2]) + remain

print(ans)
