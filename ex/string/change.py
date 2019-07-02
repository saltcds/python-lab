# 예제 - 변경(대문자, 소문자, 등)
s = "Hello world"

print("1.", s.lower())
print("2.", s.upper())
print("3.", s.swapcase())
print("4.", s.capitalize())
print("5.", s.title())

""" 💻실행 결과
1. hello world
2. HELLO WORLD
3. hELLO WORLD
4. Hello world
5. Hello World
"""

# 예제 - 공백 제거
s = "    salt dev cds    "
print("1.", s)
print("2.", s.lstrip())
print("3.", s.rstrip())
print("4.", s.strip())
""" 💻실행 결과
1.     salt dev cds
2. salt dev cds
3.     salt dev cds
4. salt dev cds
"""