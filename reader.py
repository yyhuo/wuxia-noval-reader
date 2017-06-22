# 这是程序的主题
# -*- coding:utf-8 -*-

from tkinter import *
from tkinter.ttk import *

root = Tk()
root.wm_title('简单小说阅读器')
menubar = Menu(root)
for item in ['文件', '编辑', '设置', '书库', '插件', '关于']:
    menubar.add_command(label=item)

amenu = Menu(menubar)
bmenu = Menu(menubar)
cmenu = Menu(menubar)
dmenu = Menu(menubar)
emenu = Menu(menubar)
fmenu = Menu(menubar)

for item in ['导入文件夹', '导入文件', '打开文件', '关闭窗口', '退出']:
    amenu.add_command(lable=item)
for item in ['导入文件夹', '导入文件', '打开文件', '关闭窗口', '退出']:
    bmenu.add_command(lable=item)
for item in ['导入文件夹', '导入文件', '打开文件', '关闭窗口', '退出']:
    cmenu.add_command(lable=item)
for item in ['导入文件夹', '导入文件', '打开文件', '关闭窗口', '退出']:
    dmenu.add_command(lable=item)
for item in ['导入文件夹', '导入文件', '打开文件', '关闭窗口', '退出']:
    emenu.add_command(lable=item)
for item in ['导入文件夹', '导入文件', '打开文件', '关闭窗口', '退出']:
    fmenu.add_command(lable=item)

menubar.add_cascade(label="文件", menu=amenu)
menubar.add_cascade(label="编辑", menu=bmenu)
menubar.add_cascade(label="设置", menu=cmenu)
menubar.add_cascade(label="书库", menu=dmenu)
menubar.add_cascade(label="插件", menu=emenu)
menubar.add_cascade(label="关于", menu=fmenu)

root['menu'] = menubar
root.mainloop()
