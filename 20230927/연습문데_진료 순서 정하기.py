# 진료 순서 정하기


def solution(emergency: list[int]):
    sort_emergency = sorted(emergency, reverse=True)
    return [sort_emergency.index(i) + 1 for i in emergency]


print(solution([3, 76, 24]))
