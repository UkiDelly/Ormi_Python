from collections import deque


def solution(numbers, direction):
    d_num = deque(numbers)

    if direction == "left":
        d_num.rotate(-1)
    elif direction == "right":
        d_num.rotate(1)

    return list(d_num)


print(solution([1, 2, 3, 4, 5], "right"))


def a_solution(numbers, direction):
    if direction == "left":
        e = numbers.pop(0)
        numbers.append(e)

    elif direction == "right":
        e = numbers.pop(0)
        numbers.insert(0, e)

    return numbers


print(a_solution([1, 2, 3, 4, 5], "right"))


import re


def b_solution(my_string: str):
    answer = re.findall(r"[\d]+", my_string)
    return sum(map(int, answer))


print(b_solution("aAb1B2cC34oOp"))
