def solution(n):
    answer = 0

    if n==0 or n==1:
        return n
      
    pre, cur = 0, 1
    i=1
    while i<n:

        pre, cur = cur, pre+cur
        i+=1

    return cur%1234567
    
    
    