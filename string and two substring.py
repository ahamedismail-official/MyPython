string1 = "Gfg is best for geeks and cs"
sub1 = "is"
sub2 = "and"
list1 = list(string1.split())
print(list1)
x = list1.index(sub1)
y = list1.index(sub2)
print(x)
print(y)
final = (list1[x + 1:y])
end = ' '.join(final)
print(end)
# ANOTHER METHOD
print(''.join(string1.split(sub1)[1].split(sub2)[0]).strip())
