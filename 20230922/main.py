# 저주의 숫자 3 과 5
# 3과 5가 들어간 숫자를 사용하지 않습니다.
#


# def solution(n: int):
#     answer = list(filter(lambda x: "3" not in str(x) and "5" not in str(x), range(100)))
#     return answer[n]


import re


def solution(order: int):
    pattern = re.compile("[369]")
    result = pattern.findall(order)

    return result


print(solution(30))
