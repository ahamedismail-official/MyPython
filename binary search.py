def binary(low,high):
    while (low <= high):
        mid = (low + high) // 2
        if (x == array[mid]):
            return mid
        elif array[mid]>x:
            high = mid -1
        else:
            low=mid +1
    return false
array = list(map(int,input().split()))
x = int(input("enter the element to be searched: "))
low=0
high=len(array)-1
result=binary(low,high)
print(result)