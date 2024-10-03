#====================================================================================================    
# Example 1

# 다음 중 값이 다른 것은? 
# 1. len("두산로키부트캠프")
# 2. len(["두산로키부트캠프"])
# 3. len(set("두산로키부트캠프"))
# 4. len(tuple("두산로키부트캠프"))
# 5. len({"두산로키부트캠프":"두산로키부트캠프"})

# 2,5

#====================================================================================================    
# Example 2
# 과제 15차시 문제 18) 사용자로부터 두 개의 숫자와 연산자(+, -, *, /)를 입력받아 사칙연산을 수행하는 프로그램을 작성하시오. 단, 입력 및 연산에서 발생할 수 있는 예외를 적절히 처리하시오. 발생할 수 있는 예외는 (ZeroDivisionError: 나눗셈에서 0으로 나누는 경우 발생하는 예외, ValueError: 숫자가 아닌 값을 입력했을 때 발생하는 예외, 잘못된 연산자를 입력했을 때의 예외) 와 같습니다. 아래 코드에 이어서 작성하시오. 
# -	계산이 성공했는지 여부에 따른 적절한 메시지는 다음과 같이 출력하시오 
# -	출력 예시
# 만약 두 숫자가 10, 0이고 연산자가 /이면: “0으로 나눌 수 없습니다.” 출력
# 만약 첫 번째 입력이 abc일 경우: “유효한 숫자를 입력하세요.” 출력
# 만약 연산자가 ^일 경우: “잘못된 연산자입니다.” 출력
# 만약 두 숫자가 10, 5이고 연산자가 +이면: “결과: 15” 출력

def solution2():
    try:
        # 사용자로부터 입력 받기
        a = input("첫 번째 숫자를 입력하세요: ")
        b = input("두 번째 숫자를 입력하세요: ")
        oper = input("연산자를 입력하세요 (+, -, *, /): ")

        # 입력된 숫자 확인 및 변환
        a = float(a)
        b = float(b)

        # 연산 수행
        if oper == '+':
            result = a + b
        elif oper == '-':
            result = a - b
        elif oper == '*':
            result = a * b
        elif oper == '/':
            if b == 0:
                raise ZeroDivisionError
            result = a / b
        else:
            raise ValueError
        print(f"결과: {result}")

    except ZeroDivisionError:
        print("0으로 나눌 수 없습니다.")
    except ValueError:
        print("잘못된 연산자입니다.")
    except Exception:
        print("유효한 숫자를 입력하세요.")

#solution2()

#====================================================================================================    
# Example 3
# 프로그래머스 문제 (소수만들기)
# 검색 => Summer/Winter Coding(~2018) - 소수만들기
# 문제 설명
# 주어진 숫자 중 3개의 수를 더했을 때 소수가 되는 경우의 개수를 구하려고 합니다. 숫자들이 들어있는 배열 nums가 매개변수로 주어질 때, nums에 있는 숫자들 중 서로 다른 3개를 골라 더했을 때 소수가 되는 경우의 개수를 return 하도록 solution 함수를 완성해주세요.

# 제한사항
# nums에 들어있는 숫자의 개수는 3개 이상 50개 이하입니다.
# nums의 각 원소는 1 이상 1,000 이하의 자연수이며, 중복된 숫자가 들어있지 않습니다.

# -입출력 예 #1
# [1,2,4]를 이용해서 7을 만들 수 있습니다.

# -입출력 예 #2
# [1,2,4]를 이용해서 7을 만들 수 있습니다.
# [1,4,6]을 이용해서 11을 만들 수 있습니다.
# [2,4,7]을 이용해서 13을 만들 수 있습니다.
# [4,6,7]을 이용해서 17을 만들 수 있습니다.


def solution3(nums):
    nums2=0
    count=0
    for i in nums:
        nums2 += i
    
    for i in range(1,nums2+1):
        if nums2 % i ==0:
            count +=1

    if count ==2:
        return nums2
    else:
        return False
    
nums=[1,2,3]
print(f"{nums}을 이용해서 {solution3(nums)}을 만들 수 있습니다.")
