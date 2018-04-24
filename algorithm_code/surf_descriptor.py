# -*- coding: utf-8 -*-

import sys
#reload(sys)
#sys.setdefaultencoding('utf-8')
import os
import cv2
import numpy as np


def calculateSURF(img, filename, n):
    '''img is result using cv2.imread()
        n is the number of cut line, should equal to  1 or 2
        can use np.save if don't know how to insert it into database
    '''
    image = img.copy()
    surf = cv2.xfeatures2d.SURF_create(900)# will chaneg based on version 
    #surf = cv2.SURF(900)  # if below 3.0, it is cv2.SURF(900)
    #calculate four different SURFs
    #First:
    kp1, des1 = surf.detectAndCompute(image,None)
    np.save('graph_surf2' + os.sep + filename + '_all', des1)
    #save this
    length = image.shape[1]
    width = image.shape[0]
    cut_partition = (n+1) 

    cut_length = int(length/cut_partition)

    for i in range(cut_partition):
        new_img = image[0:width, i*cut_length:(i+1)*cut_length]
        kp2 , des2 = surf.detectAndCompute(new_img, None)
        #save this for every iteration
        np.save('graph_surf2' + os.sep + filename + '_cut' + str(i+1), des2)

    move_window = int(cut_length/2)
    current = 0
    while ((current+1)*cut_length+move_window)<length:
        new_img = image[0:width, current*cut_length+move_window:(current+1)*cut_length+move_window]
        kp3 , des3 = surf.detectAndCompute(new_img, None)
        #save this for every iteration
        np.save('graph_surf2' + os.sep + filename + '_window' + str(current+1), des3)
        current += 1


if __name__ == '__main__':
    filenames = os.listdir('music graph')
    count = 1
    for filename in filenames:
        print (count, filename, 'start ...')
        path_file = 'music graph' + os.sep + filename
        img3 = cv2.imdecode(np.fromfile(path_file, dtype=np.uint8),1)
        #img3 = cv2.imread('music graph' + os.sep + filename)
        calculateSURF(img=img3, filename=filename, n=2)
        count += 1
        #break
    