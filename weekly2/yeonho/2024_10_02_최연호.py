#=============================================================================================================

# 1.
#행렬의 덧셈은 행과 열의 크기가 같은 두 행렬의 같은 행, 같은 열의 값을 서로 더한 결과가 됩니다.
#2개의 행렬 arr1과 arr2를 입력받아, 행렬 덧셈의 결과를 반환하는 함수, solution을 완성해주세요.
  
                 #입출력 예시#
#    (arr1)	       (arr2)          (return)
#[[1,2],[2,3]]	[[3,4],[5,6]]	[[4,6],[7,9]]
#  [[1],[2]]	  [[3],[4]]	      [[4],[6]]

def solution1(arr1,arr2):

    for i in range(len(arr1)):
        for j in range(len(arr1[0])):
            arr1[i][j] += arr2[i][j]
    return arr1


arr1=[[1,2],[2,3]]
arr2=[[3,4],[5,6]]
#print(solution1(arr1,arr2))

#=============================================================================================================

# 2.
#문자열 s의 길이가 4 혹은 6이고, 숫자로만 구성돼있는지 확인해주는 함수, solution을 완성하세요.
#예를 들어 s가 "a234"이면 False를 리턴하고 "1234"라면 True를 리턴하면 됩니다.

def solution2(s):

    if len(s) == 4 or len(s) == 6:
        try:
            type(int(s))==int
            return True
        except ValueError:
            return False
    else:
        return False

#print(solution2("1234"))  
    
#=============================================================================================================

#3. 
#두 수를 입력받아 최소공배수를 반환하는 함수, solution을 완성하세요.

def solution3(x,y):
    answer=0

    if x > y:
        pass
    else:
        x, y =y, x

    for i in range(y, 0, -1):
        if (x % i == 0) and (y % i == 0):
            answer=i
            break
    
    answer=int(answer*(x/answer)*(y/answer))
    return answer
    
#print(solution3(7,3))
    
#=============================================================================================================

#4. 
#두 개의 정수 n과 m이 입력하여
#별(*) 문자를 이용해 가로의 길이가 n, 세로의 길이가 m인 직사각형 형태를 출력해보세요.

def solution4(x,y):

    def garo():
        for i in range(x):
            print("*",end="")

    for i in range(y):
        garo()
        print()

#solution4(4,4)

#=============================================================================================================