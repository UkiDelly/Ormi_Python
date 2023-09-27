class User:
    def __init__(self, id: str, name: str):
        self.id = id
        self.name = name

    def __str__(self) -> str:
        return f"User(id={self.id}, name={self.name})"

    def __repr__(self) -> str:
        return f"User(id={self.id}, name={self.name})"


def solution(record: list[str]):
    answer = []
    users = {}

    for string in record:
        info = string.split()

        if info[0] == "Enter":
            users[info[1]] = info[2]
            answer.append([info[1], "님이 들어왔습니다."])

        elif info[0] == "Change":
            users[info[1]] = info[2]
        elif info[0] == "Leave":
            answer.append([info[1], "님이 나갔습니다."])

    return list(map(lambda x: str(users[x[0]] + x[1]), answer))


print(
    solution(
        [
            "Enter uid1234 Muzi",
            "Enter uid4567 Prodo",
            "Leave uid1234",
            "Enter uid1234 Prodo",
            "Change uid4567 Ryan",
        ]
    )
)
