def solution(priorities, location):
    answer = 0
    
    trans = []
    copy = trans.copy()
    for idx, pro in enumerate(priorities):
        trans.append(str(pro)+":"+str(idx))
        
    done = []
    while trans:
        
        com = trans.pop(0)
        
        temp = []
        for each in trans:
            temp.append(int(each.split(":")[0]))
        
        if len(temp)>0 and int(com.split(":")[0])< max(temp):
            trans.append(com)
        else:
            done.append(com)
            
                
    for idx, each in enumerate(done):
        if int(each.split(":")[1]) == location:
            return idx+1

            
    
            
            
        
        
        
    
    
    
    
    
    
    return answer