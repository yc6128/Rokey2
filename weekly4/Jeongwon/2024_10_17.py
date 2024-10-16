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
