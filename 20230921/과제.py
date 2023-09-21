# 과제1:
# 마지막 문제 손코딩(만약 여유가 되시면 좀 더 고도화 한 다음 손코딩 해주세요.)

# 과제2:
# student.csv에는 아래와 같은 텍스트가 담겨있습니다.
"""
학년,반,번,이름,국어,영어,수학,사회
3,3,1,licat,90,80,30,40
3,3,2,mura,80,70,60,30
3,3,3,binky,30,80,70,30
"""
# 학생들의 평균을 구해 아래와 같이 student.csv출력되게 해주세요.(xx이라 표기된 곳에 평균 값이 들어가야 합니다.)
"""
학년,반,번,이름,국어,영어,수학,사회,평균
3,3,1,licat,90,80,30,40,xx
3,3,2,mura,80,70,60,30,xx
3,3,3,binky,30,80,70,30,xx
"""
import csv


def calc_average(scores: list[str]):
    scores = list(map(int, scores))
    result = sum(scores) / len(scores)
    print(result)
    return result


head = []
data = []

with open("./20230921/student.csv", "r", encoding="utf-8") as file:
    rdr = csv.reader(file)

    for row in rdr:
        if rdr.line_num == 1:
            head = row
            head.append("평균")
            continue
        scores = row[-4:]
        average = calc_average(scores)
        row.append(str(average))
        data.append(row)

with open("./20230921/student.csv", "w", encoding="utf-8") as file:
    file.writelines([f"{','.join(head)}\n"])
    file.writelines([f"{','.join(row)}\n" for row in data])
