from distutils.command.bdist import bdist
from multiprocessing import parent_process
from tkinter import*
from tkinter import ttk
from tkinter import font
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
from sqlalchemy import column
import os
import csv
from tkinter import filedialog


class Developer:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")


        img=Image.open(r"FlexStart\assets\img\bg.jpg")
        img=img.resize((10000,10000), Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root, image=self.photoimg)
        f_lbl.place(x=0,y=0,width=10000,height=10000)

        title_lbl=Label(self.root, text="ABOUT LOG-ME-IN",font=("times new roman",35,"bold"), bg="white",fg="dark blue")
        title_lbl.place(x=0,y=20,width=1530, height=50)

        img_top=Image.open(r"FlexStart\assets\img\about_us.png")
        img_top=img_top.resize((900,500), Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root, image=self.photoimg_top,bg="light blue")
        f_lbl.place(x=600,y=170,width=900,height=500)

        img2=Image.open(r"FlexStart\assets\img\about_left.jfif")
        img2=img2.resize((400,500), Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        bg_img=Label(self.root, image=self.photoimg2)
        bg_img.place(x=60,y=170,width=400,height=500)



if __name__=="__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()
