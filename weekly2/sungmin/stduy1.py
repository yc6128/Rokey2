# 문제1
# from collections import Counter

# input_string = input("문자열을 입력하세요: ")

# words = input_string.split()

# word_count = Counter(words)

# sorted_word_count = dict(sorted(word_count.items(), key=lambda item: item[1], reverse=True))

# for word, count in sorted_word_count.items():
#     print(f"{word}: {count}")

#====================================================================================
# 문제2) 재귀 함수를 사용하여 팩토리얼을 계산하는 프로그램을 작성하시오.

# def factorial(n):
#     if n == 0 or n == 1: 
#         return 1
#     else:
#         return n * factorial(n - 1)  

# a = int(input("팩토리얼을 계산할 숫자를 입력하세요: "))

# print(factorial(a))

#===================================================================================
# 문제3) 사용자로부터 정수를 입력받아, 숫자가 소수인지 판별하는 프로그램을 작성하시오.


# num = int(input("정수를 입력하세요: "))


# if num <= 1:
#     print(f"{num}은(는) 소수가 아닙니다.")
# else:
#     is_prime = True 
    
#     for i in range(2, num):
#         if num % i == 0:
#             is_prime = False
#             break

#     if is_prime:
#         print(f"{num}은(는) 소수입니다.")
#     else:
#         print(f"{num}은(는) 소수가 아닙니다.")

#===================================================================================

# 문제4) 두 수의 최대공약수를 구하는 프로그램을 작성하시오.
## 유클리드 호세법 
# def f(x, y):
#     if y == 0:
#         return x
#     else:
#         return f(y, x % y)
    
# a = int(input("첫 번째 숫자를 입력하세요: "))
# b = int(input("두 번째 숫자를 입력하세요: "))

# print(f"{a}와 {b}의 최대공약수는 {f(a, b)}입니다.")
## -----------------------------------------------------------------------
# a = int(input("정수를 입력해주세요: "))
# b = int(input("정수를 입력해주세요: "))
# my_list = []
# for i in range(1, min(a,b) + 1):
#     if a % i == 0 and b % i ==0:
#         my_list.append(i)

# r = max(my_list)
# print(r)

#=============================================================================================================

# 문제5) 사용자로부터 정수를 입력받아, 입력받은 정수의 수 만큼 * 피라미드 탑을 쌓는 코드를 작성하시오.

# def f(n):
#     for i in range(1,n+1):
#         print(" "*(n-i),end="")
#         print('*'*(2*i-1))

# a = int(input("숫자를 입력해주세요: "))
# print(f(a))

#=============================================================================================================

# 문제6) 아래 딕셔너리를 JSON 형식의 데이터로 파일에 저장하고, 다시 불러오는 프로그램을 작성하시오.
#     • 딕셔너리
# data = {
#     'name': 'John',
#     'age': 30,
#     'city': 'New York'
# }


# import json

# # 주어진 딕셔너리
# data = {
#     'name': 'John',
#     'age': 30,
#     'city': 'New York'
# }

# # JSON 형식으로 파일에 저장
# with open('data.json', 'w') as file:
#     json.dump(data, file)  # 딕셔너리를 JSON 형식으로 변환하여 파일에 저장

# # 파일에서 JSON 데이터를 다시 불러오기
# with open('data.json', 'r') as file:
#     loaded_data = json.load(file)  # 파일에서 JSON 데이터를 불러와서 딕셔너리로 변환

# # 불러온 데이터 출력
# print(loaded_data)

#===================================================================================================================

# 문제7) 주어진 리스트 [('a', 1), ('b', 2), ('c', 3), ('a', 4)]를 딕셔너리로 변환하되, 
# 키가 중복될 경우 값들을 리스트로 묶어서 저장하는 코드를 작성하시오. 예를 들어, 
# 출력 결과는 {'a': [1, 4], 'b': 2, 'c': 3}과 같이 됩니다.

# data = [('a', 1), ('b', 2), ('c', 3), ('a', 4)]

# result = {}
# for key, value in data:
#     if key in result:
#         if not isinstance(result[key], list):
#             result[key] = [result[key]]
#         result[key].append(value)
#     else:
#         result[key] = value

# print(result)

