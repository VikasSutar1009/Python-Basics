def eval_postfix(expr):
    stack = []
    for ch in expr.split():
        if ch.isdigit():
            stack.append(int(ch))
        else:
            b, a = stack.pop(), stack.pop()
            if ch == '+': stack.append(a+b)
            elif ch == '-': stack.append(a-b)
            elif ch == '*': stack.append(a*b)
            elif ch == '/': stack.append(a/b)
    return stack[0]

print(eval_postfix("2 3 1 * + 9 -"))  