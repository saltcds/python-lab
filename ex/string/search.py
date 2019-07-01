# 예제1 - 문자열 검색 및 문자 개수 구하기
s = "salt developer CDS"
print(len(s))
print(s.find("per"))    # 문자열 검색, 검색결과 없을 경우 -1
print(s.find("d"))      # 문자 검색, 검색결과 없을 경우 -1
print(s.rfind("r"))     # rear(뒤) 검색, 검색결과 없을 경우 -1
print(s.index("v"))     # 문자 검색, 해당 문자 없을 경우 예외 발생
print(s.count("e"))     # 해당 문자 및 문자열 개수 구하기, 없을 경우 0

""" 💻실행 결과
18
11
5
13
7
3
"""