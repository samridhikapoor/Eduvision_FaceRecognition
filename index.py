from tkinter import *
from flask import Flask,redirect, url_for,render_template,request
import os

def d_dtcn():
	root = Tk()
	root.configure(background = "white")

	def function1(): 
		os.system("python login.py ")
		exit()

	def function2(): 
		os.system("python drowsiness_detection.py --shape_predictor shape_predictor_68_face_landmarks.dat")
		exit()

	
		
	root.title("EDUVISION - Making Lives Simpler")
	Label(root, text="EDUVISION - Making Lives Simpler",font=("times new roman",20),fg="white",bg="dark blue",height=2).grid(row=2,rowspan=2,columnspan=5,sticky=N+E+W+S,padx=5,pady=10)
	Button(root,text="Click here to run Log-Me-In Face Recognition Attendance Application",font=("times new roman",20),bg="dark blue",fg='white',command=function1).grid(row=5,columnspan=5,sticky=W+E+N+S,padx=5,pady=5)
	Button(root,text="Click here to run Smart-Attention Application",font=("times new roman",20),bg="dark blue",fg='white',command=function2).grid(row=7,columnspan=5,sticky=W+E+N+S,padx=5,pady=5)
	Button(root,text="Exit",font=("times new roman",20),bg="dark blue",fg='white',command=root.destroy).grid(row=9,columnspan=5,sticky=W+E+N+S,padx=5,pady=5)

	root.mainloop()