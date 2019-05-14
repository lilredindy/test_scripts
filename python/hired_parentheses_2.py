
def solution(parentheses,start_index):
    # Type your solution here
    
    
    count_open = 0

    for i in range(start_index+1, len(parentheses) ):
        if parentheses[i] is '(':
            count_open += 1
        if parentheses[i] is ')':
            if count_open is 0:
                return i
            else:
                count_open -= 1


end_index = solution("(()()()())))", 0)
print end_index