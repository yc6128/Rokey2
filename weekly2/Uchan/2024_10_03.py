
#Example 1
"""
def divide(x, y):
    try:
        answer = x / y
        print(f"{x}를 {y}로 나눈 값은 {answer} 입니다.")
        return answer
    
    except ZeroDivisionError:
        print("0으로 나눌수없습니다.")
    
    else:
        pass
    
divide(5.4,0)
"""
#Exampel 2
"""
def calculator (x):
    X3=0
    X5=0
    
    for i in range(3,x,3):
        X3 += i
        
    for J in range(5,x,5):
        X5 += J
            
    result = X3+X5
    print(result)
    
calculator(100)
    """
    
    
# Example 3
dic={'.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
       '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
       '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
       '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
       '-.--':'y','--..':'z','':' '}  
            
            
def morse(a):

    list_a=a.split(' ')   # .split 활용 복습 필요


    for i in range(len(list_a)):

        if list_a[i] in dic:

            b=dic.get(list_a[i]) 
            print (b, )
            
morse(".... .  ... .-.. . . .--. ...  . .- .-. .-.. -.--")
