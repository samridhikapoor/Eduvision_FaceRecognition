from distutils.command.bdist import bdist
from multiprocessing import parent_process
from tkinter import*
from tkinter import ttk
from tkinter import font
from PIL import Image, ImageTk
from tkinter import messagebox
from time import strftime
from datetime import datetime
import mysql.connector
import cv2
import os
import numpy as np

class Help:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        img=Image.open(r"FlexStart\assets\img\bg.jpg")
        img=img.resize((10000,10000), Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root, image=self.photoimg)
        f_lbl.place(x=0,y=0,width=10000,height=10000)

        title_lbl=Label(self.root, text="Log-Me-In : Simplifying Lives",font=("times new roman",35,"bold"), bg="white",fg="dark blue")
        title_lbl.place(x=0,y=20,width=1530, height=50)

        img2=Image.open(r"FlexStart\assets\img\contact.png")
        img2=img2.resize((1000,300), Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        bg_img=Label(self.root, image=self.photoimg2)
        bg_img.place(x=300,y=250,width=1000,height=300)


if __name__=="__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()