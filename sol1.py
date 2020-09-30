import os  
import cv2
import glob
from google.colab.patches import cv2_imshow
from xml.etree.ElementTree import Element, SubElement, Comment
#from ElementTree_pretty import prettify

def folder(name, cpath):
    directory = name 
    parent_dir = cpath

    path = os.path.join(parent_dir, directory)
    os.mkdir(path)
      
def xmllabel(fname, upath, w, h, d):
    top = Element('annotation')

    folder = SubElement(top, 'folder')
    folder.text = 'OutputLabels'

    filename = SubElement(top, 'filename')
    filename.text = fname

    path = SubElement(top, 'path')
    path.text = upath

    source = SubElement(top, 'source')
    database = SubElement(source, 'Unknown')
    database.text = upath

    size = SubElement(top, 'size')
    width = SubElement(size, 'width')
    width.text = w
    height = SubElement(size, 'height')
    height.text = h
    depth = SubElement(size, 'depth')
    depth.text = d


    #print prettify(top)
    return top

def xmlobj(top, x1, y1, x2, y2):
  object = SubElement(top, 'object')
  name = SubElement(size, 'name')
  name.text = 'nfpa'
  pose = SubElement(size, 'pose')
  pose.text = 'Unspecified'
  truncated = SubElement(size, 'truncated')
  truncated.text = '0'
  difficult = SubElement(size, 'difficult')
  difficult.text = '0'

  bndbox = SubElement(size, 'bndbox')
  xmin = SubElement(bndbox, 'xmin')
  xmin.text = x1
  ymin = SubElement(bndbox, 'ymin')
  ymin.text = y1
  xmax = SubElement(bndbox, 'xmax')
  xmax.text = x2
  ymax = SubElement(bndbox, 'ymax')
  ymax.text = y2

folder('OutputImages','/content')
folder('OutputLabels','/content')

path = '/content/Fol'


for infile in sorted(glob.glob( os.path.join(path, 'pos*.txt') )):

   # print ("current file is: " + infile)
   # xmllabel(os.path.basename(infile)
    if infile != "/content/Fol/pos-33.txt":
      continue
    file = open(infile,"r")
    #print(file.readline())
    k = 0
    for j in file.readlines():
      i = j.split()
      c = float(i[0])
      x = float(i[1])
      y = float(i[2])
      w = float(i[3])
      h = float(i[4])

      #print (infile[:-3]+'jpg')
      k += 1
      if(k == 1):
        img = cv2.imread(infile[:-3]+'jpg')

      
      x = x*img.shape[1]  
      y = y*img.shape[0]   
      w = w*img.shape[1]
      h = h*img.shape[0]

      xmax = int(x + w/2)
      xmin = int(x - w/2)
      ymax = int(y + h/2)
      ymin = int(y - h/2)

      cv2.rectangle(img,(int(xmin),int(ymin)),(int(xmax),int(ymax)),(0,0,255), 3)
    file.close()
    cv2_imshow(img)
    fname = os.path.basename(infile)
    print(fname)
    cv2.imwrite('/content/OutputImages/'+fname,img)


        
			
