 #====================================================================
#problem_1

# my_list = {'John':85,'Jane':92,'Dave':78}

# a = sum(my_list.values())
# b = len(my_list)
# r = float(a / b)
# print(r)

#  #====================================================================
# #problem_2

# import datetime

# a = datetime.datetime.now()

# print(f"현재 날짜와 시간: {a}")

 #====================================================================
#problem_3

# def solution(n):
#     num = ''
#     while n > 0:
#         a = str(n % 3)
#         num =  a + num
#         n//= 3
#         r = reversed(num)
#     return int((r), 3)         #''.join사용 / #return int(''.join(reversed(num)), 3)

# print(solution(45))


# def solution(n):
#     num = ''
#     while n > 0:
#         a = str(n % 3)
#         num =  num + a
#         n//= 3
#     return int((num), 3)

# print(solution(45))
