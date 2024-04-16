def partition(a,lb,ub):
    pivot=a[lb]
    start=lb
    end=ub
    while(start<=end):
        while a[start]<=pivot:
            start+=1
        while a[end]>pivot:
            end-=1
        if start<end:
            a[start], a[end] = a[end], a[start]
    a[end], a[lb] = a[lb], a[end]
    return end

def quick_sort(a,lb,ub):
    if lb<ub:
        loc = partition(a, lb, ub)
        quick_sort(a, lb, loc - 1)
        quick_sort(a, loc + 1, ub)

a=[7,6,10,5,9,2,1,15,17]
lb=0
ub=len(a)-1
quick_sort(a,lb,ub)
print(a)