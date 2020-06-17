import random

def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    min_num = None
    max_num = None

    for num in ints:
        if min_num is None:
            min_num = num
            max_num = num

        if num < min_num:
            min_num = num
        elif num > max_num:
            max_num = num

    return min_num, max_num


# Example Test Case of Ten Integers
l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

# Negative numbers
l = [i for i in range(-30, 1)]  # a list containing -30 - 0
random.shuffle(l)

print("Pass" if ((-30, 0) == get_min_max(l)) else "Fail")

# All negative numbers
l = [i for i in range(-30, 0)]  # a list containing -30 - -1
random.shuffle(l)

print("Pass" if ((-30, -1) == get_min_max(l)) else "Fail")

# same number
l = [i for i in [0, 0]]  # a list containing 0 - 0
random.shuffle(l)

print("Pass" if ((0, 0) == get_min_max(l)) else "Fail")
