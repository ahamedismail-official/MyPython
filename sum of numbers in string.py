
s = "4pwor2aasta6"
numbers = []
for char in s:
    if char.isdigit():
        numbers.append(int(char))
print(sum(numbers))
