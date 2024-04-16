def quicksort(arr):
	if len(arr) <= 1:
		return arr
	else:
		pivot = arr[0]
		left = [x for x in arr[1:] if x < pivot]
		right = [x for x in arr[1:] if x >= pivot]
		return quicksort(left) + [pivot] + quicksort(right)
arr1=[2,1,2,5,7,1,9,3,6,8,8]
arr2=[2,1,8,3]
sorted_arr = quicksort(arr1)
a=[]
print("Sorted Array in Ascending Order:")
print(sorted_arr)
for i in range(len(arr2)):
    for j in range(len(arr1)):
        if arr2[i]== arr1[j]:
            a.append(arr1[j])
a2=[]
for i in range(len(arr1)):
    if arr1[i] not in a:
        a2.append(arr1[i])
print(a)
print(a2)
sorte=quicksort(a2)
print((sorte))
result=a+sorte
print(result)
