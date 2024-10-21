#문제 1 
def solution(N):
    count = 0
    while N >= 0:
        if N % 5 == 0:  
            alpha = N // 5
            N = N - (5*(alpha))
            count +=(alpha)
            break
        else: 
            N -= 3
            count += 1
        if N < 0: 
            count = -1
            break
    return count

print(solution(4)) 




#문제2 

N=int(input())

count = 0
dic = {}
while (count != N):
    a = (input())
    age_name= a.split(" ")
    dic[age_name[1]]=int(age_name[0])
    count+=1

result = sorted(dic.items(), key=lambda x: x[1])

for name, age in result:
    print(age, name)




#문제3

N=int(input())

stack=[]
count = 0
while(count != N):
    a = (input())

    if a[0]=='1':
        alpha = a.split(" ")
        stack.append(alpha[1])
    elif a == '2':
        if not stack:
            print(-1)
        else:
            print(stack.pop())
    elif a == '3':
        print(len(stack))
    elif a=='4':
        if stack:
            print(0)
        else:
            print(1)
    else:
        if stack:
            print(stack[-1])
        else:
            print(-1)     

    count +=1   
    