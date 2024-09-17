def postfixtoinfix(s):
    stack = []
    for i in range(len(s)):
        c = s[i]
        if ('a'<= c <= 'z') or ('A'<= c <= 'Z') or ('0'<= c <= '9'):
            stack.append(c)
        else:
            op1 = stack.pop()
            op2 = stack.pop()

            new_infix = '('+op2+c+op1+')'
            stack.append(new_infix)
    print(stack.pop())
s = input("Enter: ")
postfixtoinfix(s)