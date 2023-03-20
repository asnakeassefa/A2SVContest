nums = input()
ans = ""
for i,num in enumerate(nums):
    if i == 0 and num == "9":
        ans += "9"
    elif 9 - int(num) < int(num):
        ans += str(9-int(num))
    else:
        ans += num

print(int(ans))