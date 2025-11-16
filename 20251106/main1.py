import tkinter as tk

flag = 0

if __name__ == '__main__':
    masterWindow = tk.Tk()
    masterWindow.title("计算器")
    masterWindow.geometry("600x300")

    dataLabel1 = tk.Label(masterWindow,text="数字1:",width=20,height=2)
    dataLabel1.grid(row=1,column=1,pady=10)
    defaultValue1 = tk.StringVar()
    dataInput1 = tk.Entry(masterWindow,textvariable=defaultValue1)
    defaultValue1.set("0")
    dataInput1.grid(row=2,column=1,padx=5)

    dataLabel2 = tk.Label(masterWindow, text="数字2:", width=20, height=2)
    dataLabel2.grid(row=1, column=4, pady=10)
    defaultValue2 = tk.StringVar()
    dataInput2 = tk.Entry(masterWindow, textvariable=defaultValue2)
    defaultValue2.set("0")
    dataInput2.grid(row=2, column=4, padx=5)

    def calcAdd():
        defaultValue3.set(str(float(defaultValue1.get()) + float(defaultValue2.get())))
    def calcMinus():
        defaultValue3.set(str(float(defaultValue1.get()) - float(defaultValue2.get())))
    def calcTimes():
        defaultValue3.set(str(float(defaultValue1.get()) * float(defaultValue2.get())))
    def calcDivided():
        if(float(defaultValue2.get())==0):
            defaultValue3.set("被除数不可为0！")
            return
        defaultValue3.set(str(float(defaultValue1.get()) / float(defaultValue2.get())))

    signalAdd = tk.Button(masterWindow,text="+",command=calcAdd,width=5,height=1)
    signalAdd.grid(row=2,column=2,pady=10)
    signalAdd = tk.Button(masterWindow, text="-",command=calcMinus, width=5, height=1)
    signalAdd.grid(row=2, column=3, pady=10)
    signalAdd = tk.Button(masterWindow, text="×",command=calcTimes, width=5, height=1)
    signalAdd.grid(row=3, column=2, pady=10)
    signalAdd = tk.Button(masterWindow, text="÷",command=calcDivided, width=5, height=1)
    signalAdd.grid(row=3, column=3, pady=10)

    signalAdd = tk.Label(masterWindow, text="=", width=2, height=2)
    signalAdd.grid(row=2, column=5, pady=10)

    dataLabel3 = tk.Label(masterWindow, text="结果:", width=20, height=2)
    dataLabel3.grid(row=1, column=6, pady=10)
    defaultValue3 = tk.StringVar()
    dataInput3 = tk.Entry(masterWindow, textvariable=defaultValue3)
    defaultValue3.set("0")
    dataInput3.grid(row=2, column=6, padx=5)

    masterWindow.mainloop()

# Leo Anderson 刘宇轩 2025112195 25L0212