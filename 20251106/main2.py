import tkinter as tk
import math
from operator import length_hint

color = "#476042"


def dfs(nowPoint,nowAngel,drawAngel,drawLength,drawPercent,drawDeep):
    if drawDeep==0 :
        return
    newLength = drawLength*drawPercent/100

    leftAngel = nowAngel + drawAngel
    rightAngel = nowAngel - drawAngel
    leftPoint = [nowPoint[0] + drawLength * math.cos(leftAngel) , nowPoint[1] - drawLength * math.sin(leftAngel) ]
    rightPoint= [nowPoint[0] + drawLength * math.cos(rightAngel), nowPoint[1] - drawLength * math.sin(rightAngel)]


    mainCanvas.create_line(nowPoint[0], nowPoint[1], leftPoint[0], leftPoint[1], fill=color)
    mainCanvas.create_line(nowPoint[0], nowPoint[1], rightPoint[0], rightPoint[1], fill=color)

    masterWindow.update()

    dfs(leftPoint, leftAngel, drawAngel, newLength, drawPercent, drawDeep-1)
    dfs(rightPoint, rightAngel, drawAngel, newLength, drawPercent, drawDeep-1)


if __name__ == '__main__':
    global masterWindow
    masterWindow=tk.Tk()

    masterWindow.title("分型图绘制")
    masterWindow.geometry("800x800")

    global mainCanvas
    mainCanvas = tk.Canvas(masterWindow,width=800,height=800)
    mainCanvas.pack()

    initPoint=[400,400]
    percent = 70
    drawangel = 30
    deep = 12
    length = 110
    dfs(initPoint, 0 * math.pi / 180, drawangel * math.pi / 180, length, percent, deep)
    dfs(initPoint, 90 * math.pi / 180, drawangel * math.pi / 180, length, percent, deep)
    dfs(initPoint, 180 * math.pi / 180, drawangel * math.pi / 180, length, percent, deep)
    dfs(initPoint, 270 * math.pi / 180, drawangel * math.pi / 180, length, percent, deep)

    masterWindow.mainloop()

# Leo Anderson 刘宇轩 2025112195 25L0212