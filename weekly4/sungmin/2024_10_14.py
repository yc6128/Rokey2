#==============================================================================================================
##problem_1
def solution(A, B):
    # A는 오름차순으로, B는 내림차순으로 정렬
    A.sort()
    B.sort(reverse=True)
    
    answer = sum(a * b for a, b in zip(A, B)) #  각각 묶어서 곱하고 더함
    
    return answer

A = [1, 4, 2]
B = [5, 4, 4]
print(solution(A, B))
# #==============================================================================================================
# ##problem_2    GPT활용
def solution(t, p):

    len_p = len(p)
    int_p = int(p)
    
    count = 0
    
    # t에서 p와 길이가 같은 부분문자열을 추출합니다.
    for i in range(len(t) - len_p + 1):
        # t의 부분문자열을 추출하고 숫자로 변환합니다.
        sub_t = int(t[i:i+len_p])
        # p보다 작거나 같으면 카운트를 증가시킵니다.
        if sub_t <= int_p:
            count += 1
    
    return count
#==============================================================================================================
##problem_3

def game_369(n):
    for i in range(1, n+1):

        if '3' in str(i) or '6' in str(i) or '9' in str(i):
            print("X", end=' ')  # 3, 6, 9가 있으면 x 출력
        else:
            print(i, end=' ') # 숫자를 출력


n = int(input()) 
game_369(n)
