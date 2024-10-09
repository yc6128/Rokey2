# problem 1

dict1 = {'John': 85, 'Jane': 92, 'Dave': 78}
total = 0

for i, j in dict1.items():
    total += j
    average = total // len(dict1)

print(f"학생들의 총점은 {total}이고 평균은 {average} 이다.")


# problem 2

import datetime
now =  datetime.datetime.now()
print(now)
# print(f"현재 시간:",now.strftime("%Y-%-m-%d %H:%M:%S"))

# problem 3

def reverse3(n):
    remainder = []
    
    while n!=0:
        remainder.append(n % 3)
        n = n // 3
    
    count = []
    num = len(remainder)-1
    for i in remainder:
        count.append(i * (3 ** num))
        num -= 1
    
    sol = sum(count)
        
    return sol
   

print(reverse3(45))
    

    # n을 3의 제곱의 어떤 수로 나눈다. 근데 바로 아래 수로 나눠야함 
    # 나머지를 출력해서 그 수를 또 나눈다 
