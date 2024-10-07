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
