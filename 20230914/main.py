from dataclasses import dataclass


# 아래 기본 data를 기반으로 문제를 풀어주세요.
data = [
    {
        "_id": "fd7e9a0f-e77b-436a-B781-119b66033d49",
        "index": "1",
        "name": "나주헌",
        "gender": "여성",
        "age": "43",
    },
    {
        "_id": "8ec6eabb-160a-41e4-A3de-cd33aff0b281",
        "index": "2",
        "name": "엄루다",
        "gender": "남성",
        "age": "22",
    },
    {
        "_id": "bcf804f7-0452-4c31-B9d1-20cc2d38490b",
        "index": "3",
        "name": "형유환",
        "gender": "남성",
        "age": "31",
    },
]

# 문제 1 gender, age값을 추출해보세요. 아래 양식처럼 추출하시면 됩니다. 가능하면 map을 사용해주세요.
result = list(map(lambda x: dict(gender=x["gender"], age=x["age"]), data))
print(result)


# 문제 2 User라는 class를 만들어 해당 데이터를 관리해주세요. 아래처럼 저장되어야 합니다.
# 다만 꼭 변수 이름이 user_1...user_n 일 필요는 없습니다.
# 저장양식: '[user_1, user_2, user_3]'
@dataclass
class User:
    _id: str
    index: str
    name: str
    gender: str
    age: str


users = [User(**person) for person in data]
print(users)


# 문제 3 BankAccount 클래스를 생성하세요. 이 클래스는 owner(계좌주 이름), balance(잔액) 속성을 가져야 합니다.
# 이 클래스는 deposit(amount) (입금) 및 withdraw(amount) (출금) 메서드를 가져야 합니다.
# 단, 출금 시 잔액보다 큰 금액을 출금하려고 하면 "잔액 부족" 메시지를 출력해야 합니다.
@dataclass
class BankAccount:
    owner: User
    balance: int

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("음수를 입금할수 없습니다.")
        self.balance += amount

    def withdraw(self, amount):
        if self.balance < amount:
            raise Exception("잔액 부족")
        self.balance -= amount
        return self.balance


newBank = BankAccount(users[0], 1000)
print(newBank)
newBank.deposit(1000)
print(newBank.withdraw(2500))
