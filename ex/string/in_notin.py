# 예제 - 조사
s = "salt dev cds"
print("1.", "s" in s)
print("2.", "b" in s)
print("3.", "dev" in s)
print("4.", "b" not in s)
print("5.", s.startswith("salt"))
print("6.", s.startswith("valt"))
print("7.", s.endswith("cd"))
print("8.", s.endswith("cds"))

""" 💻실행 결과
1. True
2. False
3. True
4. True
5. True
6. False
7. False
8. True
"""