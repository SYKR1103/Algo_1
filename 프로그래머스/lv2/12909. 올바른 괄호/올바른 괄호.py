def solution(s):

    opens = 0
    closes = 0
    
    i = 0
    
    while i < len(s):
        if s[i] =="(":
            opens+=1
            
        else:
            closes+=1
            
        if closes>opens:
            return False
        i+=1
        
    if opens!=closes:
        return False
        
    return True