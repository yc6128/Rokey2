# problem_1

user_input = input("문자열을 입력하세요: ")

count_dict = {}

for i in user_input:
    if i in count_dict:
        count_dict[i] += 1 
    else:
        count_dict[i] = 1

solution1 = dict(sorted(count_dict.items(), key = lambda item: item[1], reverse = True)) 

print(solution1)


# problem_2


def factorial(num):
    if num == 0 or num == 1:
        return 1
    
    else:
        return num * factorial(num - 1)

num = int(input("팩토리얼 숫자를 입력하세요: "))

result = factorial(num)
print(result)


# problem_3


num = int(input("소수를 확인할 정수를 입력하세요: "))

if num == 1:
    print("1은 소수가 아닙니다.")

elif num == 2:
    print("2는 소수입니다.")


elif num == 3:
    print("3은 소수 입니다.")

else:
    for i in range(2, int(num**0.5) +1):
        if num % i == 0:
            print("소수가 아닙니다.")
            break
        
        else:
            print("소수입니다.")


# problem 4

num1, num2 = map(int, input("두 정수를 입력하세요: ").split())
ans = []

for i in range(1, min(num1, num2) + 1):
    if num1 % i == 0 and num2 % i ==0:
        ans.append(i)

result = max(ans)
print(result)


# problem 5

num = int(input("쌓을 탑의 높이를 말씀해주세요: "))

for i in range(1, num+1):
    for j in range(num-i):
        print(" ",end="")
    for k in range(2*i-1):
        print("*", end="")
    print()

# problem_6

import json

data = {
    'name': 'John',
    'age' : 30,
    'city' : 'New York'
}

with open("data.json", "w") as f:
    json.dump(data, f)

with open("data.json", "r") as f:
    data_1 = json.load(f)

print(data_1)
