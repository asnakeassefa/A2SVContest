number = input()
# number = "900"
ans = ""
for i,num in enumerate(number):
    if i == 0 and 9-int(num) == 0:
        ans += num
    else:
        ans += str(min(9-int(num),int(num)))
ans = int(ans)
print(ans)
