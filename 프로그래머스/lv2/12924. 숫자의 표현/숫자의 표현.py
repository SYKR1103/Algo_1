def solution(n):
    
    count = 0
    
    # 위의 for문을 시작점만 잡아주는 역할
    for i in range(1, n+1):
        temp = 0
        for j in range(i, n+1):
            temp+=j
            if temp ==n:
                count+=1
                break
                
            elif temp>n:
                break
    
    return count