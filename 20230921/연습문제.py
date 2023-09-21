# 문제 1
# 1~9까지 합
def prob1():
    return sum(range(1, 10))


print(prob1())


# 문제 2
# 1~9까지 홀수 합
def prob2():
    return sum(range(1, 10, 2))


print(prob2())


# 문제 3
# 1000 미만의 자연수에서 3의 배수와 5의 배수의 총합을 구하는 프로그램을 작성
def prob3():
    three, five = [x for x in range(3, 1000, 3)], [x for x in range(5, 1000, 5)]
    result = sum(set(three + five))
    return result


print(prob3())

import numpy as np

m = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

print(np.sum(m))


import re
from collections import Counter

s = "Hello, World! This is a sample string for testing purposes."
counter = Counter(re.findall(r"[a-zA-Z]", s))
print(dict(counter.most_common()))


s = "Hello, World! This is a sample string for testing purposes."

d = {}
for c in s:
    d[c] = d.get(c, 1) + 1

print(d)
