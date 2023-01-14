Total = int(input())
 
for _ in range(Total):
	rectangle1 = list(map(int,input().split()))
	rectangle2 = list(map(int,input().split()))
 
	rectangle1.sort()
	rectangle2.sort()
 
	if rectangle1[1] == rectangle2[1] and rectangle1[0] + rectangle2[0] == rectangle1[1]:
		print("Yes")
	else:
		print("No")
