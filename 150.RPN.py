# import operator

# def RPN(nums):
#     stack = []


#     operator_mapping = {
#         "+": operator.add,
#         "-": operator.sub,
#         "/": operator.truediv,  
#         "*": operator.mul
#     }

#     for num in nums:
#         if num not in '+*-/':
#             stack.append(num)

#         else:
#             a , b = stack.pop() , stack.pop()
#             stack.append(f'{a}{operator_mapping[num]}{b}')

#     return stack
        


def RPN(nums):
    stack =[]

    for num in nums:
        if num == '+':
            a , b = stack.pop() , stack.pop()
            c = b + a
            stack.append(c)

        elif num == '-':
            a , b = stack.pop() , stack.pop()
            c = b - a
            stack.append(c)

        elif num == '/':
            a , b = stack.pop() , stack.pop()
            c = b // a
            stack.append(c)

        elif num == '*':
            a , b = stack.pop() , stack.pop()
            c = b * a
            stack.append(c)

        else:
            stack.append(int(num))

    return stack[0]




tokens = ["1","2","+","3","*","4","-"]

print(RPN(tokens))