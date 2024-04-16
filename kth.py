arr=[1 , 2 ,3 , 4 , 5]
k=2
for i in range(-1,-k,-1):
    temp = arr[1]
    for j in range(1,len(arr)-1):
        arr[j+1] = arr[j]
    arr[1] = temp
print(arr)
