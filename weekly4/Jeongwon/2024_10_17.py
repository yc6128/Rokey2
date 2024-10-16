#problem 1

def calculation(num):
    while num != 1 and num != 4:
        sum1 = 0
        while num > 0:
            k = num % 10
            sum1 += k**2
            num = num // 10
        # print(sum1)

        num = sum1
    return num == 1

def happy_num(range_num):
    count2 =0
    sum2 = 0
    for i in range(1, range_num+1):
        if calculation(i):
            sum2 += i
            count2 +=1
    
    return f"1 ~ {range_num} 범위의 행복 수는 {count2}개이고 총합은 {sum2}입니다."


print(happy_num(99))

#problem 2

def parallel(num):
    return 60 * num

def serial(num):
    sum1 = 0
    for i in range(num):
        sum1 += 1/60
    if num == 0:
        return 0
    return 1/sum1

def solution(num):
    set1 = set()
    for i in range(num):
        for j in range(num):
            set1.add(parallel(i)+serial(j))
            # print(parallel(i),serial(j))
            

    count1 = len(set1)
    
    return count1


print(solution(18))

