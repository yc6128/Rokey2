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

#problem 3
def solution(people, limit):
    count = 0
    for i in range(len(people)):
        for j in range(i+1,len(people)-1):
            if people[i] + people[j] <= limit:
                count += 1
                del people[i], people[j]
        else:
            return len(people)
    
    return count

print(solution([70, 80, 50],100))
                
        
