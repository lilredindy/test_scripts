
def solution(parentheses):
    # Type your solution here
    
    
    print (parentheses + "\n")
    p = parentheses.split("()")
    print (p)
    
    suffix = 0
    prefix = 0
    
    for word in p:
        if word is "":
            continue
        suffix += word.count('(')
        prefix += word.count(')')
                    
    final_str = prefix*'(' + parentheses + suffix*')' 
     
    return final_str

str = solution(")))((")
print (str)