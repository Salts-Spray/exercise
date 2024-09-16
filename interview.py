# aabbbccccaaaaa
# a2b3c4a5
def count_strings(s):
    test = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            test.append(s[i-1] + str(count))
            count = 1

    test.append(s[-1] + str(count))

    return ''.join(test)

teststr = 'aabbbccccaaaaa'
print(count_strings(teststr))