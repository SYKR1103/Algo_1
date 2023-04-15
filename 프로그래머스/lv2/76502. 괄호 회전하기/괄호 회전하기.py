def solution(s):
    answer = 0

    for i in range(0,len(s)):
        if i==0:
            temp = s
        else:
            temp = s[i:]+s[:i]
        
        i=0
        while i<100:
            temp = temp.replace("{}","").replace("()","").replace("[]","")
            i+=1 
            if temp =="":
                answer+=1
                break    
   
    return answer