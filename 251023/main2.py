#隋唐小练
def solve():
    ex=float(input("请输入每天的提升效率："))
    dayup = (1.0+ex)**365
    daydown = (1.0-ex)**365
    print("向上：{:.2f}，向下{:.2f}".format(dayup,daydown))

if __name__=="__main__":
    solve()