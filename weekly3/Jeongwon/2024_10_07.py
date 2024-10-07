#problem 1
def solution(s):
    dic1 = {"(" : 1, ")": -1}
    count = 0
    for i in s:
        if i =="(":
            count +=1
        elif i == ")":
            count -=1
        if count < 0:
            return False
            break
        

    if count < 0 :
        return False
    elif count == 0:
        return True
    return False

print(solution("(()("))

#problem 2
'''
def solution(brown, yellow):
    extent = brown + yellow
    for i in range((brown//2)-1, 0, -1):
        if extent % i ==0:
            return [i, extent//i]


print(solution(10,2))
'''

def solution(brown, yellow):
    extent = brown + yellow
    for i in range(1, int(extent**0.5)+1):
        if extent % i ==0:
            j = extent // i
            if (j - 2) * (i - 2) == yellow:
                return [j, i]


print(solution(10,2))
