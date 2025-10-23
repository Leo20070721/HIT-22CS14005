#编程实例18，刘宇轩 2025112195
def cal_e(n):
    if n<0:
        raise ValueError("请输入非负整数！")
    e=1.0
    fac=1.0
    for i in range(1,n+1):
        fac *= i
        e+=(1.0/fac)
    return e

q=int(input("请输入阶数n："))
print("e=",cal_e(q))
