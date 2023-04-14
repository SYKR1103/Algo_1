def solution(s):
    answer = -1

    temp = []
    
    for letter in s:
        
        if len(temp)>0 and temp[-1] == letter:           
            temp.pop()
        else:
            temp.append(letter)
            
            
    if temp == []:
        return 1
    else:
        return 0
    

    