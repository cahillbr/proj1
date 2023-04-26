

import random
from static_array import *


# ------------------- PROBLEM 1 - MIN_MAX -----------------------------------

def min_max(arr: StaticArray) -> (int, int):
    """
    Computes the minimum and maximum values in a StaticArray.
    Returns a tuple containing two integers representing the minimum and maximum values
    in the input StaticArray, respectively.
    """
    minimum = arr.get(0)  # assigning values of arraw both min and max
    maximum = arr.get(0)
    for i in range(arr.length()):
        if arr.get(i) < minimum:  # scenarios for values if either is less than or grater than min or max value
            minimum = arr.get(i)
        elif arr.get(i) > maximum:
            maximum = arr.get(i)
    return (minimum, maximum)



# ------------------- PROBLEM 2 - FIZZ_BUZZ ---------------------------------

def fizz_buzz(arr: StaticArray) -> StaticArray:
    """
    Transforms the input StaticArray by replacing numbers divisible by 3 with "fizz",
    numbers divisible by 5 with "buzz", and numbers divisible by both 3 and 5 with "fizzbuzz".
    Other numbers in the input StaticArray remain unchanged.
    Returns a new StaticArray with "fizz", "buzz", "fizzbuzz", or the original numbers,
    depending on their divisibility by 3 and/or 5 in the input StaticArray.
    """
    new_arr = StaticArray(arr.length())
    for i in range(arr.length()):
        if arr.get(i) % 3 == 0 and arr.get(i) % 5 == 0:  # conditionals on which value is divisble by 3 or 5
            new_arr.set(i, "fizzbuzz")  # also with conditional if 3 or 5 are multiples
        elif arr.get(i) % 5 == 0:
            new_arr.set(i, "buzz")
        elif arr.get(i) % 3 == 0:
            new_arr.set(i, "fizz")
        else:
            new_arr.set(i, arr.get(i))
    return new_arr



# ------------------- PROBLEM 3 - REVERSE -----------------------------------

def reverse(arr: StaticArray) -> None:
    """
    Reverses the elements in the input StaticArray in-place.
    Returns None
    """
    for index in range(arr.length() // 2):  # reverse order of elements in array
        temp = arr.get(index)
        arr.set(index, arr.get(arr.length() - 1 - index))
        arr.set(arr.length() - 1 - index, temp)



# ------------------- PROBLEM 4 - ROTATE ------------------------------------

def rotate(arr: StaticArray, steps: int) -> StaticArray:
    """
    Rotate the given StaticArray by a number of steps.
    Returns a new StaticArray with the rotated elements.
    """
    size = arr.length()
    if steps < 0:
        steps += size  # convert negative steps to positive

    new_arr = StaticArray(size)

    # Copy the elements to the new array
    for i in range(size):
        new_arr[(i + steps) % size] = arr[i]

    return new_arr



# ------------------- PROBLEM 5 - SA_RANGE ----------------------------------

def sa_range(start: int, end: int) -> StaticArray:
    """
    Create a StaticArray containing all consecutive integers between start and end (inclusive).
    Returns a StaticArray containing all consecutive integers between start and end.
    """
    size = abs(end - start) + 1
    sa = StaticArray(size)

    step = -1 if start > end else 1
    for i in range(size):
        sa.set(i, start)
        start += step

    return sa


# ------------------- PROBLEM 6 - IS_SORTED ---------------------------------

def is_sorted(arr: StaticArray) -> int:
    """
    Returns an integer that describes whether the StaticArray is sorted.
    Returns:
        1 if the array is sorted in strictly ascending order.
        -1 if the array is sorted in strictly descending order.
        0 otherwise.
    """
    n = arr.length()
    if n == 1:  # single-element array is considered sorted in strictly ascending order
        return 1

    is_asc = None  # flag to check if the array is in strictly ascending order
    is_desc = None  # flag to check if the array is in strictly descending order

    for i in range(1, n):
        if arr[i] > arr[i-1]:
            is_asc = True
            if is_desc is not None:  # if the array was already in strictly descending order
                return 0
        elif arr[i] < arr[i-1]:
            is_desc = True
            if is_asc is not None:  # if the array was already in strictly ascending order
                return 0
        else:  # equal elements are not allowed in strictly ascending/descending order
            return 0

    if is_asc and not is_desc:
        return 1
    elif is_desc and not is_asc:
        return -1
    else:
        return 0


# ------------------- PROBLEM 7 - FIND_MODE -----------------------------------

def find_mode(arr: StaticArray) -> (int, int):
    """
    Finds the mode (most frequently occurring element) in the input StaticArray.
    Returns a tuple containing the mode (most frequently occurring element) as the first element
    and its frequency (count of occurrences) as the second element.
    """
    current_count = 1  # orders static array values in nondescending or ascending
    maximum_count = 1
    mode = arr.get(0)
    for index in range(1, arr.length()):
        if arr.get(index) == arr.get(index - 1):
            current_count += 1
            if current_count > maximum_count:
                maximum_count = current_count
                mode = arr.get(index)
        else:  # output of array
            current_count = 1
    return mode, maximum_count



# ------------------- PROBLEM 8 - REMOVE_DUPLICATES -------------------------

def remove_duplicates(arr: StaticArray) -> StaticArray:
    """
    Removes duplicates from the input StaticArray and returns a new StaticArray with only unique elements.
    Returns a new StaticArray containing only unique elements from the input array.
    """
    # Create a new StaticArray object to store unique elements
    unique_arr = StaticArray(arr.length())

    # Handle the first element separately
    unique_arr.set(0, arr.get(0))
    unique_index = 1

    # Iterate through the rest of the elements
    for i in range(1, arr.length()):
        if arr.get(i) != arr.get(i-1):
            # Add the element to the unique array if it's different
            unique_arr.set(unique_index, arr.get(i))
            unique_index += 1

    # Create a new StaticArray object with only unique elements
    result_arr = StaticArray(unique_index)
    for i in range(unique_index):
        result_arr.set(i, unique_arr.get(i))
    return result_arr



# ------------------- PROBLEM 9 - COUNT_SORT --------------------------------

def count_sort(arr: StaticArray) -> StaticArray:
    """
    Sorts a StaticArray in non-ascending order using the count sort algorithm
    Returns a new StaticArray with the same content sorted in non-ascending order.
    """
    # Find the range of numbers in the input array
    min_val = float('inf')
    max_val = float('-inf')
    for i in range(arr.length()):
        val = arr.get(i)
        if val < min_val:
            min_val = val
        if val > max_val:
            max_val = val

    # Create a count array to tabulate the occurrences of each element in the input array
    count = [0] * (max_val - min_val + 1)
    for i in range(arr.length()):
        val = arr.get(i)
        count[val - min_val] += 1

    # Create a new StaticArray to store the sorted result
    sorted_arr = StaticArray(arr.length())

    # Iterate through the count array to generate the sorted array
    index = 0
    for i in range(len(count) - 1, -1, -1):
        freq = count[i]
        if freq > 0:
            val = i + min_val
            for j in range(freq):
                sorted_arr.set(index, val)
                index += 1

    return sorted_arr



# ------------------- PROBLEM 10 - SORTED SQUARES ---------------------------

def transform_string(source: str, s1: str, s2: str) -> str:
    """
    Transforms a given source string based on two mapping strings (s1 and s2) and returns the transformed string.
    Returns the transformed string where characters from the source string are replaced based on s1 and s2.
    """
    res = []
    for char in source:
        if char in s1:
            res.append(s2[s1.index(char)])
        elif char.isupper():
            res.append(' ')
        elif char.islower():
            res.append('#')
        elif char.isdigit():
            res.append('!')
        else:
            res.append('=')
    return ''.join(res)




# ------------------- BASIC TESTING -----------------------------------------

if __name__ == "__main__":

    print('\n# min_max example 1')
    arr = StaticArray(5)
    for i, value in enumerate([7, 8, 6, -5, 4]):
        arr[i] = value
    print(arr)
    result = min_max(arr)
    if result:
        print(f"Min: {result[0]: 3}, Max: {result[1]}")
    else:
        print("min_max() not yet implemented")

    print('\n# min_max example 2')
    arr = StaticArray(1)
    arr[0] = 100
    print(arr)
    result = min_max(arr)
    if result:
        print(f"Min: {result[0]}, Max: {result[1]}")
    else:
        print("min_max() not yet implemented")

    print('\n# min_max example 3')
    test_cases = (
        [3, 3, 3],
        [-10, -30, -5, 0, -10],
        [25, 50, 0, 10],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(arr)
        result = min_max(arr)
        if result:
            print(f"Min: {result[0]: 3}, Max: {result[1]}")
        else:
            print("min_max() not yet implemented")

    print('\n# fizz_buzz example 1')
    source = [_ for _ in range(-5, 20, 4)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr[i] = value
    print(fizz_buzz(arr))
    print(arr)

    print('\n# reverse example 1')
    source = [_ for _ in range(-20, 20, 7)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr.set(i, value)
    print(arr)
    reverse(arr)
    print(arr)
    reverse(arr)
    print(arr)

    print('\n# rotate example 1')
    source = [_ for _ in range(-20, 20, 7)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr.set(i, value)
    print(arr)
    for steps in [1, 2, 0, -1, -2, 28, -100, 2 ** 28, -2 ** 31]:
        space = " " if steps >= 0 else ""
        print(f"{rotate(arr, steps)} {space}{steps}")
    print(arr)

    print('\n# rotate example 2')
    array_size = 1_000_000
    source = [random.randint(-10 ** 9, 10 ** 9) for _ in range(array_size)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr[i] = value
    print(f'Started rotating large array of {array_size} elements')
    rotate(arr, 3 ** 14)
    rotate(arr, -3 ** 15)
    print(f'Finished rotating large array of {array_size} elements')

    print('\n# sa_range example 1')
    cases = [
        (1, 3), (-1, 2), (0, 0), (0, -3),
        (-95, -89), (-89, -95)]
    for start, end in cases:
        print(f"Start: {start: 4}, End: {end: 4}, {sa_range(start, end)}")

    print('\n# is_sorted example 1')
    test_cases = (
        [-100, -8, 0, 2, 3, 10, 20, 100],
        ['A', 'B', 'Z', 'a', 'z'],
        ['Z', 'T', 'K', 'A', '5'],
        [1, 3, -10, 20, -30, 0],
        [-10, 0, 0, 10, 20, 30],
        [100, 90, 0, -90, -200],
        ['apple']
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        result = is_sorted(arr)
        space = "  " if result and result >= 0 else " "
        print(f"Result:{space}{result}, {arr}")

    print('\n# find_mode example 1')
    test_cases = (
        [1, 20, 30, 40, 500, 500, 500],
        [2, 2, 2, 2, 1, 1, 1, 1],
        ["zebra", "sloth", "otter", "otter", "moose", "koala"],
        ["Albania", "Belgium", "Chile", "Denmark", "Egypt", "Fiji"]
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        result = find_mode(arr)
        if result:
            print(f"{arr}\nMode: {result[0]}, Frequency: {result[1]}\n")
        else:
            print("find_mode() not yet implemented\n")

    print('# remove_duplicates example 1')
    test_cases = (
        [1], [1, 2], [1, 1, 2], [1, 20, 30, 40, 500, 500, 500],
        [5, 5, 5, 4, 4, 3, 2, 1, 1], [1, 1, 1, 1, 2, 2, 2, 2]
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(arr)
        print(remove_duplicates(arr))
    print(arr)

    print('\n# count_sort example 1')
    test_cases = (
        [1, 2, 4, 3, 5], [5, 4, 3, 2, 1], [0, -5, -3, -4, -2, -1, 0],
        [-3, -2, -1, 0, 1, 2, 3], [1, 2, 3, 4, 3, 2, 1, 5, 5, 2, 3, 1],
        [10100, 10721, 10320, 10998], [-100320, -100450, -100999, -100001],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        before = arr if len(case) < 50 else 'Started sorting large array'
        print(f"Before: {before}")
        result = count_sort(arr)
        after = result if len(case) < 50 else 'Finished sorting large array'
        print(f"After : {after}")

    print('\n# count_sort example 2')
    array_size = 5_000_000
    min_val = random.randint(-1_000_000_000, 1_000_000_000 - 998)
    max_val = min_val + 998
    case = [random.randint(min_val, max_val) for _ in range(array_size)]
    arr = StaticArray(len(case))
    for i, value in enumerate(case):
        arr[i] = value
    print(f'Started sorting large array of {array_size} elements')
    result = count_sort(arr)
    print(f'Finished sorting large array of {array_size} elements')

    print('\n# transform_string example 1\n')
    original = (
        '#     #  =====  !      =====  =====  #     #  =====',
        '#  #  #  !      !      !      !   !  ##   ##  !    ',
        '# # # #  !===   !      !      !   !  # # # #  !=== ',
        '##   ##  !      !      !      !   !  #  #  #  !    ',
        '#     #  =====  =====  =====  =====  #     #  =====',
        '                                                   ',
        '         TTTTT OOOOO      22222   66666    1       ',
        '           T   O   O          2   6       11       ',
        '           T   O   O       222    66666    1       ',
        '           T   O   O      2       6   6    1       ',
        '           T   OOOOO      22222   66666   111      ',
    )
    test_cases = ('eMKCPVkRI%~}+$GW9EOQNMI!_%{#ED}#=-~WJbFNWSQqDO-..@}',
                  'dGAqJLcNC0YFJQEB5JJKETQ0QOODKF8EYX7BGdzAACmrSL0PVKC',
                  'aLiAnVhSV9}_+QOD3YSIYPR4MCKYUF9QUV9TVvNdFuGqVU4$/%D',
                  'zmRJWfoKC5RDKVYO3PWMATC7BEIIVX9LJR7FKtDXxXLpFG7PESX',
                  'hFKGVErCS$**!<OS<_/.>NR*)<<+IR!,=%?OAiPQJILzMI_#[+}',
                  'EOQUQJLBQLDLAVQSWERAGGAOKUUKOPUWLQSKJNECCPRRXGAUABN',
                  'WGBKTQSGVHHHHHTZZZZZMQKBLC66666NNR11111OKUN2KTGYUIB',
                  'YFOWAOYLWGQHJQXZAUPZPNUCEJABRR6MYR1JASNOTF22MAAGTVA',
                  'GNLXFPEPMYGHQQGZGEPZXGJVEYE666UKNE11111WGNW2NVLCIOK',
                  'VTABNCKEFTJHXATZTYGZVLXLAB6JVGRATY1GEY1PGCO2QFPRUAP',
                  'UTCKYKGJBWMHPYGZZZZZWOKQTM66666GLA11111CPF222RUPCJT')

    for case in test_cases:
        print(transform_string(case, '612HZ', '261TO'))
