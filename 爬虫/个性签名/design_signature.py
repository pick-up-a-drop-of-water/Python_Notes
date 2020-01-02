import requests
import re
from urllib.request import urlretrieve
import tkinter as tk
from PIL import ImageTk
from tkinter import ttk
import os


type_font_dict = {'个性签': 'jfcs.ttf', '连笔签': 'qmt.ttf', '潇洒签': 'bzcs.ttf', '草体签': 'lfc.ttf',
                  '合文签': 'haku.ttf', '商务签': 'zql.ttf', '可爱签': 'yqk.ttf'}


def get_image(*arg):
    url = 'http://www.uustv.com'
    # 签名数据及类型
    name_designed = e1.get()
    type_name = combo_list.get()
    data = {'word': name_designed,
            'sizes': '60',
            'fonts': type_font_dict[type_name],
            'fontcolor': '#000000',
            }
    response = requests.post(url, data=data)
	# 自动识别网页编码
    response.encoding = response.apparent_encoding      
    # 正则匹配
    reg = re.compile('src="tmp/(.*?.gif)"')
    res = re.findall(reg, response.text)
    print(res)
    gif_url = 'http://www.uustv.com/tmp/' + res[0]
    print(gif_url)
    # 保存图片路径检验
    save_path = r'./' + '签名图片/'
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    gif_save_path = save_path + '{:}{}.gif'.format(name_designed, type_name)
	# 提取图片
    urlretrieve(url=gif_url, filename=gif_save_path)
	# 显示图片
    bm = ImageTk.PhotoImage(file=gif_save_path)
    l2 = tk.Label(win, image=bm)       
    l2.bm = bm
    l2.grid(row=1, columnspan=3)       # 跨3列显示，因为第三行有三个组件，这样显示才不会改变第一行的结构


if __name__ == '__main__':
    win = tk.Tk()
    # 宽 X 高
    win.geometry('540x260')
    win.title('专属个签')
	# 标签
    l1 = tk.Label(win, text='名字', font=('华文行楷', 20), width=6, fg='blue')
    l1.grid(row=0, column=0)        			# 放置位置
    default_name = tk.StringVar(value='李沁')
	# 文本框
    e1 = tk.Entry(win, text="", font=("华文行楷", 20), width=20, bd=10, fg='black', textvariable=default_name)
    e1.grid(row=0, column=2)
	# 列表框
    combo_list = ttk.Combobox(win, font=("华文行楷", 20), width=8)
    combo_list['values'] = ("个性签", "连笔签", "潇洒签", "草体签", "合文签", "商务签", "可爱签")
    combo_list.grid(row=0, column=1)
	# 设置列表框显示默认值
    combo_list.current(0)
    # 下拉列表选中时绑定事件
    combo_list.bind("<<ComboboxSelected>>", get_image)
    # 一直刷新
    win.mainloop()


