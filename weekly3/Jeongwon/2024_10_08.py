# problem 1
def solution(new_id):
    new_id = new_id.lower()
    result = []

    for i in new_id:
        if i.isalnum() or i in ['-','_','.']:
            result.append(i)

    result = ''.join(result)

    while ".." in result:
        result=result.replace("..",'.')
    
    result = result.strip(".")
    
    if result == "":
        result = 'a'
    
    elif len(result) >= 16:
        result = result[:15]
        if result[-1] == '.':
            result = result[:-1]
    
   
    while len(result) <3:
        result += result[-1]
    

    return result
    





# problem 2
def solution(s):
    dic1 = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five':'5' ,'six': '6','seven': '7', 'eight': '8','nine': '9'}
    lst = []
    word = ""
    
    
    for i in s:
        if i.isdigit():
            lst.append(i)

        else:
            word += i
            if word in dic1:
                lst.append(dic1[word])
                word = ""

    lst1 = ''.join(lst)
    ans = int(lst1)
    return ans
    
    


print(solution("2three45sixseven"))
