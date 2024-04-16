s = input()
if len(s) <= 2:
    print(s)
elif s[len(s) - 3:len(s)] == "ing":
    s += "ly"
    print(s)
else:
    s += "ing"
    print(s)
