import sys


def my_range(n: int):
    print("My_range starts")
    start = 0
    while start < n:
        print('my range is returning %d' % start)
        yield start
        start += 1


big_range = my_range(5)

print("big_range is {} bytes".format(sys.getsizeof(big_range)))

#  Create a list contains all the values in big_range

big_list = []
for val in big_range:
    big_list.append(val)


print("big_list is {} bytes".format(sys.getsizeof(big_list)))
