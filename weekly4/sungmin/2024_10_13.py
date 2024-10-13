#==============================================================================================================
#problem_1

def solution(cpr):
    answer = []
    basic_order = ["check", "call", "pressure", "respiration", "repeat"]
    for action in cpr:
        for i in range(len(basic_order)):
            if action == basic_order[i]:
                answer.append(i + 1)  # 기본 순서는 1부터 시작하므로 i+1을 추가
    return answer

#==============================================================================================================
##problem_2

number = int(input())

answer = 0
# while number > 0:
for i in range(100):

    answer += number % 100  
    number //= 100  

print(answer)
