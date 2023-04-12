def solution(s):
    answer = []    
    bins, zeros = 0, 0    
    while s!="1":        
        zeros += s.count("0")
        s= s.replace("0","")
        s = bin(len(s))[2:]
        bins+=1    
    answer = [bins, zeros]    
    return answer

