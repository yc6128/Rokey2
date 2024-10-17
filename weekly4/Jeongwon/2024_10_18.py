
# problem 1

def solution(sides):
    max_length = sides.pop(sides.index(max(sides)))
    if max_length < sum(sides):
        return 1
    return 2

# problem 2

def solution(x):
    sum = 0
    a = x
    while x > 0:
        k = x % 10
        sum += k
        x = x // 10
    
    if a % sum == 0:
        return True
    return False
