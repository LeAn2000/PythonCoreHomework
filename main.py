import cv2
import numpy as np
from matplotlib import pyplot as plt
import threading
from tkinter import *

# phương thước tạo map
root = Tk()
root.title("MultiThread in Python")
root.geometry("1000x800")
# điểm khởi tạo Map
label1 = Label(root, text="Nhập số điểm cần khởi tạo:",font=('Time New Roman',15))
label1.place(x=0, y=10)
my_text = Text(root, width=10, height=1)
my_text.insert(END ,100)
my_text.place(x=251 ,y=15)

####Chọn luồng
lb_chon_lg=Label(root,text="Chọn số luồng để chạy chương trình:",font=('Time New Roman',15))
lb_chon_lg.place(x=0,y=50)
r=IntVar()
r.set("1")
#laydl
def get_Data():
    x=int(my_text.get(1.0, END))
    return x
#chọn luồng Function
def Click_thread(value):
    #===================Data_train
    traindata = np.random.randint(0, 1000, (get_Data(), 2)).astype(np.float32)
    ketqua = np.random.randint(0, 3, (get_Data(), 1)).astype(np.float32)
    blue = traindata[ketqua.ravel() == 0]
    red = traindata[ketqua.ravel() == 1]
    yellow=traindata[ketqua.ravel() == 2]
    new_member = np.random.randint(0, 1000, (1, 2)).astype(np.float32)
    # show map function
    def show():
        plt.scatter(red[:, 0], red[:, 1], 50, 'r', 's')
        plt.scatter(blue[:, 0], blue[:, 1], 50, 'b', '<')
        plt.scatter(yellow[:, 0], yellow[:, 1], 50, 'y', '^')
        plt.scatter(new_member[:, 0], new_member[:, 1], 50, 'g', 'o')
        plt.show()

    btnshow=Button(root,text="Khởi tạo Map",font=('Time New Roman',10),command=show)
    btnshow.place(x=350, y=10)

    class myThread(threading.Thread):
        def __init__(self, name, couter):  # ghi đề hàm khởi tạo
            threading.Thread.__init__(self)
            self.name = name
            self.couter = couter

        def run(self):  # ghi đè hàm run
            # lb0=Label(mylist,text=f'Sẵn sàng chạy {self.name}',font=('Time New Roman',10))
            # lb0.pack()
            mylist.insert(END,f'Sẵn sàng chạy {self.name}')
            knn = cv2.ml.KNearest_create()
            knn.train(traindata, 0, ketqua)
            temp, result, hangxom, khoangcach = knn.findNearest(new_member, self.couter)
            if (result.astype(np.int32) == 1):
                # lb = Label(mylist, text="Red", bg="Red",font=('Time New Roman',15))
                # lb.pack()
                mylist.insert(END,f'Red')
            elif result.astype(np.int32) == 0:
                # lb = Label(mylist, text="Blue", bg="Blue",font=('Time New Roman',15))
                # lb.pack()
                mylist.insert(END, f'Blue')
            else:
                mylist.insert(END, f'Yellow')
            # lb1= Label(mylist,text=f'Hàng xóm của {self.name} là: {hangxom}',font=('Time New Roman',10))
            # lb2 = Label(mylist, text=f'Khoảng cách của {self.name} với các hàng xóm {khoangcach}',font=('Time New Roman',10))
            # lb3 = Label(mylist, text='kết thuc'+self.name,font=('Time New Roman',10))
            # lb1.pack()
            # lb2.pack()
            # lb3.pack()
            mylist.insert(END, f'Hàng xóm của {self.name} là: {hangxom}')
            mylist.insert(END, f'Khoảng cách của {self.name} với các hàng xóm {khoangcach}')
            mylist.insert(END, 'kết thuc'+self.name)

    if r.get()==1:
        Hide_All_Frame()
        frame_2luong.place(x=0,y=200)
        lbtext2l=Label(frame_2luong,text="Bạn chọn 2 luồng để thực hiện chương trình:",font=('Time New Roman',15))
        lbtext2l.place(x=0,y=0)
        lblg1=Label(frame_2luong,text="Luồng 1:")
        lblg2=Label(frame_2luong,text="Luồng 2:")
        tblg1=Text(frame_2luong,width=10,height=1)
        tblg2 = Text(frame_2luong, width=10, height=1)
        lblg1.place(x=0,y=35)
        tblg1.place(x=50, y=35)
        lblg2.place(x=150,y=35)
        tblg2.place(x=200, y=35)
        tblg1.insert(END, 1)
        tblg2.insert(END, 1)

        def Tinhtoan():
            try:
                # khởi tạo ThreaD


                l1 = int(tblg1.get(1.0, END))
                l2 = int(tblg2.get(1.0, END))
                thread1 = myThread("Thread 1", l1)
                thread2 = myThread("Thread 2", l2)
                thread1.start()
                thread2.start()

            except:
                print("lỗi thực hiện luồng chương trình")
        def reset():
            tblg1.delete(1.0,END)
            tblg2.delete(1.0,END)
            mylist.delete(0, END)
        btnTinh = Button(frame_2luong, text="Run",command=Tinhtoan)
        btnTinh.place(x=300, y=33,width=50)
        btnRS = Button(frame_2luong, text="Reset", command=reset)
        btnRS.place(x=400, y=33,width=50)


    elif r.get()==2:
        Hide_All_Frame()
        frame_4luong.place(x=0,y=200)
        lbtext4l = Label(frame_4luong, text="Bạn chọn 4 luồng để thực hiện chương trình:",font=('Time New Roman',15))
        lbtext4l.place(x=0, y=0)
        lblg1 = Label(frame_4luong, text="Luồng 1:")
        lblg2 = Label(frame_4luong, text="Luồng 2:")
        lblg3 = Label(frame_4luong, text="Luồng 3:")
        lblg4 = Label(frame_4luong, text="Luồng 4:")
        tblg1 = Text(frame_4luong, width=10, height=1)
        tblg2 = Text(frame_4luong, width=10, height=1)
        tblg3 = Text(frame_4luong, width=10, height=1)
        tblg4 = Text(frame_4luong, width=10, height=1)
        lblg1.place(x=0, y=35)
        tblg1.place(x=50, y=35)
        lblg2.place(x=150, y=35)
        tblg2.place(x=200, y=35)
        lblg3.place(x=300,y=35)
        tblg3.place(x=350,y=35)
        lblg4.place(x=450, y=35)
        tblg4.place(x=500, y=35)
        tblg1.insert(END, 1)
        tblg2.insert(END, 1)
        tblg3.insert(END, 1)
        tblg4.insert(END, 1)


        def Tinhtoan():
            try:
                # khởi tạo ThreaD
                l1 = int(tblg1.get(1.0, END))
                l2 = int(tblg2.get(1.0, END))
                l3 = int(tblg3.get(1.0, END))
                l4 = int(tblg4.get(1.0, END))
                thread1 = myThread("Thread 1", l1)
                thread2 = myThread("Thread 2", l2)
                thread3 = myThread("Thread 3", l3)
                thread4 = myThread("Thread 4", l4)
                thread1.start()
                thread2.start()
                thread3.start()
                thread4.start()

            except:
                print("lỗi thực hiện luồng chương trình")
        def reset():
            tblg1.delete(1.0,END)
            tblg2.delete(1.0,END)
            tblg3.delete(1.0, END)
            tblg4.delete(1.0, END)
            mylist.delete(0, END)
        btnTinh = Button(frame_4luong, text="Run", command=Tinhtoan)
        btnTinh.place(x=230, y=75,width=50)
        btnRS = Button(frame_4luong, text="Reset", command=reset)
        btnRS.place(x=300, y=75, width=50)


    else:
        Hide_All_Frame()
        frame_8luong.place(x=0,y=200)
        lbtext8l = Label(frame_8luong, text="Bạn chọn 8 luồng để thực hiện chương trình:",font=('Time New Roman',15))
        lbtext8l.place(x=0, y=0)
        lblg1 = Label(frame_8luong, text="Luồng 1:")
        lblg2 = Label(frame_8luong, text="Luồng 2:")
        lblg3 = Label(frame_8luong, text="Luồng 3:")
        lblg4 = Label(frame_8luong, text="Luồng 4:")
        lblg5 = Label(frame_8luong, text="Luồng 5:")
        lblg6 = Label(frame_8luong, text="Luồng 6:")
        lblg7 = Label(frame_8luong, text="Luồng 7:")
        lblg8 = Label(frame_8luong, text="Luồng 8:")
        tblg1 = Text(frame_8luong, width=10, height=1)
        tblg2 = Text(frame_8luong, width=10, height=1)
        tblg3 = Text(frame_8luong, width=10, height=1)
        tblg4 = Text(frame_8luong, width=10, height=1)
        tblg5 = Text(frame_8luong, width=10, height=1)
        tblg6 = Text(frame_8luong, width=10, height=1)
        tblg7 = Text(frame_8luong, width=10, height=1)
        tblg8 = Text(frame_8luong, width=10, height=1)
        lblg1.place(x=0, y=35)
        tblg1.place(x=50, y=35)
        lblg2.place(x=150, y=35)
        tblg2.place(x=200, y=35)
        lblg3.place(x=300, y=35)
        tblg3.place(x=350, y=35)
        lblg4.place(x=450, y=35)
        tblg4.place(x=500,y=35)
        lblg5.place(x=0, y=95)
        tblg5.place(x=50, y=95)
        lblg6.place(x=150, y=95)
        tblg6.place(x=200, y=95)
        lblg7.place(x=300, y=95)
        tblg7.place(x=350, y=95)
        lblg8.place(x=450, y=95)
        tblg8.place(x=500, y=95)
        tblg1.insert(END, 1)
        tblg2.insert(END, 1)
        tblg3.insert(END, 1)
        tblg4.insert(END, 1)
        tblg5.insert(END, 1)
        tblg6.insert(END, 1)
        tblg7.insert(END, 1)
        tblg8.insert(END, 1)

        def Tinhtoan():
            try:
                # khởi tạo ThreaD


                l1 = int(tblg1.get(1.0, END))
                l2 = int(tblg2.get(1.0, END))
                l3 = int(tblg3.get(1.0, END))
                l4 = int(tblg4.get(1.0, END))
                l5 = int(tblg5.get(1.0, END))
                l6 = int(tblg6.get(1.0, END))
                l7 = int(tblg7.get(1.0, END))
                l8 = int(tblg8.get(1.0, END))
                thread1 = myThread("Thread 1", l1)
                thread2 = myThread("Thread 2", l2)
                thread3 = myThread("Thread 3", l3)
                thread4 = myThread("Thread 4", l4)
                thread5 = myThread("Thread 5", l5)
                thread6 = myThread("Thread 6", l6)
                thread7 = myThread("Thread 7", l7)
                thread8 = myThread("Thread 8", l8)
                thread1.start()
                thread2.start()
                thread3.start()
                thread4.start()
                thread5.start()
                thread6.start()
                thread7.start()
                thread8.start()
            except:
                print("lỗi thực hiện luồng chương trình")
        def reset():
            tblg1.delete(1.0,END)
            tblg2.delete(1.0,END)
            tblg3.delete(1.0, END)
            tblg4.delete(1.0, END)
            tblg5.delete(1.0, END)
            tblg6.delete(1.0, END)
            tblg7.delete(1.0, END)
            tblg8.delete(1.0, END)
            mylist.delete(0,END)
        btnRS = Button(frame_8luong, text="Reset", command=reset)
        btnRS.place(x=300, y=150, width=50)
        btnTinh = Button(frame_8luong, text="Run", command=Tinhtoan)
        btnTinh.place(x=230, y=150,width=50)


#clear_frame
def Hide_All_Frame():
    for f2 in frame_2luong.winfo_children():
        f2.destroy()
    for f4 in frame_4luong.winfo_children():
        f4.destroy()
    for f8 in frame_8luong.winfo_children():
        f8.destroy()
    mylist.delete(0,END)
    frame_2luong.place_forget()
    frame_4luong.place_forget()
    frame_8luong.place_forget()



Radiobutton(root, text="2 Luồng",variable=r,font=('Time New Roman',10),command=lambda: Click_thread(r.get()), value=1).place(x=0,y=100)
Radiobutton(root, text="4 Luồng",variable=r,font=('Time New Roman',10),command=lambda: Click_thread(r.get()), value=2).place(x=0,y=120)
Radiobutton(root, text="8 Luồng",variable=r,font=('Time New Roman',10),command=lambda: Click_thread(r.get()), value=3).place(x=0,y=140)

#tạo frame cho từng luồng
frame_2luong=Frame(root,width=700,height=400)
frame_4luong=Frame(root,width=700,height=400)
frame_8luong=Frame(root,width=700,height=400)
#ScrollBar
scrollbarY = Scrollbar(root)
scrollbarY.pack( side = RIGHT, fill = Y )
scrollbarX = Scrollbar(root,orient = HORIZONTAL)
scrollbarX.pack( side = BOTTOM, fill = X )
mylist = Listbox(root, yscrollcommand = scrollbarY.set,xscrollcommand = scrollbarX.set, height=15, font=('Time New Roman',15), bg='#dedfda' )
mylist.pack(side=BOTTOM, fill = BOTH)
scrollbarY.config( command = mylist.yview )
scrollbarX.config( command = mylist.xview )
#--------------------------#
Label(root,text='Chú thích:',font=('Time New Roman',15)).place(x=600,y=10)
Label(root,text='Màu xanh gán nhãn là 0',font=('Time New Roman',15),bg='Blue').place(x=700,y=12)
Label(root,text='Màu đò gán nhãn là    1',font=('Time New Roman',15),bg='Red').place(x=700,y=42)
Label(root,text='Màu vàng gán nhãn là 2',font=('Time New Roman',15),bg='Yellow').place(x=700,y=72)
root.mainloop()