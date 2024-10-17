#example 1

def solution(sides):
    sorte_sides= sorted(sides)
    if sorte_sides[-1] >= sorte_sides[0]+sorte_sides[1]:
        return 2
    else:
        return 1
    answer = solution(sides)
    return answer






#example 2
def solution(x):
    total = 0
    for i in str(x):
        total += int(i)   #1  ,  2  
        
    if x % total == 0:
        True
        answer = True
    
    else:
        answer = False
        
    return answer
