
def solution(n):

    for i in range(n+1, n*n):
        
        if str(bin(i)).count("1") == str(bin(n)).count("1"):
            return i
        
        