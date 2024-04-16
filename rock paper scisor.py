string=input()
st=0
ke=0
v='AEIOUaeiou'
i=0
while i<len(string):
        if string[i] in v:
            ke+=(len(string)-i)
        else:
            st+=(len(string)-i)
        i+=1
print(st,ke)
print("stuart wins" if st>ke else "kevin wins")