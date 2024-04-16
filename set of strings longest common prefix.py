def longest_common_prefix(strings):
    if not strings:
        return ""
    strings.sort()
    first_string = strings[0]
    last_string = strings[-1]
    common_prefix = []
    for i in range(len(first_string)):
        if i < len(last_string) and first_string[i] == last_string[i]:
            common_prefix.append(first_string[i])
        else:
            break
    return "".join(common_prefix)


string_set = ["geeksforgeeks", "geeks", "geek", "geezer"]
result = longest_common_prefix(string_set)
print("Longest Common Prefix:", result)
