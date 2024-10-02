# problem 1


def divide(x, y):
    try:
        result = x / y
    
    except ZeroDivisionError:
        return "0으로 나눌 수 없습니다."
    
    else:
        return result
    
print(divide(3.2, 2))
print(divide(5.4, 0))


# problem 2

def sol2():
    
    answer = 0
    for i in range(1,1001):
        if i % 3 == 0 or i % 5 == 0:
            answer += i
    
    return answer

print(sol2())
