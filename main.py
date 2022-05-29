from tkinter import *
from tkinter import ttk
from tkinter import font
import os
import tkinter
from PIL import Image, ImageTk
from developer import Developer
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from help import Help



class Face_Recognition_System:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        img=Image.open(r"FlexStart\assets\img\bg.jpg")
        img=img.resize((10000,10000), Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root, image=self.photoimg)
        f_lbl.place(x=0,y=0,width=10000,height=10000)

        img2=Image.open(r"FlexStart\assets\img\bg.jpg")
        img2=img2.resize((10000,10000), Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        bg_img=Label(self.root, image=self.photoimg2)
        bg_img.place(x=0,y=0,width=10000,height=10000)

        title_lbl=Label(bg_img, text="Log-Me-In : FACE RECOGNITION ATTENDANCE SYSTEM",font=("times new roman",35,"bold"), bg="white",fg="dark blue")
        title_lbl.place(x=0,y=0,width=1530, height=45)

        img1=Image.open(r"FlexStart\assets\img\attendance.jpg")
        img1=img1.resize((220,220), Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        b1=Button(bg_img,image=self.photoimg1,command=self.student_details, cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Student details",command=self.student_details,cursor="hand2", font=("times new roman",15,"bold"), bg="dark blue",fg="white")
        b1_1.place(x=200,y=300,width=220,height=40)

        #detect face
        img5=Image.open(r"FlexStart\assets\img\face_recognition.jpg")
        img5=img5.resize((220,220), Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5, cursor="hand2",command=self.face_data)
        b1.place(x=500,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Face Detector", cursor="hand2",command=self.face_data, font=("times new roman",15,"bold"), bg="dark blue",fg="white")
        b1_1.place(x=500,y=300,width=220,height=40)

        #attendance 
        img6=Image.open(r"FlexStart\assets\img\att_home.jfif")
        img6=img6.resize((220,220), Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6, cursor="hand2",command=self.attendance)
        b1.place(x=800,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Attendance", cursor="hand2",command=self.attendance, font=("times new roman",15,"bold"), bg="dark blue",fg="white")
        b1_1.place(x=800,y=300,width=220,height=40)

        #helpdesk
        img7=Image.open(r"FlexStart\assets\img\helpdesk.jfif")
        img7=img7.resize((220,220), Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7, cursor="hand2",command=self.help_data)
        b1.place(x=1100,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Help Desk", cursor="hand2",command=self.help_data, font=("times new roman",15,"bold"), bg="dark blue",fg="white")
        b1_1.place(x=1100,y=300,width=220,height=40)

        #train face detector
        img8=Image.open(r"FlexStart\assets\img\trainmodel.jfif")
        img8=img8.resize((220,220), Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8, cursor="hand2",command=self.train_data)
        b1.place(x=200,y=400,width=220,height=220)

        b1_1=Button(bg_img,text="Train the Model", cursor="hand2",command=self.train_data, font=("times new roman",15,"bold"), bg="dark blue",fg="white")
        b1_1.place(x=200,y=600,width=220,height=40)

        #photos face button
        img9=Image.open(r"FlexStart\assets\img\camera.jfif")
        img9=img9.resize((220,220), Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9, cursor="hand2",command=self.open_img)
        b1.place(x=500,y=400,width=220,height=220)

        b1_1=Button(bg_img,text="Captured Photos",command=self.open_img, cursor="hand2", font=("times new roman",15,"bold"), bg="dark blue",fg="white")
        b1_1.place(x=500,y=600,width=220,height=40)

        #developers page button
        img10=Image.open(r"FlexStart\assets\img\developers.jfif")
        img10=img10.resize((220,220), Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10, cursor="hand2",command=self.developer_data)
        b1.place(x=800,y=400,width=220,height=220)

        b1_1=Button(bg_img,text="About Log-Me-In", cursor="hand2",command=self.developer_data, font=("times new roman",15,"bold"), bg="dark blue",fg="white")
        b1_1.place(x=800,y=600,width=220,height=40)

        #exit page button
        img11=Image.open(r"FlexStart\assets\img\exit.jfif")
        img11=img11.resize((220,220), Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimg11, cursor="hand2",command=self.iExit)
        b1.place(x=1100,y=400,width=220,height=220)

        b1_1=Button(bg_img,text="Exit the Application", cursor="hand2",command=self.iExit, font=("times new roman",15,"bold"), bg="dark blue",fg="white")
        b1_1.place(x=1100,y=600,width=220,height=40)

    def open_img(self):
        os.startfile("data")

    #functions

    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)
    
    def attendance(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)

    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)

    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure you want to exit the Application?",parent=self.root)
        if self.iExit>0:
            self.root.destroy()
        else:
            return
        


if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()