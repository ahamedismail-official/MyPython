string_array = ['amaama']
sentence=string_array[0]
print(sentence)
a=len(sentence)
mid=a//2
part_1=sentence[0:mid]
part_2=sentence[mid:]
if part_1 == part_2:
    print("the entered String ia aSymmetrical")
else:
    print("the entered string is not symmetrical")
def isPalindrome(sentence):
	return sentence == sentence[::-1]
ans = isPalindrome(sentence)
if ans:
	print("The entered String is Palindrome")
else:
	print("The entered String is not a Palindrome")


