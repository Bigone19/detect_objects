import os
import cv2
import time

path = "/home/moby/Cascade_Classifier/neg/"
dirs = os.listdir(path)
n = 0

for f in dirs:
    old = path+dirs[n]
    new = path+str(n+1)+'.jpg'
    os.rename(old, new)
    n += 1
    
