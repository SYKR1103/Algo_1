def solution(s):
    answer = ''
    
    numbers = s.split(" ")
    temp = [int(numbers[0]),int(numbers[0])]
    for number in numbers:
        if int(number) <= temp[0]:
            temp[0] = int(number)
            
        if int(number) >= temp[1]:
            temp[1] = int(number)
            
    answer = str(temp[0]) + " " + str(temp[1]) 
    return answer