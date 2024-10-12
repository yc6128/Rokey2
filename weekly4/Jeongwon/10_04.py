# problem 1
def solution(cpr):
    answer = []
    basic_order = ["check", "call", "pressure", "respiration", "repeat"]
    for action in cpr:
        for i in range(len(basic_order)):
            if action == basic_order[i]:
                answer.append(i+1)
    return answer

print(solution(["call", "respiration", "repeat", "check", "pressure"]))

# problem 2
number = int(input())

answer = 0

while number > 0:
    answer += number % 100
    number //= 100

print(answer)
