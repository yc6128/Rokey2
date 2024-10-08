# problem 1






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
