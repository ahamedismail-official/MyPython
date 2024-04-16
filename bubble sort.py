li=list(map(int,input().split()))
c=0
for i in range(len(li)-1):
    for j in range(len(li)-1-i):
        c+=1
        if li[j]>li[j+1]:
            li[j],li[j+1]=li[j+1],li[j]
print(li)
print(c)