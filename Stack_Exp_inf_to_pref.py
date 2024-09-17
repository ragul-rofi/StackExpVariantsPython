def reverse(exp):
    exp = exp[::-1]
    exp = exp.replace('(','temp')
    exp = exp.replace(')', '(')
    exp = exp.replace('temp', ')')
    return exp

def priority(c):
    if c == '^':
        return 2
    elif c == '/' or c == '*':
        return 1
    elif c == '+' or c == '-':
        return 0
    else:
        return -1

def infixtoprefix(s):
    s = reverse(s)
    stack =[]
    prefix = []

    for i in range (len(s)):
        c = s[i]
        if c.isalnum():
            prefix.append(c)
        elif c == '(':
            stack.append(c)
        elif c == ')':
            while stack and stack[-1] != '(':
                prefix.append(stack.pop())
            stack.pop()
        else:
            while stack and (priority(s[i]) < priority(stack[-1]) or priority(s[i]) == priority(stack[-1])):
                prefix.append(stack.pop())
            stack.append(c)

    while stack:
        prefix.append(stack.pop())
    return ''.join(prefix[::-1])

s = input()
print(infixtoprefix(s))
