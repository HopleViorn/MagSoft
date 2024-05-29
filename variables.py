import numpy as np
import pickle
import cv2
from PyQt5 import QtCore, QtGui, QtWidgets

mm_per_pix=1

length_cali_model=None
length_cali_array=np.zeros((0,2))

def mag_recovery(array):
    global mag_cali_model
    if mag_cali_model is None:
        mag_cali_model=QtGui.QStandardItemModel(0,2)
    else:
        mag_cali_model.setRowCount(0)
    model=mag_cali_model
    model.setHorizontalHeaderLabels(['pixel mag','actual mag'])
    for i in range(array.shape[0]):
        n_row  = model.rowCount()
        model.setItem(n_row,0,QtGui.QStandardItem('{:.4f}'.format(array[i,0])))
        model.setItem(n_row,1,QtGui.QStandardItem('{:.4f}'.format(array[i,1])))

def len_recovery(array):
    global length_cali_model
    if length_cali_model is None:
        length_cali_model=QtGui.QStandardItemModel(0,2)
    else:
        length_cali_model.setRowCount(0)
    model=length_cali_model
    model.setHorizontalHeaderLabels(['pixel mag','actual mag'])
    for i in range(array.shape[0]):
        n_row  = model.rowCount()
        model.setItem(n_row,0,QtGui.QStandardItem('{:.4f}'.format(array[i,0])))
        model.setItem(n_row,1,QtGui.QStandardItem('{:.4f}'.format(array[i,1])))

def add_length_point(pix,l):
    if l is None:
        l=0
    global length_cali_model
    n_row=length_cali_model.rowCount()
    length_cali_model.setItem(n_row,0, QtGui.QStandardItem('{:.4f}'.format(pix)))
    length_cali_model.setItem(n_row,1, QtGui.QStandardItem('{:.4f}'.format(l)))

mag_cali_model=None
mag_cali_array=np.zeros((0,2))
def add_mag_point(pix,s):
    global mag_cali_model
    n_row=mag_cali_model.rowCount()
    mag_cali_model.setItem(n_row,0, QtGui.QStandardItem('{:.4f}'.format(pix)))
    mag_cali_model.setItem(n_row,1, QtGui.QStandardItem('{:.4f}'.format(s)))

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

def get_font_width():
    font_coe=60
    return resolution[1]/font_coe

def get_derivated_img(img):
    global base_img
    if base_img.shape != img.shape:
        base_img=cv2.resize(base_img,(img.shape[1],img.shape[0])).astype(np.uint8)
    return img-base_img

# TODO
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
    content=(base_img,length_cali_array,mag_cali_array)
    pickle.dump(content,file)

def load_from_file(file_path):
    global base_img
    global length_cali_array
    global mag_cali_array
    file=open(file_path,'rb')
    content=pickle.load(file)
    base_img,length_cali_array,mag_cali_array=content
    mag_recovery(mag_cali_array)
    len_recovery(length_cali_array)
