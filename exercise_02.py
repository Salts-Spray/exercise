def find_peek(test):
    n = len(test)

    if n == 0:
        return None
    if n == 1:
        return test[0]

    peaks = []

    if test[0] > test[1]:
        peaks.append(test[0])

    for i in range(1, n-1):
        if test[i] > test[i - 1] and test[i] > test[i + 1]:
            peaks.append(test[i])

    if test[n - 1] > test[n -2]:
        peaks.append(test[n-1])

    if peaks:
        return max(peaks)
    else:
        return None

test_input = [1, 2, 9, 4, 5, 8, 10]
print(find_peek(test_input))
