string_array = ['geeksforgeeks is the best for geeks']
char_list = ['e', 'b', 'g', 'f']

sentence = string_array[0]
print(sentence)
count = {}
for i in sentence:
    if i in char_list:
        if i in count:
            count[i] += 1

        else:
            count[i] = 1

print(count)
sorted_dic=dict(sorted(count.items(),key=lambda a:a[1]))
print(sorted_dic)
