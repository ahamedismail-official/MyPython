a= []
n = int(input("Enter number of elements : "))
for i in range(0, n-1):
	ele = int(input())
	a.append(ele)
for i in range(1,n+1):
    if i not in a:
        print("the missing elements is",i)
