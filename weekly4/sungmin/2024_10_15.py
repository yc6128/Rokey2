#===========================================================================
#problem_1

# def solution(price, money, count):
#     total=0
#     for i in range(1, count + 1):
    
#         total += price * i #가진돈
    
#     if money >= total:
#         return 0
    
#     result = total - money
#     return result

# # 테스트
# price = 3
# money = 20
# count = 4

# print(solution(price, money, count)) 
# #===========================================================================
# #problem_2


# def sol(s):
#     length = len(s)
#     center = length//2
#     #홀수
#     if length % 2==1:
#         return s[center]
#     #짝수
#     else:
#         return s[center-1:center+1]

#테스트 
# print(solution("abcde")) 
# print(solution("qwer"))


# #===========================================================================
# #problem_3
# def solution(n):
#     result = '수박'* (n//2)  #짝수
    
#     if n % 2 == 1:       #홀수
#         result += '수'
#     return result

##-----------------------------
# # def solution(n):

# #     return ('수박' * n)[:n]
##-----------------------------
#테스트
# print(solution(3))
# print(solution(4))


#===========================================================================
#problem_4    문제를 이해 못함 

# def solution(numbers):
#     result = set()  # 중복을 방지하기 위해 set 사용
#     length = len(numbers)
    
#     # 두 개의 숫자를 뽑아 더하기
#     for i in range(length):
#         for j in range(i + 1, length):
#             result.add(numbers[i] + numbers[j])
    
#     # set을 리스트로 변환하고 오름차순으로 정렬
#     return sorted(result)

# # 테스트 예시
# numbers = [2, 1, 3, 4, 1]
# print(solution(numbers))  # 결과: [2, 3, 4, 5, 6, 7]

# numbers = [5, 0, 2, 7]
# print(solution(numbers))  # 결과: [2, 5, 7, 9, 12]

#===========================================================================
#problem_5    문제는 이해함 풀이를 못함

# def solution(array, commands):
#     result = []
    
#     for command in commands:
#         i, j, k = command
#         # 배열 자르기 (인덱스는 1부터 시작하므로 0 기반 인덱스로 변환해야 함)
#         sliced_array = array[i-1:j]
#         # 정렬
#         sorted_array = sorted(sliced_array)
#         # k번째 숫자를 결과에 추가
#         result.append(sorted_array[k-1])
    
#     return result
##-------------------------------------
# def solution(array, commands):
#     return [sorted(array[i-1:j])[k-1] for i, j, k in commands]
##------------------------------------
# 테스트 예시
# array = [1, 5, 2, 6, 3, 7, 4]
# commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
# print(solution(array, commands))  # 결과: [5, 6, 3]



