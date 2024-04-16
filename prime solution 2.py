arr=list(map(int,input().split()))
count=0
sum=0
for num in arr:
    if num>1:
        flag= True
        for i in range(2,int(num/2)+1):
            if num%i==0:
                flag= False
                break
        if flag ==True:
            count+=1
            sum+=num
print(count)
print(sum)