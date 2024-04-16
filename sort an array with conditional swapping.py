arr = [5,4,1,3,2,1]
f = False
if len(arr) % 2 == 0:
    for i in range(0, len(arr) - 1, 1):
        if abs(arr[i] - arr[i + 1] == 1):
            f = True
        else:
            f = False
if f:
    print('yes')
else:
    print('no')
