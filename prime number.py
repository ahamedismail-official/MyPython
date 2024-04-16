li=list(map(int,input().split()))
prime=[]
count = 0
for i in li:
    c=0
    for j in range(1,i):
        if i % j == 0:
            c+=1
    if c==1:
         prime.append(i)
c=prime
print(len(c))
print(sum(c))
