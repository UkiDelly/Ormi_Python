from collections import Counter


def solution(N: int, stages: list[int]):
    players = len(stages)
    answer = []
    counter = Counter(stages)

    for i in range(1, N + 1):
        fail = counter[i]
        if not fail:
            answer.append((i, 0))
            continue
        answer.append((i, fail / players))
        players -= fail

    answer.sort(key=lambda x: x[1], reverse=True)
    return list(map(lambda x: x[0], answer))


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4, 4, 4, 4, 4]))


# from collections import Counter


# def solution(N, stages):
#     total_people = len(stages)
#     count_people = Counter(stages)

#     answer = {}  # 스테이지:실패율

#     for i in range(1, N + 1):
#         answer[i] = 0

#     for i in answer:
#         if count_people[i] != 0 and total_people != 0:
#             answer[i] = count_people[i] / total_people
#         total_people -= count_people[i]

#     print(answer)

#     answer = sorted(answer, key=lambda x: answer[x], reverse=True)

#     return list(map(lambda x: answer[x], answer))


solution(5, [2, 1, 2, 6, 2, 4, 3, 3])
