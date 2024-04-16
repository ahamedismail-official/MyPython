li=[100,180,260,310,40,535,695]
n=len(li)
profit=0
initial=li[0]
for i in range(1,n):
    if(li[i]>initial):
        profit=max(profit,li[i]-initial)
    else:
        initial =li[i]
        final=profit
final=final+profit
print(final)

