#problem 1
a = len("두산로키부트캠프")
b = len(["두산로키부트캠프"])
c = len(set("두산로키부트캠프"))
d = len(tuple("두산로키부트캠프"))
e = len({"두산로키부트캠프":"두산로키부트캠프"})

print(a, b, c, d, e)


# problem 2
def calculation():

 try:
 num1 = float(input("첫 번째 숫자를 입력하세요: "))
 num2 = float(input("두 번째 숫자를 입력하세요: "))
 operator = input("연산자를 입력하세요 (+, -, *, /): ")

 if operator == "+":
 print(f"{num1} + {num2} = {num1+num2} 입니다.")
 elif operator == "-":
 print(f"{num1} - {num2} = {num1-num2} 입니다.")
 elif operator == "*":
 print(f"{num1} * {num2} = {num1*num2} 입니다.")
 elif operator == "/":
 print(f"{num1} / {num2} = {num1/num2} 입니다.")
 else:
 print("잘못된 연산자입니다.")
 except ValueError:
 print("유효한 숫자를 입력하세요.")
 except ZeroDivisionError:
 print("0 으로 나눌 수 없습니다.")
  
calculation()

# problem 3
def prime(result):

    if result < 2:
        return

    for a in range(2, int(result**0.5)+1):
        if result % a == 0:
            return
        
    else:
        return result

def solution(nums):
    lst = []
    i = 0
    for i in range(i,len(nums)-2):
        for j in range(i+1,len(nums)-1):
            for k in range(j+1, len(nums)):
                result = nums[i]+nums[j]+nums[k]
                if result == prime(result):
                    lst.append(sorted([nums[i],nums[j],nums[k]]))
    '''
    for i in lst:
        sums = sum(i)
        print(f"{i}를 이용해서 {sums}을 만들 수 있습니다.") 
    ''' 
    
    return len(lst)

nums = [1,2,7,6,4]
solution(nums)
# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

import random


nums_count = random.randint(3,51)
a = range(1,1001)
nums = random.sample(a, k=nums_count)
print(f"숫자가 주어졌습니다. 함수를 사용할 매개 변수를 넣어주세요\n{nums}")
s = list(map(int, input("숫자 입력: ").split()))

def solution():
    total = 0
    set_count = len(set(s) & set(nums))
    if set_count == 3:
        for i in s:
            total += i

    else:
        k = sorted(list(set(s).difference(nums)))
        print(f"숫자{k}가 리스트에 없습니다.")

    print(f"더하면 나오는 숫자: {total}")

    
    if total < 2:
        return f"{total}은 소수가 아닙니다."
    
    for i in range(2, int(total**0.5)+1):
        if total % i == 0:
            return f"{total}은 소수가 아닙니다."
    
    else:
        return f"{total}은 소수입니다."
  
print(solution())


