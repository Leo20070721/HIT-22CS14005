#输出斐波那契数列前n项
def fibonacci(n):
    a=0
    b=1
    print(b,end=' ')
    for i in range(n-1):
        b=a+b
        a=b-a
        print(b,end=' ')

if __name__=="__main__":
    q=int(input("你想要斐波那契数列的前几项？："))
    fibonacci(q)