def is_operand(c):
    return ('a' <= c <= 'z') or ('A' <= c <= 'Z') or ('0' <= c <= '9')

def postfix_to_prefix(s):
    stack = []
    for c in s:
        if is_operand(c):
            stack.append(c)
        else:
            op1 = stack.pop()
            op2 = stack.pop()
            stack.append(c + op2 + op1)
    return stack.pop()

# Test the function
s = input("Enter a postfix expression: ")
print("Prefix:", postfix_to_prefix(s))