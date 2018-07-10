# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 12:41:30 2018

@author: HP
"""
import cv2
import os
from PIL import Image  
#this is used to check the extension of image
writing=open("C:/Users/HP/Desktop/data.csv",'w')
path="C:/Users/HP/Desktop/spcl/downloads"
f_path="C:/Users/HP/Desktop/spcl/f_images"
os.makedirs(f_path)
#directory for saving the file is created
c=0
dir=os.listdir(path)
#we get the sub directories present in the directory
j=0
for file in dir:
    path1=""
    path3=""
    path1=path+'/'+file

    path3=f_path+'/'+file
    #path1 corresponds to reading and path3 for saving the file
    os.makedirs(path3)
    #directory creation
    j=j+1
    k=0
    dir1=os.listdir(path1)
    for file1 in dir1:
        path2=""
        path2=path1+'/'+file1
        k=k+1
        path4=path3+'/'+str(k)
        #only strings could be added
        #print(path4)
        try:
            img = Image.open(path2)
            t=img.format
            #to check the format of the image
            print(t)
            if t=="JPEG":
                path4=path4+'.jpeg'
            if t=="PNG":
                    path4=path4+'.png'
            if t=="GIF":
                path4=path4+'.gif'
            if t=="MPO":
                path4=path4+'.mpo'
            reading=open(path2)    
            x=cv2.imread(path2)
            #image is read
            if x is not None:
                        resize_img = cv2.resize(x,(28,28), interpolation = cv2.INTER_AREA)
                        #image resized
                        gray = cv2.cvtColor(resize_img,cv2.COLOR_BGR2GRAY)
                        #resized image coverted to gray image
                        print(path4)
                        cv2.imwrite(path4,gray)
                        #image saved @path4
        except:
            print("file could not be read")
