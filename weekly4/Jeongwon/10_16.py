#problem 1

def solution(price, money, count):
    result = 0
    for i in range(count+1):
        result += price * i
    
    if money >= result:
        return 0
    
    return result - money
  
#problem 2

def solution(s):
    a = len(s)
    if a % 2 == 0:
        return s[len(s)//2 -1 : len(s)//2+1]
    
    else:
        return s[len(s)//2]
              
    return s

#problem 3

def solution(n):
    word = ''
    for i in range(1,n+1):
        if i % 2 == 1:
            word += '수'
        if i % 2 == 0:
            word += '박'
     
    return word
  
#problem 4

def solution(numbers):
    lst = []
    for i in range(len(numbers)-1):
        for j in range(i+1, len(numbers)):
            lst.append(numbers[i]+numbers[j])
    lst = list(sorted(set(lst)))
            
    return lst



#problem 5

def solution(array, commands):
    lst = []
    for command in commands:
        word = sorted(array[command[0]-1:command[1]])
        word = word[:command[2]]
        lst.append(word[-1])

    return lst
