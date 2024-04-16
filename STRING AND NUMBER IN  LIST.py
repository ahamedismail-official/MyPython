n=input()
m=n.split()
al=0
num=0
for i in n:
    if (i >='a' and i<='z') or (i >='A' and i<='Z'):
        al+=1
    if i in ('0','1','2','3','4','5','6','7','8','9'):
        num+=1
print(al,num)
if al >=1 and num >=1:
    print("True")
else:
    print(False)