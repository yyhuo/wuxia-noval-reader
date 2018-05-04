# 这是程序的主体
# -*- coding:utf-8 -*-

from tkinter import *
from tkinter.ttk import *


def donothing():
    filewin = Toplevel(root)
    button = Button(filewin, text="Do nothing button")
    button.pack()


root = Tk()
root.wm_title('简单小说阅读器')
root.geometry('800x600')
menubar = Menu(root)

filemenu = Menu(menubar, tearoff=0)
editmenu = Menu(menubar,tearoff=0)
setmenu = Menu(menubar,tearoff=0)
bankmenu = Menu(menubar,tearoff=0)
pludginmenu = Menu(menubar,tearoff=0)
aboutmenu = Menu(menubar,tearoff=0)

for item in ["导入文件夹","导入文件","打开文件","关闭窗口","退出"]:
    filemenu.add_command(label=item, command=donothing)

for item in ["进入编辑模式","复制","剪切","粘贴","删除","退出编辑模式"]:
    editmenu.add_command(label=item, command=donothing)

for item in ["阅读设置","网络设置"]:
    setmenu.add_command(label=item, command=donothing)

for item in ["打开书库","导入书库"]:
    bankmenu.add_command(label=item, command=donothing)

for item in ["安装插件","插件库"]:
    pludginmenu.add_command(label=item, command=donothing)



menubar.add_cascade(label="文件(F)", menu=filemenu)
menubar.add_cascade(label="编辑(E)", menu=editmenu)
menubar.add_cascade(label="设置(S)", menu=setmenu)
menubar.add_cascade(label="书库(B)", menu=bankmenu)
menubar.add_cascade(label="插件(P)", menu=pludginmenu)
menubar.add_cascade(label="关于(A)", menu=aboutmenu)

root['menu'] = menubar
root.mainloop()
