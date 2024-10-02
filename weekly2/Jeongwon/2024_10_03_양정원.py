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

# 2번 다른 풀이
def sol2():
    
    list2 = []
    for i in range(1,1001):
        if i % 3 == 0 or i % 5 == 0:
            list2.append(i)
    
    answer = set(list2)
    
    sol = 0
    for i in answer:
        sol += i
        
    return sol

print(sol2())

# problem 3

dic={'.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
       '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
       '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
       '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
       '-.--':'y','--..':'z','':' '}

s = input("모스 부호를 입력하세요: ")

words = s.split("  ")
#print(words)

for i in range(len(words)):
    words2 = words[i].split(" ")
    for j in range(len(words2)):
        if words2[j] in dic:
            words2[j] = dic[words2[j]]
    #print(words2, end = "")

print(words2)

'''
떠오르는 문제 풀이 도구들
for append replace split dic[i] '''
