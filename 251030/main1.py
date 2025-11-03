from collections import deque

Q = deque()
ques = input("请输入算数表达式：")
for i in ques:
    if i in '0123456789':
        if len(Q) == 0:
            Q.append(i)
            continue
        op = Q.pop()
        if op =='*':
            num = Q.pop()
            num = str(int(num) * int(i))
            Q.append(num)
        elif op =='/':
            num = Q.pop()
            num = str(int(num) / int(i))
            Q.append(num)
        elif op =='%':
            num = Q.pop()
            num = str(int(num) % int(i))
            Q.append(num)
        else:
            Q.append(op)
            Q.append(i)
    elif i in '+-*/^%(（[【{':
        Q.append(i)
    elif i in ')）]】}':
        fin = 0
        num = Q.pop()
        op = Q.pop()
        while not op in '(（[【{':
            if op == '+':
                fin = fin + int(num)
            elif op == '-':
                fin = fin - int(num)
            if len(Q) == 0:
                raise ValueError(f"Too much right parentheses.")
            num = Q.pop()
            op = Q.pop()
        fin += int(num)
        Q.append(str(fin))
    else:
        raise ValueError(f"Unknown operator: {i}")

ans = int(Q.popleft())
while len(Q) != 0:
    op = Q.popleft()
    if op == '+':
        ans = ans + int(Q.popleft())
    elif op == '-':
        ans = ans - int(Q.popleft())
    elif op in '(（[【{':
        continue
    else:
        raise SyntaxError(f"Incorrect calculation.")

print(f"{ques}={ans}")