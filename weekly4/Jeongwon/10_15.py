#problem 1
def solution(A,B):
    A = sorted(A)
    B = sorted(B)
    answer = 0

    for i in range(len(A)):
        answer += A[i] * B[-i-1]
    
    return answer

#problem 2
def solution(t, p):
    count = 0

    for i in range(len(t)-(len(p)-1)):
        k = t[i:i+len(p)]
        if int(k) <= int(p):
            count +=1
        

    return count

#problem 3
def three_six_nine_game(n):
    for i in range(1, n+1):
        if i % 10 == 3 or i % 10 == 6 or i % 10 == 9 :
            print("X", end='')
        elif i >= 30:
            print("30을 초과하였습니다.")
        else:
            print(i, end='')

three_six_nine_game(29)
