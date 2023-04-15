def solution(cacheSize, cities):
    
    
    temp = []
    count = 0

    if cacheSize ==0:
        return 5*len(cities)
    
    
    i=0
    while i<len(cities):
        if cities[i].lower() in temp:
            temp.remove(cities[i].lower())
            temp.append(cities[i].lower())
            count+=1
        
        if temp==[]:
            temp.append(cities[i].lower())
            count+=5
            
        if cities[i].lower() not in temp:
            if len(temp)==cacheSize:
                temp.pop(0)      
            temp.append(cities[i].lower())
            count+=5
                            
        i+=1
        
    return count
        