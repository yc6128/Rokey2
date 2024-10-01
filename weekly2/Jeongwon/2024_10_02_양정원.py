# problem 1

def arr_add(list1, list2):
    arr1 = list(map(int, input("첫번째 행을 입력하세요: ")).split())
    arr2 = list(map(int, input("첫번째 열을 입력하세요: ")).split())
    arr3 = list(map(int, input("두번째 행을 입력하세요: ")).split())
    arr4 = list(map(int, input("두번째 열을 입력하세요: ")).split())



# problem 2


def sol2():
    str = input("문장을 입력하세요: ")

    if len(str) == 4 or len(str) == 6 or str.isdigit():
        print(True)
    
    else:
        print(False)

sol2()


# problem 3



def sol3():

    num1 = int(input("최소공배수를 구할 숫자1 을 입력하세요: "))
    num2 = int(input("최소공배수를 구할 숫자2 를 입력하세요: "))

    list1 = []
    multi1 = 1

    for i in range(min(num1,num2), 0, -1):
        if num1 % i == 0 and num2 % i == 0:
            big_ans = i
            break

    list1.append(big_ans)
    list1.append(num1 // big_ans)
    list1.append(num2 // big_ans)
    
    for j in list1:
        multi1 *= j
        
    
    print(multi1)

sol3()


# problem 4

num1 = int(input("정수n을 입력하세요: "))
num2 = int(input("정수m을 입력하세요: "))

for i in range(num2):
    print("*"*num1)
