# from django.shortcuts import render
#
# Create your views here.
#
# 腾讯课堂
# 课题：艺术签名
# 1.用 Python 实现界面
# 2.界面操作实现功能逻辑
#
# 用到的模块和库
# tkinter---->图形库
# requests--->
# re
# pillow----->图形库
#

from tkinter import *
from tkinter import messagebox
import requests  # 爬虫经常用到
import re
from PIL import Image, ImageTk


# 功能逻辑模块
def show():
    start_url = 'http://www.uustv.com/'
    name = enter.get()
    if not name:
        messagebox.showinfo(title='警告', message='输入内容为空')
    else:
        data = {
            'word': name,
            'sizes': 60,
            'fonts': 'jfcs.ttf',
            'fontcolor': '#000000',
        }
        result = requests.post(url=start_url, data=data)
        result.encoding = 'utf-8'
        html = result.text
        reg = '<div class="tu">.*?<img src="(.*?)"/></div>'
        img_path = re.findall(reg, html)
        img_url = start_url + img_path[0]
        print(img_url)

        response = requests.get(url=img_url).content
        f = open('{}.gif'.format(name), 'wb')
        f.write(response)

        bm = ImageTk.PhotoImage(file='{}.gif'.format(name))
        lable2 = Label(root, image=bm)

        lable2.bm = bm

        lable2.grid(row=2, columnspan=2)


root = Tk()
root.title = '人如其名'
root.geometry('600x300')

lable = Label(root, text='签名', font=('华文行楷', 20), fg='red')
lable.grid()

enter = Entry(root, font=('微软雅黑', 22))
enter.grid(row=0, column=1)

button = Button(root, text='设计漂亮的名字', font=('微软雅黑', 20), command=show)
button.grid(row=1, column=0)

root.mainloop()
