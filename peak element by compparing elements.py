arr=list(map(int,input().split()))
n=len(arr)
print(n)
for i in range(1,n-1):
    if(arr[i]>arr[i+1] and arr[i] >arr[i-1]):
        i%2!=0
        print("odd elements"+arr[i])
for i in range(1,n-1):
    if(arr[i]>arr[i+1] and arr[i] >arr[i-1]):
        i%2==0
        print("even elements"+arr[i])
