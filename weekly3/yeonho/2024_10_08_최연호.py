# problem_1 코딩테스트 연습 스택/큐 올바른 괄호 //  problem_2 코딩테스트 연습완전탐색 카펫 // problem_3  코딩테스트 연습탐욕법(Greedy) 구명보트



# problem_1 코딩테스트 연습 스택/큐 올바른 괄호

'''
문제 설명

괄호가 바르게 짝지어졌다는 것은 '(' 문자로 열렸으면 반드시 짝지어서 ')' 문자로 
닫혀야 한다는 뜻입니다. 예를 들어

    "()()" 또는 "(())()" 는 올바른 괄호입니다.
    ")()(" 또는 "(()(" 는 올바르지 않은 괄호입니다.

'(' 또는 ')' 로만 이루어진 문자열 s가 주어졌을 때, 문자열 s가 올바른 괄호이면 true를 return 하고, 
올바르지 않은 괄호이면 false를 return 하는 solution 함수를 완성해 주세요.
제한사항

    문자열 s의 길이 : 100,000 이하의 자연수
    문자열 s는 '(' 또는 ')' 로만 이루어져 있습니다.
입출력 예
s 	answer
"()()" 	true
"(())()" 	true
")()(" 	false
"(()(" 	false
입출력 예 설명

입출력 예 #1,2,3,4
문제의 예시와 같습니다.
'''

def solution1(s):
    if s[0] == '(':  
        if s[-1] == ')': 
            return True
        elif s[-1] != ')':  
            return False
        
    if s[-1] == ')':  
        if s[0] == '(': 
            return True
        elif s[0] != '(':  
            return False
        
    if s[0] == ')' or s[-1] == '(':  
        return False

s = "(()(" 
#print(solution1(s))


# problem_2 코딩테스트 연습완전탐색 카펫

'''
문제 설명

Leo는 카펫을 사러 갔다가 아래 그림과 같이 중앙에는 노란색으로 칠해져 있고 테두리 1줄은 갈색으로 칠해져 있는 격자 모양 카펫을 봤습니다.

carpet.png

Leo는 집으로 돌아와서 아까 본 카펫의 노란색과 갈색으로 색칠된 격자의 개수는 기억했지만, 전체 카펫의 크기는 기억하지 못했습니다.

Leo가 본 카펫에서 갈색 격자의 수 brown, 노란색 격자의 수 yellow가 매개변수로 주어질 때 카펫의 가로, 세로 크기를 순서대로 배열에 담아 return 하도록 solution 함수를 작성해주세요.
제한사항

    갈색 격자의 수 brown은 8 이상 5,000 이하인 자연수입니다.
    노란색 격자의 수 yellow는 1 이상 2,000,000 이하인 자연수입니다.
    카펫의 가로 길이는 세로 길이와 같거나, 세로 길이보다 깁니다.

입출력 예
brown 	yellow 	return
  10 	   2 	[4, 3]
   8 	   1 	[3, 3]
  24 	   24 	[8, 6]

'''
def solution2(brown, yellow):
    answer=[]
    height=0 #세로
    width=0  #가로
    sum_carpet=brown+yellow
    # 10 2 12 
    # 1~6
    # 
    for i in range(1,(sum_carpet/2)+1):
        if sum_carpet % i ==0:
            width=sum_carpet/i

    return answer
    

# problem_3  코딩테스트 연습탐욕법(Greedy) 구명보트
'''
문제 설명

무인도에 갇힌 사람들을 구명보트를 이용하여 구출하려고 합니다. 구명보트는 작아서 한 번에 최대 2명씩 밖에 탈 수 없고, 무게 제한도 있습니다.

예를 들어, 사람들의 몸무게가 [70kg, 50kg, 80kg, 50kg]이고 구명보트의 무게 제한이 100kg이라면 2번째 사람과 4번째 사람은 같이 탈 수 있지만 1번째 사람과 3번째 사람의 무게의 합은 150kg이므로 구명보트의 무게 제한을 초과하여 같이 탈 수 없습니다.

구명보트를 최대한 적게 사용하여 모든 사람을 구출하려고 합니다.

사람들의 몸무게를 담은 배열 people과 구명보트의 무게 제한 limit가 매개변수로 주어질 때, 모든 사람을 구출하기 위해 필요한 구명보트 개수의 최솟값을 return 하도록 solution 함수를 작성해주세요.
제한사항

    무인도에 갇힌 사람은 1명 이상 50,000명 이하입니다.
    각 사람의 몸무게는 40kg 이상 240kg 이하입니다.
    구명보트의 무게 제한은 40kg 이상 240kg 이하입니다.
    구명보트의 무게 제한은 항상 사람들의 몸무게 중 최댓값보다 크게 주어지므로 사람들을 구출할 수 없는 경우는 없습니다.

입출력 예
people 	limit 	return
[70, 50, 80, 50] 	100 	3
[70, 80, 50] 	100 	3
'''

def solution3(people,limit):
    answer=0
    light=0
    light_two=1

    sorted_people=sorted(people)
    while len(sorted_people)!=0:

        if len(sorted_people)==1:
            answer+=1
            break

        if sorted_people[light]+sorted_people[light_two] <=limit:
            answer += 1
            del sorted_people[light]
            del sorted_people[light]
            
        else:
            answer +=1
            del sorted_people[light]
    
    return answer

people= [50,70,50,80]
limit=100
#print(solution3(people,limit))