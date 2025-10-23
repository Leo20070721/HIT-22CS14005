#检测四位正整数是否为回文数（低效率）
def solve(n):
    a=n%10
    b=(n//10)%10
    c=(n//100)%10
    d=(n//1000)%10
    if a==d and c==b:
        return True
    else:
        return False
if __name__ == '__main__':
    q=int(input("请输入一个正四位数："))
    while q<1000 | q>=10000:
        q=int(input("非正数四位数，请重新输入："))
    if solve(q):
        print("q=",q,"是回文数。")
    else:
        print("q=",q,"不是回文数。")
