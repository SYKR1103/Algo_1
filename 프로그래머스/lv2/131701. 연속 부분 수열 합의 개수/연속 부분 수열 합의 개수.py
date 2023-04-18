def solution(elements):
    k = len(elements)
    elements = elements * 2

    def substring(temp, n):
        result = []
        for n in range(1, k+1):
            for i in range(len(elements)):
                if i+n > len(elements):
                    break
                result.append(sum(elements[i:i+n]))
        return len(list(set(result)))
    
    
    
    answer = substring(elements, k)
    return answer