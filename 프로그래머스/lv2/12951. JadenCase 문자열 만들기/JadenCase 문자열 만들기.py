def solution(s):

    temp=[' ']
    i=0
    while i<len(s):
        print(s[i])
        if temp[-1]==' ' and s[i].isalpha():
            temp.append(s[i].upper())
            
        elif s[i] == ' ':
            temp.append(s[i])
        else:
            temp.append(s[i].lower())
            
        i+=1
    
    answer = "".join(temp).lstrip()
    
    return answer