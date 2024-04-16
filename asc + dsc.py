list=[10,12,4,8,34,23,26,78,90]
n=len(list)
a=n//2
part1=list[0:a]
d=len(part1)
part2=list[a:]
e=len(part2)
for i in range (d):
    for j in range(i + 1,d):
        if(part1[i] > part1[j]):
            temp = part1[i]
            part1[i] = part1[j]
            part1[j] = temp
print(part1)
for i in range (e):
    for j in range(i + 1,e):
        if(part2[j] > part2[i]):
            temp = part2[i]
            part2[i] = part2[j]
            part2[j] = temp
print(part2)