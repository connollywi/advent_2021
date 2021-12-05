from collections import deque


def get_input_data(input_path):
    data = []
    with open(input_path, "r") as input_file:
        data.extend(input_file.readlines())
    return [int(number) for number in data]


def get_increases_count(numbers):
    temp = deque(numbers)
    temp.rotate(-1)
    offset = list(temp)
    difference = [a - b for a, b in zip(numbers, offset)]
    return len([num for num in difference[:-1] if num < 0])


def offset_sums(numbers, offset):
    cache = []
    start = 0
    while 1:
        try:
            numbers[start+offset-1]
            cache.append(sum(numbers[start:offset+start]))
            start += 1
        except IndexError:
            break
    return cache
