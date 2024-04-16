arr=[1,20,6,4,5]
c=0
for i in range (len(arr)):
    for j in range(i+1,len(arr)):
        if i <j and arr[i]>arr[j]:
            c+=1
        else:
            continue
print(c)