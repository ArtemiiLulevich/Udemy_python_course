# def avr_word_len(*words):
#     mean = 0
#     for word in words:
#         mean += len(word)
#     return mean / len(words)
#
#
# def min_max(*args):
#     print("max: {}".format(max(args)))
#     print("min: {}".format(min(args)))
#
#
# def reverse_tuple(*args):
#     return args[::-1]
#
#
# def tuple_list(*args):
#     return list(args)
#
#
# print(avr_word_len("lol", 'ball', 'us3'))
# print(min_max(1, 3, 45, 76, 23, 2))
# print(reverse_tuple(2, 5, 6, 7))
# print(tuple_list(1, 45, 7, 8, 9, 4))


# def print_backwards(*args, end=' ', **kwargs):
#     print(kwargs)
#     for word in args[::-1]:
#         print(word[::-1], end=end, **kwargs)

def print_backwards(*args, end=' ', **kwargs):
    end_character = kwargs.pop('end', '\n')
    sep_character = kwargs.pop('sep', ' ')

    for word in args[:0:-1]:
        print(word[::-1], end=sep_character, **kwargs)
    print(args[0][::-1], end=end_character, **kwargs)
    # print(end_character)

# with open("backwards.txt", 'w') as backwards:
#     print_backwards('hello', 'planet', 'earth', 'take', 'me', 'to', 'your', 'leader', end='\t', file=backwards)


print('hello', 'planet', 'earth', 'take', 'me', 'to', 'your', 'leader', end='', sep='\n**\n')
print()
print_backwards('hello', 'planet', 'earth', 'take', 'me', 'to', 'your', 'leader', end='', sep='\n**\n')
