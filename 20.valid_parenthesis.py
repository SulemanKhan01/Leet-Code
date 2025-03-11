def valid_parentheses(string):

    if string[0] == ")" or string[0] == "}" or string[0] == "]":
        return False
    
    stack = []
    brackets = {')':'(' , ']':'[' , '}':'{'}
    for i in range(len(string)):

        if string[i] == "(" or string[i] == "{" or string[i] == "[":
            stack.append(string[i])

        elif string[i] == ")" or string[i] == "}" or string[i] == "]":
            if not stack or stack.pop() != brackets[string[i]]:
                return False
        
    if len(stack) == 0:
        return True
    else:
        False

print(valid_parentheses("[[(())]]"))

