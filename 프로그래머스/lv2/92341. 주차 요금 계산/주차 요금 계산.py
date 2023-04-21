import math
def solution(fees, records):
    answer = []
    temp = {}
    for record in records:
        time = record.split(" ")[0]
        number = record.split(" ")[1]    
        inorout = record.split(" ")[2]    
  
        if number not in temp:
            temp[number] = [time+inorout]
        else:
            temp[number].append(time+inorout)


    
    for carnumber, times in temp.items():
        hours, mins =0, 0
        if times[-1][-1]=='N':
            hours+=23
            mins+= 59
        for time in times:
            if time[-1] =="N":
                hours -= int(time[:2])
                mins -= int(time[3:5])
            else:
                hours += int(time[:2])-1
                mins += int(time[3:5])+60
        

        if mins+60*hours-fees[0]>=0:
            print(math.ceil((mins+60*hours-fees[0])/fees[2]))
            print(((mins+60*hours-fees[0])/fees[2]))
            value = fees[1] + math.ceil((mins+60*hours-fees[0])/fees[2])*fees[3]
        else:
            value = fees[1]

        #15.4*600 = 9240 + 5000 = 14240!!!!!
        
        answer.append([carnumber,value])
        answer.sort(key=lambda x:x[0])
        answer2 = []
        for each in answer:
            answer2.append(each[1])
    return answer2


