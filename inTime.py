import os
import win32_setctime
import datetime
import math
import tkinter
from tkinter import filedialog


def file_select():
    input_box.delete(0,tkinter.END)
    create_box_Y.delete(0,tkinter.END)
    create_box_M.delete(0,tkinter.END)
    create_box_D.delete(0,tkinter.END)
    create_box_h.delete(0,tkinter.END)
    create_box_m.delete(0,tkinter.END)
    create_box_s.delete(0,tkinter.END)
    update_box_Y.delete(0,tkinter.END)
    update_box_M.delete(0,tkinter.END)
    update_box_D.delete(0,tkinter.END)
    update_box_h.delete(0,tkinter.END)
    update_box_m.delete(0,tkinter.END)
    update_box_s.delete(0,tkinter.END)
    access_box_Y.delete(0,tkinter.END)
    access_box_M.delete(0,tkinter.END)
    access_box_D.delete(0,tkinter.END)
    access_box_h.delete(0,tkinter.END)
    access_box_m.delete(0,tkinter.END)
    access_box_s.delete(0,tkinter.END)

    global file_path
    dir = os.path.abspath(os.path.dirname(__file__))
    file_path = tkinter.filedialog.askopenfilename(initialdir = dir)
    input_box.insert(tkinter.END, file_path)

    createTime_u=os.path.getctime(file_path)
    createTime_d=datetime.datetime.fromtimestamp(math.floor(createTime_u))
    create_box_Y.insert(tkinter.END, createTime_d.year)
    create_box_M.insert(tkinter.END, createTime_d.month)
    create_box_D.insert(tkinter.END, createTime_d.day)
    create_box_h.insert(tkinter.END, createTime_d.hour)
    create_box_m.insert(tkinter.END, createTime_d.minute)
    create_box_s.insert(tkinter.END, createTime_d.second)

    updateTime_u=os.path.getmtime(file_path)
    updateTime_d=datetime.datetime.fromtimestamp(math.floor(updateTime_u))
    update_box_Y.insert(tkinter.END, updateTime_d.year)
    update_box_M.insert(tkinter.END, updateTime_d.month)
    update_box_D.insert(tkinter.END, updateTime_d.day)
    update_box_h.insert(tkinter.END, updateTime_d.hour)
    update_box_m.insert(tkinter.END, updateTime_d.minute)
    update_box_s.insert(tkinter.END, updateTime_d.second)

    accessTime_u=os.path.getatime(file_path)
    accessTime_d=datetime.datetime.fromtimestamp(math.floor(accessTime_u))
    access_box_Y.insert(tkinter.END, accessTime_d.year)
    access_box_M.insert(tkinter.END, accessTime_d.month)
    access_box_D.insert(tkinter.END, accessTime_d.day)
    access_box_h.insert(tkinter.END, accessTime_d.hour)
    access_box_m.insert(tkinter.END, accessTime_d.minute)
    access_box_s.insert(tkinter.END, accessTime_d.second)

    message_label['text'] = 'ファイル選択中'


def change_time():
    try:
        create_time =datetime.datetime(year=int(create_box_Y.get()), month=int(create_box_M.get()), day=int(create_box_D.get()), hour=int(create_box_h.get()), minute=int(create_box_m.get()), second=int(create_box_s.get())).timestamp()
        update_time =datetime.datetime(year=int(update_box_Y.get()), month=int(update_box_M.get()), day=int(update_box_D.get()), hour=int(update_box_h.get()), minute=int(update_box_m.get()), second=int(update_box_s.get())).timestamp()
        access_time =datetime.datetime(year=int(access_box_Y.get()), month=int(access_box_M.get()), day=int(access_box_D.get()), hour=int(access_box_h.get()), minute=int(access_box_m.get()), second=int(access_box_s.get())).timestamp()
    except:
        message_label['text'] = '入力した時間がおかしい'
        return 0

    try:
        win32_setctime.setctime(file_path, create_time)
        os.utime(file_path, (access_time, update_time))
        message_label['text'] = '変更できたよ！'
    except:
        message_label['text'] = '時間変更できなかった...'
        return 0



root = tkinter.Tk()
root.title("ファイルの時間変更ツール")
root.geometry("360x260")

input_label = tkinter.Label(text="ファイルの名前")
input_label.place(x=10, y=10)

input_box = tkinter.Entry(width=40)
input_box.place(x=10, y=30)

select_button = tkinter.Button(text="ファイルを選ぶ",command=file_select)
select_button.place(x=10, y=50)


create_label = tkinter.Label(text="作成日時")
create_label.place(x=10, y=80)
create_box_Y = tkinter.Entry(width=5)
create_box_Y.place(x=10, y=100)
create_label_Y = tkinter.Label(text="年")
create_label_Y.place(x=40, y=100)
create_box_M = tkinter.Entry(width=3)
create_box_M.place(x=60, y=100)
create_label_M = tkinter.Label(text="月")
create_label_M.place(x=80, y=100)
create_box_D = tkinter.Entry(width=3)
create_box_D.place(x=100, y=100)
create_label_D = tkinter.Label(text="日")
create_label_D.place(x=120, y=100)
create_box_h = tkinter.Entry(width=3)
create_box_h.place(x=140, y=100)
create_label_h = tkinter.Label(text="時")
create_label_h.place(x=160, y=100)
create_box_m = tkinter.Entry(width=3)
create_box_m.place(x=180, y=100)
create_label_m = tkinter.Label(text="分")
create_label_m.place(x=200, y=100)
create_box_s = tkinter.Entry(width=3)
create_box_s.place(x=220, y=100)
create_label_s = tkinter.Label(text="秒")
create_label_s.place(x=240, y=100)

update_label = tkinter.Label(text="更新日時")
update_label.place(x=10, y=120)
update_box_Y = tkinter.Entry(width=5)
update_box_Y.place(x=10, y=140)
update_label_Y = tkinter.Label(text="年")
update_label_Y.place(x=40, y=140)
update_box_M = tkinter.Entry(width=3)
update_box_M.place(x=60, y=140)
update_label_M = tkinter.Label(text="月")
update_label_M.place(x=80, y=140)
update_box_D = tkinter.Entry(width=3)
update_box_D.place(x=100, y=140)
update_label_D = tkinter.Label(text="日")
update_label_D.place(x=120, y=140)
update_box_h = tkinter.Entry(width=3)
update_box_h.place(x=140, y=140)
update_label_h = tkinter.Label(text="時")
update_label_h.place(x=160, y=140)
update_box_m = tkinter.Entry(width=3)
update_box_m.place(x=180, y=140)
update_label_m = tkinter.Label(text="分")
update_label_m.place(x=200, y=140)
update_box_s = tkinter.Entry(width=3)
update_box_s.place(x=220, y=140)
update_label_s = tkinter.Label(text="秒")
update_label_s.place(x=240, y=140)

access_label = tkinter.Label(text="アクセス日時")
access_label.place(x=10, y=160)
access_box_Y = tkinter.Entry(width=5)
access_box_Y.place(x=10, y=180)
access_label_Y = tkinter.Label(text="年")
access_label_Y.place(x=40, y=180)
access_box_M = tkinter.Entry(width=3)
access_box_M.place(x=60, y=180)
access_label_M = tkinter.Label(text="月")
access_label_M.place(x=80, y=180)
access_box_D = tkinter.Entry(width=3)
access_box_D.place(x=100, y=180)
access_label_D = tkinter.Label(text="日")
access_label_D.place(x=120, y=180)
access_box_h = tkinter.Entry(width=3)
access_box_h.place(x=140, y=180)
access_label_h = tkinter.Label(text="時")
access_label_h.place(x=160, y=180)
access_box_m = tkinter.Entry(width=3)
access_box_m.place(x=180, y=180)
access_label_m = tkinter.Label(text="分")
access_label_m.place(x=200, y=180)
access_box_s = tkinter.Entry(width=3)
access_box_s.place(x=220, y=180)
access_label_s = tkinter.Label(text="秒")
access_label_s.place(x=240, y=180)


change_a_button = tkinter.Button(text="変更",command=change_time)
change_a_button.place(x=10, y=210)

message_label = tkinter.Label(text="ようこそ ver1.0")
message_label.place(x=10, y=235)


root.mainloop()
