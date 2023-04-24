def solution(n, t, m, p):
    answer = ''

    # 숫자 나열
    # 진법으로 바꿔서 원자화
    # 차례의 인덱스값 가져오고
    # 구할 숫자갯수 채운 리스트 반환
    
    # 임의로 t로 설정
    # 10진수 n진법으로 바꾸는 내장함수 찾아보기
    
    def convert(n, number):
        
        temp = []
        while number//n!=0:
            
            temp.append(number%n)
            number = number//n
            
        temp.append(number%n)
        temp.reverse()
        con = {10:"A", 11:"B",12:"C",13:"D", 14:"E", 15:"F", 16:"G"}
 
        for i in range(len(temp)):
            if temp[i] in con.keys():
                temp[i] = con[temp[i]]
        
        return "".join(map(str, temp))
    
    answer_list = "" 
    for i in range(t*m):
        answer_list+=convert(n, i)

    answer_list = list(answer_list)
    
    
    for i in range(len(answer_list)):
        if m==p and (i+1)%m==0:
            answer+=answer_list[i]
        elif (i+1)%m==p:
            answer+=answer_list[i]
        if len(answer)==t:
            return answer
        
        
        
        
        
        
        
        
        
    
    
    