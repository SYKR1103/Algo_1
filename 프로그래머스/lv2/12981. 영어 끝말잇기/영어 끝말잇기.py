def solution(n, words):

    temp = []
    for idx, word in enumerate(words):
        
        x = idx%n+1
        y = idx//n+1
            
        if len(temp)>0 and word in temp:
            print(temp, word, idx, x, y)
            return [x, y]                
        
        if len(temp) ==0:
            temp.append(word)
        
        elif temp[-1][-1] == word[0]:
            temp.append(word)
        
        elif temp[-1][-1] != word[0]:
            print(idx, x, y)
            return [x,y]
 
    return [0,0]