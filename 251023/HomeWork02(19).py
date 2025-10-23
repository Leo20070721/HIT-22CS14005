#编程实例19，刘宇轩 2025112195
def cal_e_precision(n):
    e=1.0
    fac = 1.0
    i=0
    pre=0.1 ** n
    while ((1.0)/fac >= pre):
        i += 1
        fac*=i
        e+=(1.0/fac)
    return e,i

q=int(input("请输入计算精度(1e-n，n=?)："))
get_e , get_n = cal_e_precision(q)
print("e=",get_e," n=",get_n)