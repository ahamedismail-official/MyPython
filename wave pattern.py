arr=[10,5,6,3,2,20,100,80]
for i in range(1,len(arr)-1,1):
    if arr[i]<arr[i-1] and arr[i]>arr[i+1]:
        arr[i],arr[i+1]=arr[i+1],arr[i]
print(arr)