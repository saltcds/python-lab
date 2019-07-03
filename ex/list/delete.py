# 예제 - 삭제
count = 1   # 실행결과 순번 증가
nums = [n for n in range(1,11)]
print("{}.{}".format(count, nums))
""" 💻실행 결과
1.[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
"""

count += 1  # 실행결과 순번 증가
nums.remove(5)
del(nums[2])
print("{}.{}".format(count, nums))
""" 💻실행 결과
2.[1, 2, 4, 6, 7, 8, 9, 10]
"""

count += 1  # 실행결과 순번 증가
nums[1:4] = []
print("{}.{}".format(count, nums))
""" 💻실행 결과
3.[1, 7, 8, 9, 10]
"""

count += 1  # 실행결과 순번 증가
print("{}.{} >> {}".format(count, nums.pop(), nums))
count += 1  # 실행결과 순번 증가
print("{}.{} >> {}".format(count, nums.pop(2), nums))
""" 💻실행 결과
4.10 >> [1, 7, 8, 9]
5.8 >> [1, 7, 9]
"""