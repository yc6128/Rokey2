# 1 (실패)
def example (N):
    if N == 4 or N == 7:
        return -1
    elif N % 5 == 0:
        return N // 5
    else:
        return 1 + example(N - 3)
    
    
result = example(16)
print(result)


#2(성공)
N = int(input())

members = []
for _ in range(N):
    age, name = input().split()
    age = int(age)
    members.append((age, name))

members.sort(key=lambda member: member[0])

for member in members:
    print(member[0], member[1])


#3 (실패)
 # AI code 
import sys
input = sys.stdin.read  #여러줄 입력

def process_commands(commands):
    stack = []
    result = []

    for command in commands:
        if command[0] == '1':
            _, x = command.split()
            stack.append(int(x))
        elif command[0] == '2':
            if stack:
                result.append(stack.pop())
            else:
                result.append(-1)
        elif command[0] == '3':
            result.append(len(stack))
        elif command[0] == '4':
            result.append(1 if not stack else 0)
        elif command[0] == '5':
            if stack:
                result.append(stack[-1])
            else:
                result.append(-1)

    return result

if __name__ == "__main__":
    data = input().splitlines()
    n = int(data[0])
    commands = data[1:]
    output = process_commands(commands)
    for line in output:
        print(line)
