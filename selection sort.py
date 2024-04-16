li=list(map(int,input().split()))
for i in range(0,len(li)-1):
    min=i
    for j in range(i+1,len(li)):
        if li[j]<li[min]:
            min=j
    if i!=  min:
        li[i],li[min]=li[min],li[i]
print(li)