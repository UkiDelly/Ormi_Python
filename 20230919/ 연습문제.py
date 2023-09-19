# 문제1
# div(a, b)라고 입력했을 때 b에 0이 입력되면 예외처리를 하여 정상작동이 되게 만들어주세요.


def div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("오류가 발생했습니다.")


print(div(1, 0))
