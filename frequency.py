array=[2,5,2,8,5,6,8,8]
count={}
for i in range(len(array)):
    if array[i] in count:
        count[array[i]]+=1
    else:
        count[array[i]]=1
print(count)
sorted_dic=dict(sorted(count.items(),key=lambda a:a[1],reverse=True))
print(sorted_dic)
for i in sorted_dic.keys():
    for k in range(sorted_dic[i]):
        print(i,end=" ")