# 예제 - 리스트 정렬
count = 1   # 실행결과 순번 증가
nums = [1, 3, 5, 7, 9, 8, 6, 4, 2]
print("{}.{}".format(count, nums))
""" 💻실행 결과
1.[1, 3, 5, 7, 9, 8, 6, 4, 2]
"""

count += 1  # 실행결과 순번 증가
nums.sort(reverse = True)   # reverse = True(내림) | False(오름, 디폴트)
print("{}. {}".format(count, nums))
count += 1  # 실행결과 순번 증가
nums.reverse()
print("{}. {}".format(count, nums))
""" 💻실행 결과
2. [9, 8, 7, 6, 5, 4, 3, 2, 1]
3. [1, 2, 3, 4, 5, 6, 7, 8, 9]
"""

alphabet = ["a", "c", "e", "E", "d", "b"]
count += 1  # 실행결과 순번 증가
alphabet2 = sorted(alphabet)
print("{}. alphabet : {} / alphabet2 : {}".format(count, alphabet, alphabet2))
count += 1  # 실행결과 순번 증가
alphabet.sort()
print("{}. {}".format(count, alphabet))
count += 1  # 실행결과 순번 증가
alphabet.sort(key = str.lower)
print("{}. {}".format(count, alphabet))
""" 💻실행 결과
4. alphabet : ['a', 'c', 'e', 'E', 'd', 'b'] / alphabet2 : ['E', 'a', 'b', 'c', 'd', 'e']
5. ['E', 'a', 'b', 'c', 'd', 'e']
6. ['a', 'b', 'c', 'd', 'E', 'e']
"""