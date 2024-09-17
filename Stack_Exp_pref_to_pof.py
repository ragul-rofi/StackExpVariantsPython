def is_operand(c):
    return ('a' <= c <= 'z') or ('A' <= c <= 'Z') or ('0' <= c <= '9')

def prefix_to_postfix(s):
    stack = []
    for c in reversed(s):
        if is_operand(c):
            stack.append(c)
        else:
            op1 = stack.pop()
            op2 = stack.pop()
            stack.append(op1 + op2 + c)
    return stack.pop()

# Test the function
s = input("Enter a prefix expression: ")
print("Postfix:", prefix_to_postfix(s))