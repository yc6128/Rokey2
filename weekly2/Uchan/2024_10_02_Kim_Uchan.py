
#2
s="45.3"
s_len=len(s)
if s_len == 4 or s_len == 6:
    try:
        type(int(s)) == int
        print (True)
    except ValueError:
        print( False)    
       
else:
    print(False)
    
  
    






#3
"""
Num1=input("첫번째 숫자")
Num2=input("두번쨰 숫자")

def calculation(a,b):
    if a%2==0:
        result1=0
        if
        
    else:

   
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
        
"""
#4   
n=int(input("가로길이"))
m=int(input("세로길이"))
i=0
while i < m:
    print(("*")*n)
    i+=1
    
print("33")
    
