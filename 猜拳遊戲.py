import random
def judge(player):
    choice = ["剪刀", "石頭", "布"]
    computer = choice[random.randint(0, 2)]
    # print("電腦出",computer)
    if player==computer:
        剪刀按鈕.destroy()
        石頭按鈕.destroy()
        布按鈕.destroy()
        msg=tk.Message(window,text="電腦出{}\n平手".format(computer),width=100)
        msg.pack()
    elif player=="石頭" and computer=="剪刀":
        剪刀按鈕.destroy()
        石頭按鈕.destroy()
        布按鈕.destroy()
        msg = tk.Message(window, text="電腦出{}\n你贏了".format(computer),width=100)
        msg.pack()
    elif player=="石頭" and computer=="布":
        剪刀按鈕.destroy()
        石頭按鈕.destroy()
        布按鈕.destroy()
        msg = tk.Message(window, text="電腦出{}\n你輸了".format(computer),width=100)
        msg.pack()
    elif player=="剪刀" and computer=="石頭":
        剪刀按鈕.destroy()
        石頭按鈕.destroy()
        布按鈕.destroy()
        msg = tk.Message(window, text="電腦出{}\n你輸了".format(computer),width=100)
        msg.pack()
    elif player=="剪刀" and computer=="布":
        剪刀按鈕.destroy()
        石頭按鈕.destroy()
        布按鈕.destroy()
        msg = tk.Message(window, text="電腦出{}\n你贏了".format(computer),width=100)
        msg.pack()
    elif player=="布" and computer=="石頭":
        剪刀按鈕.destroy()
        石頭按鈕.destroy()
        布按鈕.destroy()
        msg = tk.Message(window, text="電腦出{}\n你贏了".format(computer),width=100)
        msg.pack()
    elif player=="布" and computer=="剪刀":
        剪刀按鈕.destroy()
        石頭按鈕.destroy()
        布按鈕.destroy()
        msg = tk.Message(window, text="電腦出{}\n你贏了".format(computer),width=100)
        msg.pack()

import tkinter as tk
def 按下剪刀按鈕():
    judge(player="剪刀")

def 按下石頭按鈕():
    judge(player="石頭")

def 按下布按鈕():
    judge(player="布")

# 建立主視窗
window = tk.Tk()
window.title('來猜拳吧') #視窗標題
window.geometry("300x100+250+150") #視窗大小，及視窗（左上角）在螢幕上的座標位置為 (250, 150)
剪刀按鈕=tk.Button(window,
                   text="剪刀",
                   command=按下剪刀按鈕)
剪刀按鈕.pack()
石頭按鈕=tk.Button(window,
                   text="石頭",
                   command=按下石頭按鈕)
石頭按鈕.pack()
布按鈕=tk.Button(window,
                   text="布",
                   command=按下布按鈕)
布按鈕.pack()
# 執行主程式
window.mainloop()