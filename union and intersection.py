a= []
n = int(input("Enter number of elements : "))
for i in range(0, n):
	ele = int(input())
	a.append(ele)
print(a)
b= []
n = int(input("Enter number of elements : "))
for i in range(0, n):
	ele2 = int(input())
	b.append(ele2)
print(b)
c=a+b
print(c)
myset = set(c)
a_set = set(a)
b_set = set(b)
if (a_set & b_set):
    d=a_set & b_set
print("union= ",len(myset))
print("intersection",len(d))
