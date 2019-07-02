# 예제 - 대체
s = "소금 개발자"
print("1.", s)
print("2.", s.replace("개발자", "dev"))
""" 💻실행 결과
1. 소금 개발자
2. 소금 dev
"""

# 예제 - 정렬(오른쪽, 왼쪽, 가운데)
s = "salt developer CDS"
print("1.", s.ljust(30))
print("2.", s.rjust(30))
print("3.", s.center(30))
""" 💻실행 결과
1. salt developer CDS
2.             salt developer CDS
3.       salt developer CDS
"""