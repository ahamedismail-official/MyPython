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


arr = [15, 5, 24, 8, 1, 3, 16, 10, 20]
lower_bound = 0
upper_bound = len(arr) - 1
merge_sort(arr, lower_bound, upper_bound)
print("Sorted array:", arr)
