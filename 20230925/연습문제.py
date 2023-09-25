def solution(data: list[int]):
    sandwitch = [1, 2, 3, 4, 1]
    count = 0
    stack = []

    for i in data:
        stack.append(i)
        if stack[-5:] == sandwitch:
            del stack[-5:]

    return count


print(solution([1, 1, 1, 2, 3, 4, 1, 2, 3, 4, 1]))
