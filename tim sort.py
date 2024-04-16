def merge(a, lower_bound, mid, upper_bound):
    i = lower_bound
    j = mid + 1
    k = lower_bound
    new_array = []

    while i <= mid and j <= upper_bound:
        if a[i] < a[j]:
            new_array.append(a[i])
            i += 1
        else:
            new_array.append(a[j])
            j += 1
        k += 1

    while i <= mid:
        new_array.append(a[i])
        i += 1
        k += 1

    while j <= upper_bound:
        new_array.append(a[j])
        j += 1
        k += 1

    # Copy sorted elements back to the original array
    for i in range(lower_bound, k):
        a[i] = new_array[i - lower_bound]


def merge_sort(a, lower_bound, upper_bound):
    if lower_bound < upper_bound:
        mid = (lower_bound + upper_bound) // 2
        merge_sort(a, lower_bound, mid)
        merge_sort(a, mid + 1, upper_bound)
        merge(a, lower_bound, mid, upper_bound)

def in_sort(a):
    for i in range(1,len(a)):
        b=i
        while b>0 and a[b] <  a[b-1]:
            a[b],a[b-1]=a[b-1],a[b]
            b-=1
    return a
arr=[17,6,10,5,9,2,1,15,17]
mid=len(arr)//2
arr1=arr[:mid]
part1=in_sort(arr1)
arr2=arr[mid:]
part2=in_sort(arr2)
print(part1)
print(part2)
arr23=part1+part2
lower_bound = 0
upper_bound = len(arr23) - 1
merge_sort(arr23, lower_bound, upper_bound)
print("Sorted array:", arr23)
