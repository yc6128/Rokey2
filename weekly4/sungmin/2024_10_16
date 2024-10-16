#===========================================================================
#problem_1   
def is_happy(n):
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(digit) ** 2 for digit in str(n))
    return n == 1

count = 0
total_sum = 0

for i in range(1, 10000):
    if is_happy(i):
        count += 1
        total_sum += i

print(f"행복 수의 개수: {count}")
print(f"행복 수의 총합: {total_sum}")

#===========================================================================
#problem_2
# 진짜 모르겠어요 gpt 사용 

from fractions import Fraction

# 축전기들의 저장 용량을 계산하는 함수
def possible_capacitances(n):
    if n == 1:
        return {Fraction(1)}
    
    capacities = set()
    # n개의 축전기를 두 개의 그룹으로 나누어서 직렬 및 병렬 연결 계산
    for i in range(1, n):
        left = possible_capacitances(i)
        right = possible_capacitances(n - i)
        
        for l in left:
            for r in right:
                # 병렬 연결
                capacities.add(l + r)
                # 직렬 연결
                capacities.add(Fraction(1, Fraction(1, l) + Fraction(1, r)))
    
    return capacities

# D(n)을 계산하는 함수
def D(n):
    return len(possible_capacitances(n))

# D(18) 값을 구하기
result = D(18)
print(f"D(18)의 값은: {result}")
