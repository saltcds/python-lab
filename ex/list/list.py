# 예제 - 리스트(list) - 점수 합계, 평균
jumsu = [90, 95, 75, 86, 66]
sum = 0
for s in jumsu:
    sum += s
print("1.", "총점 : {} / 평균 : {}".format(sum, sum / len(jumsu)))
""" 💻실행 결과
1. 총점 : 412 / 평균 : 82.4
"""

# 예제 - 리스트(list) - 요소 접근 방식
jumsu = [90, 95, 75, 86, 66]
print("1.", jumsu[0])
print("2.", jumsu[-1])
print("3.", jumsu[1:2])
print("4.", jumsu[:3])
print("5.", jumsu[3:])
""" 💻실행 결과
1. 90
2. 66
3. [95]
4. [90, 95, 75]
5. [86, 66]
"""