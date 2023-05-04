def solution(numbers):
    answer = []
    
    
    #소수 판별
    def sosu(num):
        
        if num in (0,1):
            return False
        
        for i in range(2,num):
            if num%i==0:
                return False
            
        return True
    
    
    #조합 생성
    def comb(string1, string2):

        if string1!="":
            if sosu(int(string1)):
                #011과 11은 같으니까
                answer.append(int(string1))
   
        for i in range(len(string2)):
            #한개씩 더해줌
            #빈값에서 전체 뒤집은것까지의 경우의수 하나씩 던져주면 소수판별추가
            comb(string1+string2[i], string2[i+1:]+string2[:i])
            
    comb("", numbers)
    print(set(answer))
    return len(set(answer))