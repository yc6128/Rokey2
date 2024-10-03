#problem 1
# a = len("두산로키부트캠프")
# b = len(["두산로키부트캠프"])
# c = len(set("두산로키부트캠프"))
# d = len(tuple("두산로키부트캠프"))
# e = len({"두산로키부트캠프":"두산로키부트캠프"})
# print (a)
# print (b)
# print (c)
# print (d)
# print (e)
#===========================================================================
# problem 2
# def calculate():
#     try:
#         a = float(input("첫 번째 숫자를 입력하세요: "))
#         b = float(input("두 번째 숫자를 입력하세요: "))
#         operator = input("연산자를 입력하세요 (+, -, *, /): ")
#         r1 = a + b
#         r2 = a - b
#         r3 = a * b
#         r4 = a / b

#         # 사칙연산 수행
#         if operator == "+":
#             print(f"{a} + {b} = {r1}")
#         elif operator == "-":
#             print(f"{a} - {b} = {r2}")
#         elif operator == "*":
#             print(f"{a} * {b} = {r3}")
#         elif operator == "/":
#             if b == 0:
#                 raise ZeroDivisionError
#             print(f"{a} / {b} = {r4}")
#         else:
#             raise ValueError("잘못된 연산자입니다.")


#     except ValueError:
#             print("유효한 숫자를 입력하세요.")

#     except ZeroDivisionError:
#         print("0으로 나눌 수 없습니다.")

# calculate()
#===========================================================================
# problem 3
### 내가 푼 저는 답을 내지 못했어요...ㅜㅜ
def is_prime(n):
    if n < 2:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

def solution(nums):
    l = range(1,1001)
    answer = 0
    my_list = []
    for i in range(l):
        for j in range(i+1,l):
            for k in range(j+1,l):
                total=nums[i]+nums[j]+nums[k]
                answer+=1
    return answer

### 다른분 풀이
# def solution(nums):
#     answer = 0

#     for i in range(len(nums)):
#         for j in range(i+1, len(nums)):
#             for k in range(j+1, len(nums)):
#                 number = nums[i] + nums[j] + nums[k]
#                 if len([m for m in range(2, number) if number % m == 0]) == 0:
#                     answer += 1

#     return answer
