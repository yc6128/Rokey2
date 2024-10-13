# 심폐소생술은 다음과 같은 순서를 통해 실시합니다. 프로그래머스 cpr문제 /정기평가 4번 빈칸 문제
# https://school.programmers.co.kr/learn/courses/30/lessons/340203?language=python3
# #==============================================================================================================
# problem_1
# 심정지 및 무호흡 확인 [check]
# 도움 및 119 신고 요청 [call]
# 가슴압박 30회 시행 [pressure]
# 인공호흡 2회 시행 [respiration]
# 가슴압박, 인공호흡 반복 [repeat]
# 주어진 solution 함수는 심폐소생술을 하는 방법의 순서가 담긴 문자열들이 무작위 순서로 담긴 리스트 cpr이 주어질 때 
# 각각의 방법이 몇 번째 단계인지 순서대로 담아 return하는 함수입니다. solution 함수가 올바르게 작동하도록 빈칸을 채워 solution 함수를 완성해 주세요
# 제한사항
# cpr은 다음 문자열들이 한 번씩 포함되어 있습니다.
# "check", "call", "pressure", "respiration", "repeat"
# 입출력 예 #1

# "call", "respiration", "repeat", "check", "pressure"은 각각 2, 4, 5, 1, 3 번째 순서이므로 [2, 4, 5, 1, 3]을 리턴합니다.
# 입출력 예 #2

# "respiration", "repeat", "check", "pressure", "call"은 각각 4, 5, 1, 3, 2 번째 순서이므로 [4, 5, 1, 3, 2]를 리턴합니다.
# cpp를 응시하는 경우 리스트는 배열과 동일한 의미이니 풀이에 참고해주세요.
# ex) 번호가 담긴 정수 리스트 numbers가 주어집니다. => 번호가 담긴 정수 배열 numbers가 주어집니다.

def solution(cpr):
    answer = []
    basic_order = ["check", "call", "pressure", "respiration", "repeat"]
    for action in cpr:
        for i in range(5):
            if action == basic_order[i]:
                answer.append(i+1)
    return answer

cpr = ["pressure", "repeat", "respiration", "call" ,"check"]
print(solution(cpr))
# 실행 결과

# 정기평가 3번 / 프로그래머스 수 나누기
# #==============================================================================================================
# https://school.programmers.co.kr/learn/courses/30/lessons/340205
# problem_2

# 2자리 이상의 정수 number가 주어집니다. 주어진 코드는 이 수를 2자리씩 자른 뒤, 자른 수를 모두 더해서 그 합을 출력하는 코드입니다. 
# 코드가 올바르게 작동하도록 한 줄을 수정해 주세요.

number= int(input("숫자를 입력하세요: "))
total = 0

for i in range((len(str(number)) // 2)):
    total += number % 100  
    number //= 100        

print(total)