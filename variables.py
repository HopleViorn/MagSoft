import numpy as np
import pickle
import cv2

mm_per_pix=1
rgb_mt=[]

base_img=np.zeros((1,1))
mag_lut=np.array([i for i in range(256)])
profile_area=None

resolution=(1,1)

currentTab=1

def setCurrentTab(tab):
    global currentTab
    currentTab=tab

def get_line_width():
    line_coe=360
    return resolution[1]/line_coe

def get_derivated_img(img):
    global base_img
    if base_img.shape != img.shape:
        base_img=cv2.resize(base_img,(img.shape[1],img.shape[0])).astype(np.uint8)
    return img-base_img

def update_mag_lut():
    rgb_mt.sort(key=lambda x:x.avg)
    j=0
    l=len(rgb_mt)
    print('\n')
    for i in range(256):
        if j<l-1 and rgb_mt[j+1].avg <= i:
            j+=1
        x0,x1=rgb_mt[j].avg,rgb_mt[j+1].avg
        y0,y1=rgb_mt[j].md,rgb_mt[j+1].md

        point=(i-x0)*(y1-y0)/(x1-x0)+y0
        mag_lut[i]=point

def save_to_file(file_path):
    file=open(file_path,'wb')
    content=(mm_per_pix,base_img,mag_lut)
    pickle.dump(content,file)

def load_from_file(file_path):
    global base_img
    global mm_per_pix
    global mag_lut
    file=open(file_path,'rb')
    content=pickle.load(file)
    mm_per_pix,base_img,mag_lut=content
    print(mm_per_pix)

