#=================================================================
#problem_1(gpt_사용)

def solution(s: str) -> bool:
    stack = []
    
    for char in s:
        if char == '(':  # 열린 괄호일 경우 스택에 추가
            stack.append(char)
        elif char == ')':  # 닫힌 괄호일 경우 스택에서 열린 괄호를 제거
            if not stack:  # 스택이 비어 있다면 짝이 맞지 않음
                return False
            stack.pop()  # 스택에서 열린 괄호 제거
    
    # 문자열을 다 확인한 후 스택이 비어 있으면 올바른 괄호, 비어 있지 않으면 올바르지 않음
    return len(stack) == 0

#====================================================================
#problem_2

# def solution(brown, yellow):
#     answer = []
#     total = brown + yellow  # 전체 격자의 수

#     for h in range(3, total + 1): # h높이 설정(3칸 이상)
#         if total % h == 0:  # h로 나누어 떨어질 때만 가로 길이 계산
#             d = total // h
#####             # (width - 2) * (height - 2)가 노란색 격자의 수와 일치하는지 확인
#####             #if (d - 2) * (h - 2) == yellow:
#####                 # 가로는 세로보다 크거나 같아야 함
#             answer = [d,h]  # [길이,높이]
#             break  

#     return answer

# print(solution(10,2))


#=====================================================================
#problem_3

# def sol(people,limit):
#     people.sort()
#     r = len([p for p in people if p <= 50])
#     r1 = len([p1 for p1 in people if p1 > 50])
    
#     r2 = (r // 2)+(r % 2)
#     boats = r1+r2
    
#     return boats

# print(sol([50,50,70,80],100))
