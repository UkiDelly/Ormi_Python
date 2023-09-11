# 문제 1번
x = 3
y = 5
result = (x + y) or (isinstance(x, int) and isinstance(y, int))
print(result)

# 문제 2번
print("hello" < "hell o")  # False, 그 이유는 공백의 유니코드가 알파벳보다 앞이라서(?)
print([10, 20, 30] < [10, 19, 100])  # False, 2번째 인젝스인 20 < 19는 False 이기 때문에
print(10 % 3.3 == 0.1)  # False, 부동소수점의 오류로 인하여

# 문제 3번
email2 = "abc@gmail.com"  # gmail
email3 = "abc@naver.com"  # naver
email4 = "abc@weniv.co.kr"  # weniv
email5 = "li.cat@weniv.co.kr"  # weniv


def get_email(email: str) -> str:
    return email.split("@")[1].split(".")[0]


print(get_email(email2))
print(get_email(email3))
print(get_email(email4))
print(get_email(email5))
