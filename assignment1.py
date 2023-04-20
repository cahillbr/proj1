# Name:
# OSU Email:
# Course: CS261 - Data Structures
# Assignment:
# Due Date:
# Description:


import random
from static_array import *


# ------------------- PROBLEM 1 - MIN_MAX -----------------------------------

def min_max(arr: StaticArray) -> tuple:
    # Initialize min and max to the first element of the array
    min_val = max_val = arr.get(0)

    # Loop through the rest of the array, updating min and max as necessary
    for i in range(1, arr.length()):
        val = arr.get(i)
        if val < min_val:
            min_val = val
        elif val > max_val:
            max_val = val

    # Return min and max as a tuple
    return (min_val, max_val)


# ------------------- PROBLEM 2 - FIZZ_BUZZ ---------------------------------

def fizz_buzz(arr: StaticArray) -> StaticArray:
    n = len(arr)
    result_arr = StaticArray(n)
    for i in range(n):
        if arr[i] % 3 == 0 and arr[i] % 5 == 0:
            result_arr[i] = "fizzbuzz"
        elif arr[i] % 3 == 0:
            result_arr[i] = "fizz"
        elif arr[i] % 5 == 0:
            result_arr[i] = "buzz"
        else:
            result_arr[i] = arr[i]
    return result_arr

# ------------------- PROBLEM 3 - REVERSE -----------------------------------

def reverse(arr: StaticArray) -> None:
    left = 0
    right = len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1


# ------------------- PROBLEM 4 - ROTATE ------------------------------------

def rotate(arr: StaticArray, steps: int) -> StaticArray:
    n = len(arr)
    if n == 1 or steps % n == 0:
        return arr.copy()
    steps = steps % n
    result = StaticArray(n)
    for i in range(n):
        j = (i + steps) % n
        result[j] = arr[i]
    return result


# ------------------- PROBLEM 5 - SA_RANGE ----------------------------------

def sa_range(start: int, end: int) -> StaticArray:
    arr = StaticArray(end - start + 1)
    for i in range(len(arr)):
        arr[i] = start + i
    return arr


# ------------------- PROBLEM 6 - IS_SORTED ---------------------------------

def is_sorted(arr: StaticArray) -> int:
    n = len(arr)
    if n == 1:
        return 1

    ascending = True
    descending = True

    for i in range(1, n):
        if arr[i] < arr[i - 1]:
            ascending = False
        if arr[i] > arr[i - 1]:
            descending = False

    if ascending:
        return 1
    elif descending:
        return -1
    else:
        return 0


# ------------------- PROBLEM 7 - FIND_MODE -----------------------------------

def find_mode(arr: StaticArray) -> tuple:
    mode = arr[0]
    mode_freq = 1
    curr = arr[0]
    curr_freq = 1

    for i in range(1, len(arr)):
        if arr[i] == curr:
            curr_freq += 1
        else:
            if curr_freq > mode_freq:
                mode = curr
                mode_freq = curr_freq
            curr = arr[i]
            curr_freq = 1

    # Check the last value
    if curr_freq > mode_freq:
        mode = curr
        mode_freq = curr_freq

    return mode, mode_freq


# ------------------- PROBLEM 8 - REMOVE_DUPLICATES -------------------------

def remove_duplicates(arr: StaticArray) -> StaticArray:
    n = len(arr)
    if n == 1:
        return arr.copy()

    new_arr = StaticArray(n, arr[0].__class__)
    new_arr[0] = arr[0]
    j = 1

    for i in range(1, n):
        if arr[i] != arr[i-1]:
            new_arr[j] = arr[i]
            j += 1

    return new_arr[:j]


# ------------------- PROBLEM 9 - COUNT_SORT --------------------------------

def count_sort(arr: StaticArray) -> StaticArray:
    # Find the range of values in the array
    min_val = max_val = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < min_val:
            min_val = arr[i]
        elif arr[i] > max_val:
            max_val = arr[i]

    # Create a count array to store the number of occurrences of each value
    count = [0] * (max_val - min_val + 1)
    for i in range(len(arr)):
        count[arr[i] - min_val] += 1

    # Modify count array to store the cumulative sum of occurrences
    for i in range(1, len(count)):
        count[i] += count[i-1]

    # Create the output array and fill it with the sorted elements
    output = StaticArray(len(arr))
    for i in range(len(arr)-1, -1, -1):
        output[count[arr[i]-min_val]-1] = arr[i]
        count[arr[i]-min_val] -= 1

    return output


# ------------------- PROBLEM 10 - TRANSFORM_STRING ---------------------------

def transform_string(source: str, s1: str, s2: str) -> str:
    # Create a dictionary to map characters in s1 to characters in s2
    mapping = {s1[i]: s2[i] for i in range(len(s1))}

    # Create a list to hold the transformed characters
    transformed = []

    # Process the source string one character at a time
    for c in source:
        if c in mapping:
            # Replace the character using the mapping
            transformed.append(mapping[c])
        elif c.isupper():
            transformed.append(' ')
        elif c.islower():
            transformed.append('#')
        elif c.isdigit():
            transformed.append('!')
        else:
            transformed.append('=')

    # Return the transformed string
    return ''.join(transformed)


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
