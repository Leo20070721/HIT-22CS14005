#对于任意位数正整数检测是否为回文数
if __name__=="__main__":
    q=input("请输入要检测谁是否为回文数：")
    p=q[::-1]
    if(int(q)==int(p)):
        print(q,"是回文数。")
    else:
        print(q,"不是回文数。")