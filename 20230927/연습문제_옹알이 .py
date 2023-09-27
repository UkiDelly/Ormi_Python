import re

# def solution(babbling: list[str]):
#     pattern = re.compile(r"aya|ye|woo|ma")
#     tmp = []
#     for word in babbling:
#         tmp.append(pattern.sub("#", word))

#     answer = []
#     for word in tmp:
#         if all(x == "#" for x in word):
#             answer.append(word)

#     return len(answer)


def solution(babbling):
    regex = re.compile("^(aya|ye|woo|ma)+$")
    cnt = 0
    for e in babbling:
        if regex.match(e):
            cnt += 1
    return cnt


# print(solution(["aya", "yee", "u", "maa", "wyeoo"]))
print(solution(["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]))
