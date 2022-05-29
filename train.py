from distutils.command.bdist import bdist
from multiprocessing import parent_process
from tkinter import*
from tkinter import ttk
from tkinter import font
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class Train:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        img=Image.open(r"FlexStart\assets\img\bg.jpg")
        img=img.resize((10000,10000), Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root, image=self.photoimg)
        f_lbl.place(x=0,y=0,width=10000,height=10000)

        title_lbl=Label(self.root, text="TRAIN DATASET",font=("times new roman",35,"bold"), bg="white",fg="dark blue")
        title_lbl.place(x=0,y=20,width=1530, height=45)

        img_top=Image.open(r"FlexStart\assets\img\train_data_img.jpg")
        img_top=img_top.resize((500,400), Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root, image=self.photoimg_top,bg="light blue")
        f_lbl.place(x=500,y=170,width=500,height=400)

        b1_1=Button(self.root,text="Click here to Train Data",command=self.train_classifier,cursor="hand2", font=("times new roman",15,"bold"), bg="dark blue",fg="white")
        b1_1.place(x=655,y=600,width=220,height=40)

    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L')
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training data",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)

        #training the classifier
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Dataset Trained Successfully")






if __name__=="__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()