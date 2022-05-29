# Eduvision_FaceRecognition

## Table of Contents
1. [General Info](#general-info)
2. [Live Demo](#live-demo)
3. [Special configuration setting(s) to be followed at the time of installation of the project](#special-configuration-settings-to-be-followed-at-the-time-of-installation-of-the-project)
4. [Technologies](#technologies)
5. [Features](#features)
### General Info
***
**EDUVISION** is a one step solution for an educational institution to meet requirements of their day-to-day activities including:
1. Marking attendance of students/employees
2. Ensuring a "Secure" campus by allowing only the registered vehicles to enter the premises, 
3. Maintaining a COVID-19 safe ecosystem by ensuring that all present inside the campus wear masks at all time 
4. Allowing faculty to monitor the students' devices in real time in order to keep a check that they are alert and awake during virtual lectures.


**Working of EDUVISION**

**1. Log-Me-In**
It is a User-Friendly, Efficient and Cent Percent Reliable Software to LogIn and mark Attendance by Facial Recognition. The application requires creation of a database for all students as well as employees of the institution by the Admin. The database includes personal details as well as picture of the individual. Once the model is trained for the created dataset, the software detects the image of the individual along with the ID, Roll No and Name. Incase of any discrepancy, the Admin can manually enter the attendance, on request of the student/employee and update the records. All attendance records can be exported from the software in the form of a CSV File for further activities, if any. 

**2. SecureEx**
It is an Automated License Plate Recognition (ALPR) Sytem that is built to enhance the security within the campus. It ensures that only the vehicles registered in the institution's database are allowed inside the campus. A picture of the vehicle license plate is taken by the camera and is uploaded in the SecureEx software. The software verifies the number plate as registered/unregistered and accordingly allows/denies its entry. In case of a registered license plate, the software detects and records the licence plate number, its country of origin as well as the date and time of entry. Incase of a unregistered license plate, entry is denied inside the campus. The recorded data can later be exported in the form of a CSV File thereby minimising the human effort of manual checking.

**3. MaskEssentia**
This feature mainly focuses on limiting the spread of COVID-19 in the premises of the educational institution, by ensuring that all present inside the premises must wear a face mask at all times. The user needs to keep the face in the range of the web camera and the software will detect whether the user is wearing a mask or not and labels every image accordingly. In addition to this, MaskEssentia also provides latest news and statistics on the spread of COVID-19 globally.


**4. Smart-Attention**
This is the most impressive and first of its kind feature that allows the faculty to monitor the students devices in real time and keep a check that they are alert during virtual lectures. The software uses facial features like Eye Aspect Ratio and Mouth Aspect Ratio to detect closed eyes or yawn incase a student is sleepy or non-attentive during the on-going lectures. Smart-Attention has an inbuilt feature of giving a buzzer alarm so that the student is alerted as soon as he/she gets drowsy.


Agile Methodology was used for building this project. The best Agile practices adopted were :

* Proper Planning
* Keeping Product Backlog
* Maintaining a SPRINT Burndown and a PRODUCT Burndown.
* Adopting the concepts of relative estimation and velocity.

## Live Demo 
***

Demo Video: [https://youtu.be/MywlX0E_WVs](https://youtu.be/XBQSv4InpDw)

## Special configuration setting(s) to be followed at the time of installation of the project
***
1. A little intro about the installation. 
```
$ git clone https://github.com/Riyadevvarshney11/video-call-webapp.git
$ pip install -r requirements.txt
```
2. In order to run the entire project (Flask Application), Run the file main python file named : "myapp.py" that is present in the root directory of the project uploaded on GitHub. 
```
$ python myapp.py
```
3. For opening the Log-Me-In Facial Recognition Attendance system use folllowing login credentials:

> Username: s@gmail.com

> Password: 12345

4. I have created the project database in MySQL and hosted the same on Azure. I have made it publicly accessible. In case there is any issue in accessing the database, the following credentials may please be used:
```
user="engage2022"
password="Useme@123"
host="engage2022.mysql.database.azure.com"
port=3306
database="face_recognizer"
ssl_disabled=True
```

5. I was facing difficulty in installing the Package named : "dlib". The version used in the project can be downloaded from the following link:

[Download Dlib From here](https://github.com/datamagic2020/Install-dlib/raw/main/dlib-19.22.99-cp310-cp310-win_amd64.whl)

After xthe (.whl)file is downloaded, search for the path of the file in your local computer (In my case, it was downloaded in the "Downloads" folder). Then run the below command in the terminal to install dlib library. This version of dlib is compatible with the python version(3.10.4) that I have used in my project. NOTE: The path used in the snippet below is w.r.t. my local system. Kindly make the changes and add the path of the dlib library w.r.t. your system.
```
pip install "C:\Users\ektak\Downloads\C:\Users\ektak\Downloads\dlib-19.22.99-cp310-cp310-win_amd64.whl"
```


## Screenshots
***
### 1. EDUVISION Home Page
![eduvision](https://user-images.githubusercontent.com/83203229/170849771-6de9312a-952e-4e0b-beed-3ca1681461fc.PNG)

### 2. Log-Me-In Attendance by Facial Recognition
![Capture](https://user-images.githubusercontent.com/83203229/170849315-267a3766-e124-4014-9236-bd00e0d472e4.PNG)


### 3. SecureEx Automatic License Plate Recognition System
![1](https://user-images.githubusercontent.com/83203229/170849446-2efdaea2-211c-4b3b-a790-e88da421309f.PNG)


### 4. MaskEssentia mask detection
![mask (2)](https://user-images.githubusercontent.com/83203229/170849552-533ee675-3ed7-4e67-abc1-531e6480c032.PNG)

### 5. Smart-Attention<br>
![sleep](https://user-images.githubusercontent.com/83203229/170849734-8fa2f0a9-2997-42d4-ac71-a9e39ec94485.PNG)

## Technologies
***
A list of technologies used within the project:
* OpenCV 
* Tkinter
* Dlib
* Imutils
* PIL (Python Imaging Library)
* MySQL
* Scipy

## Features
***
**EDUVISION: Log-Me-In Features**
* Enables database creation by the Admin
* Enables Facial Recognition from the available database and marks attendance
* Provides a facility to the Admin to manually update attendance record, in case of any discrepancy
* Enables export of the attendance records in the form of a CSV Data file for any time use

**EDUVISION: SecureEx Features**
* Enables creation of database for all registered vehicles through their Licence Plates
* Recognizes the vehicles as "registered/unknown" vehicles and allows/refuses the entry into the campus premises
* Records the License Plate Number, Country of origin of the vehicle, the date and time of entry of the vehicle into the campus
* For unregistered vehicles, provides information of refusing entry through a pop up message on the website as well as email to the Admin
* Enables export of the vehicle entry records in the form of a CSV Data file for any-time use
* Minimises the human effort of manual checking of vehicle entry

**EDUVISION: MaskEssentia Features**
* Enables creation of a COVID-19 safe campus 
* Provides "Real time mask detection" for all who are present in the campus
* Provides an alert to the Admin incase people are not wearing masks in the campus
* Provides latest news and statistics on the spread of COVID-19 globally, for creating awareness

**EDUVISION: Smart-Attention Features**
* Enables the faculty to monitor the students' devices in real time and keep a check that they are alert during virtual lectures. 
* Uses facial features like "Eye Aspect Ratio" and "Mouth Aspect Ratio" to detect closed eyes or yawn incase a student is sleepy or non-attentive during the ongoing lectures. 
* Provides for a buzzer alarm so that the student is alerted as soon as he/she gets drowsy.

