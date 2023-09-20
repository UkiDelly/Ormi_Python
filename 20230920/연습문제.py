# 회전초밥 문제

# 초밥은 아래와 같은 양식으로 나옵니다.


# 각 초밥은 몇개가 나올지 알 수 없습니다.
# 초밥에 '어'가 나오는 초밥만 먹습니다.
# 내가 먹은 초밥의 비용을 계산하는 코드를 작성


from typing import Any, Generator


susi = [
    ["광어 초밥", 1000],
    ["연어 초밥", 2000],
    ["계란 초밥", 3000],
    ["문어 초밥", 4000],
    ["장어 초밥", 5000],
]


def solution(data: list):
    for name, price in data:
        if "어" in name:
            yield price


print(sum(solution(susi)))


def another_solution(*name: str):
    susi_list = list(generator(name))
    for name, price in susi_list:
        if "어" in name:
            yield price


def generator(data: tuple[str]) -> Generator[list[str | int], Any, None]:
    price: int = 1000
    for name in data:
        yield [name, price]
        price += 1000


print(sum(another_solution("광어 초밥", "연어 초밥", "계란 초밥", "문어 초밥", "장어 초밥")))
