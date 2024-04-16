def in_sort(a):
    for i in range(1,len(a)):
        b=i
        while b>0 and a[b] <  a[b-1]:
            a[b],a[b-1]=a[b-1],a[b]
            b-=1
    return array


array=[3,5,8,1,2]
print(in_sort(array))