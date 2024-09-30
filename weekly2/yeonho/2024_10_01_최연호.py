# 2024/10/01 스터디 문제풀이 (DR_02161_최연호)

#=========================================================================================
# 문제1) 사용자로부터 문자열을 입력받아, 각 단어의 빈도를 딕셔너리로 계산한 후, 빈도수가
#  높은 순서대로 단어를 출력하는 코드를 작성하시오.

def solution1():
    string = input("문자열을 입력하세요: ")
    string_list = string.split(" ")
    count = {}
    sort_count = []

    # 빈도수 계산
    for i in string_list:
        if i in count:
            count[i] += 1 
        else:
            count[i] = 1  

  
    for k, v in count.items():
        sort_count.append((k, v))

    #리스트(정렬)
    for i in range(len(sort_count)):
        for j in range(i + 1, len(sort_count)):
            if sort_count[i][1] < sort_count[j][1]:
                sort_count[i], sort_count[j] = sort_count[j], sort_count[i]

    #딕셔너리
    answer = {}
    for k, v in sort_count:
        answer[k] = v
    
    for k,v in answer.items():
        for i in range(v):
            print(k ,end=" ")

#solution1()

 #=========================================================================================
# 문제2) 재귀 함수를 사용하여 팩토리얼을 계산하는 프로그램을 작성하시오.

def solution2(n):
    if n == 1:      
        return 1   
    return n * solution2(n - 1)    
 
# print(solution2(5))

 #=========================================================================================
# 문제3) 사용자로부터 정수를 입력받아, 숫자가 소수인지 판별하는 프로그램을 작성하시오.

def solution3(n):
    count = 0
    for i in range(1, n+1):
        if n % i == 0:
            count += 1

    # 소수: 1과 자기 자신 외에 약수가 없는 수('1'은 소수가 아님)
    if count == 2:
        answer = "소수입니다"
    else: 
        answer = "소수가 아닙니다"

    print(answer)

#solution3(11)

 #=========================================================================================
# 문제4) 두 수의 최대공약수를 구하는 프로그램을 작성하시오.

def solution4(x,y):
    answer=0

    # 큰 수 찾기
    if x>y:
        pass
    else:
        x ,y = y, x

    #최대 공약수 계산
    for i in range(y, 0, -1):
        if (x % i == 0) and (y % i == 0):
            answer=i
            break

    print(answer)

#solution4(12,16)

#=========================================================================================   
# 문제5) 사용자로부터 정수를 입력받아, 입력받은 정수의 수 만큼 * 피라미드 탑을 쌓는 코드를 작성하시오.

def solution5(n):
    for i in range(n):

        for j in range(n-i):  
            print(" ", end="")
    
        for k in range(2*(i+1)-1): 
            print("*", end="")
    
        print()

#solution5(5)

#=========================================================================================   
# 문제6) 아래 딕셔너리를 JSON 형식의 데이터로 파일에 저장하고, 다시 불러오는 프로그램을 작성하시오.
#     • 딕셔너리
# data = {
#     'name': 'John',
#     'age': 30,
#     'city': 'New York'
# }

import json

def solution6(data):
    
    with open("solution6.json", 'w') as file: # 파일 저장
        json.dump(data, file) 

    with open("solution6.json", 'r') as file: # 파일 불러오기
        answer = json.load(file) 

    print(answer)

data = {
    'name': 'John',
    'age': 30,
    'city': 'New York'
}

#solution6(data)

#=========================================================================================   
# 문제7) 주어진 리스트 [('a', 1), ('b', 2), ('c', 3), ('a', 4)]를 딕셔너리로 변환하되, 키가 중복될 경우 값들을 리스트로 묶어서 저장하는 코드를 작성하시오. 
# 예를 들어, 출력 결과는 {'a': [1, 4], 'b': 2, 'c': 3}과 같이 됩니다.

def solution7(list):
    answer={}

    for i in range(len(list)):
        k = list[i][0]
        v = list[i][1]

        if k in answer:                     #중복될 경우
            if type(answer[k]) == list:
                answer[k].append(v)         #이미 리스트인 경우 
            else:
                answer[k] = [answer[k], v]  #리스트가 아닌 경우
        else:
            answer[k]=v                     #중복되지 않는 경우

    print(answer)


list= [('a', 1), ('b', 2), ('c', 3), ('a', 4)]

#solution7(list)





    





