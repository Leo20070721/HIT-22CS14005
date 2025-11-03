def ack(m,n):
    if m == 0:
        print(f"A({m},{n})={n+1}")
        return n+1
    elif n == 0:
        print(f"A({m},{n})=A({m-1},1)")
        return ack(m-1,1)
    else:
        print(f"A({m},{n})=A({m - 1},A({m},{n-1})")
        return ack(m-1,ack(m,n-1))

if __name__ == '__main__':
    print("计算ack(m,n)")
    Qm = int(input("请输入m："))
    Qn = int(input("请输入n："))
    print(f"ack({Qm},{Qn})={ack(Qm,Qn)}")