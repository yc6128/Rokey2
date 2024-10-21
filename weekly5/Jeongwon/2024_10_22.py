# problem 1
def solution(N):
    lst = []
    for i in range(N//5+1):
        for j in range(N//3+1):
            if (5 * i) + (3 * j) == N:
                lst.append(i + j)
        
        
    
    if len(lst) > 0:
        return min(lst)

    return -1

# problem 2
def solution():
    N = int(input())
    people = []
    for i in range(N):
        a = input('나이와 이름을 입력하세요: ')
        people_split = a.split()
        people.append((int(people_split[0]), people_split[1]))

    print(people)

print(solution())
    
    for j in people:

    

    

# problem 3
def solution():
    lst = []
    while True:
        a = input('')
        if a == '':
            break

        a_splited = a.split()
        
        if a_splited[0] == '1':
            lst.append(a_splited[1])
        
        elif a_splited[0] == '2':
            if lst:
                print(lst.pop())
            else:
                print(-1)

        elif a_splited[0] == '3':
            print(len(lst))

        elif a_splited[0] == '4':
            if not lst:
                print(1)
            else:
                print(0)
        
        elif a_splited[0] == '5':
            if lst:
                print(lst[-1])
            else:
                print(-1)
        
print(solution())
