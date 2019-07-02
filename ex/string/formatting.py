# 예제 - 포멧팅
jumsu = 90
jumsu2 = 87.12345
grade = "A"

print("1.", "점수 : %d" %jumsu)
print("2.", "점수 : %d, 등급 : %s" %(jumsu, grade))
print("3.", "점수 : %5d, 등급 : %5s" %(jumsu, grade))   # %5d => 5자리
print("4.", "점수 : %-5d, 등급 : %-5s" %(jumsu, grade))   # %-5d => 5자리, 왼쪽 정렬
print("5.", "점수 : %5.3f, 등급 : %-5s" %(jumsu2, grade))   # %5.3f => 총 5자리 소수점 3자리
""" 💻실행 결과
1. 점수 : 90
2. 점수 : 90, 등급 : A
3. 점수 :    90, 등급 :     A
4. 점수 : 90   , 등급 : A   
5. 점수 : 87.123, 등급 : A 
"""

# 예제 - 포멧팅 {}
student = {"jumsu":81, "grade":"C"}
print("1.", "점수 : {}, 등급 : {}".format(jumsu, grade))
print("2.", "점수 : {0}, 등급 : {1}".format(jumsu, grade))
print("3.", "점수 : {a}, 등급 : {b}".format(a = 79, b = "B"))
print("4.", "점수 : {0[jumsu]}, 등급 : {0[grade]}".format(student))
""" 💻실행 결과
1. 점수 : 90, 등급 : A
2. 점수 : 90, 등급 : A
3. 점수 : 79, 등급 : B
4. 점수 : 81, 등급 : C
"""