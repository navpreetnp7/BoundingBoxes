import os  
import cv2

def folder(name, cpath):
    
    directory = name 
    parent_dir = cpath
        
    path = os.path.join(parent_dir, directory)
    os.mkdir(path)

#folder('Op','C:/Users/navpr/Desktop/PyTask')

def drawbb(im,x,y,w,h):

    start = ()


def coord(x,y,w,h):

    x = x+y

img = cv2.imread('C:/Users/navpr/Desktop/PyTask/Screenshot.png')
print(img.shape)
    
