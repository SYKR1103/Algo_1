import collections
import math
def solution(str1, str2):
    answer = 0

    def first(str):
        
        i = 0
        temp = []
        while i<len(str)-1:         
            if str[i:i+2].isalpha():            
               temp.append(str[i:i+2].lower())
            i+=1            
        return temp

    set1 = collections.Counter(first(str1))
    set2 = collections.Counter(first(str2))
    both = set2&set1
    total = set1|set2
    temp = [0,0]
    
    for each in both.values():
        temp[0]+=each
    
    for each in total.values():
        temp[1]+=each
    print(temp)
    if temp[1]==0:
        return 65536
    else:
        return math.floor(temp[0]/temp[1]*65536)
    
    
    
    
    
    