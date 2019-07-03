# 예제 - 리스트 인덱스, 카운터, 최대, 최소, 크기
count = 1   # 실행결과 순번 증가
nums = [n * 10 for n in range(1,11)]
nums += [n * 10 for n in range(1,11,2)]
print("{}.{}".format(count, nums))
""" 💻실행 결과
1.[10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 10, 30, 50, 70, 90]
"""

count += 1  # 실행결과 순번 증가
print("{}.20은 {} 번째".format(count, nums.index(20)))
count += 1  # 실행결과 순번 증가
print("{}.10은 {} 개".format(count, nums.count(10)))
count += 1  # 실행결과 순번 증가
print("{}.리스트 수 : {}".format(count, len(nums)))
count += 1  # 실행결과 순번 증가
print("{}.최대 값 : {}".format(count, max(nums)))
count += 1  # 실행결과 순번 증가
print("{}.최소 값 : {}".format(count, min(nums)))
""" 💻실행 결과
2.20은 1 번째
3.10은 2 개
4.리스트 수 : 15
5.최대 값 : 100
6.최소 값 : 10
"""