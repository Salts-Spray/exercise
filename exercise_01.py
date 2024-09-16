# def count_alphabets(s):
#     alphabet = set('abcdefghijklmnopqrstuvwxyz')
#     string_s = set(s)
#
#     return alphabet.issubset(string_s)
#


count_alpha = lambda s: set('abcdefghijklmnopqrstuvwxyz').issubset(set(s))

input_str = 'abcds@@#efghijklmnopqrstuvwxy'

print(count_alpha(input_str))