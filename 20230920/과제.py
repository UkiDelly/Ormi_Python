import time
from typing import Callable
import datetime


# 문제1
# 다음과 같이 동작하는 제너레이터 함수 fibonacci(n)를 완성하세요.
# 주어진 숫자 n까지의 피보나치 수열을 반환합니다.
# 인터넷에서 피보나치 순열 Python 코드를 검색해보셔도 좋습니다.


def fib(n: int):
    curr_num, next_num = 0, 1
    for _ in range(n + 1):
        yield curr_num
        curr_num, next_num = next_num, curr_num + next_num


for i in fib(5):
    print(i)


# 문제2
# 주어진 함수의 실행 시간을 측정하여 출력하는 데코레이터 time_it를 작성하세요.
# (힌트: time 모듈의 time() 함수를 사용하세요.)
def time_it(function: Callable):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = function(*args, **kwargs)
        end = time.time()
        print(f"실행하는데 걸린 시간: {datetime.timedelta(seconds=(end-start))}초")
        return result

    return wrapper


@time_it
def time_measure():
    time.sleep(5)


time_measure()
