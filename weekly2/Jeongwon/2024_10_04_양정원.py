#problem 1
a = len("두산로키부트캠프")
b = len(["두산로키부트캠프"])
c = len(set("두산로키부트캠프"))
d = len(tuple("두산로키부트캠프"))
e = len({"두산로키부트캠프":"두산로키부트캠프"})

print(a, b, c, d, e)


# problem 2
def calculation():

 try:
 num1 = float(input("첫 번째 숫자를 입력하세요: "))
 num2 = float(input("두 번째 숫자를 입력하세요: "))
 operator = input("연산자를 입력하세요 (+, -, *, /): ")

 if operator == "+":
 print(f"{num1} + {num2} = {num1+num2} 입니다.")
 elif operator == "-":
 print(f"{num1} - {num2} = {num1-num2} 입니다.")
 elif operator == "*":
 print(f"{num1} * {num2} = {num1*num2} 입니다.")
 elif operator == "/":
 print(f"{num1} / {num2} = {num1/num2} 입니다.")
 else:
 print("잘못된 연산자입니다.")
 except ValueError:
 print("유효한 숫자를 입력하세요.")
 except ZeroDivisionError:
 print("0 으로 나눌 수 없습니다.")
  
calculation()
