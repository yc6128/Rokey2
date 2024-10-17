#===========================================================================
# #problem_1

def solution(sides):

    sides.sort() #오름차순
    
    if sides[2] < sides[0] + sides[1]: 
        return 1 
    else:
        return 2 

#===========================================================================
# #problem_2
def solution(x):

    l_sum = sum(int(a) for a in str(x))
    
    if x % l_sum == 0:
        return True
    else:
        return False
    
print(solution(18))
