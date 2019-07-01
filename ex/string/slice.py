# 예제1 - 기본
s = "saltdev-ds"
print(s[2:5])
print(s[3:])
print(s[:4])
print(s[2:-2])

""" 💻실행 결과
ltd
tdev-ds
salt
ltdev-
"""

# 예제1 - 거꾸로 출력
s2 = "가나다라마바사"
print(s2[::2])     # 2칸씩  출력
print(s2[::-1])    # 거꾸로 출력

""" 💻실행 결과
가다마사
사바마라다나가
"""

# 예제3 - 파일명과 확장자
s3 = "abcdefg.jpg"
print(s3[0:-4])
print(s3[-3:])
""" 💻실행 결과
abcdefg
jpg
"""