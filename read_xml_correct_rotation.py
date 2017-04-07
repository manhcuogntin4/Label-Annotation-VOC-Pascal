import lxml.etree as et
import xml.etree.ElementTree as ET
import math
import cv2
import numpy as numpy
import imutils

from shutil import copyfile

def copy_file(file_input, file_output):
    copyfile(file_input, file_output)
    return file_output
def rotate_file_image(filename, Alpha):
    img=cv2.imread(filename,1)
    dst=imutils.rotate_bound(img,Alpha)
    w_n,h_n,d_n=dst.shape
    file_rotate_image=str(Alpha)+filename
    cv2.imwrite(file_rotate_image,dst)
    file_annotate=filename.replace("png", "xml")
    file_annotate_rotate=file_rotate_image.replace("png", "xml")
    copy_file(file_annotate,file_annotate_rotate)
    rotate_xml(file_annotate_rotate, Alpha,w_n, h_n)

def rotate_xml(filename, Alpha, w,h):
    """ Parse a PASCAL VOC xml file """
    Alpha=math.radians(Alpha)
    tree = ET.parse(filename)
    objects = []


    for st in tree.findall('size'):
        w=int(st.find("width").text) -1
        h=int(st.find("height").text) -1
        h_n=int(w*math.sin(Alpha) + h*math.cos(Alpha))
        w_n=int(h*math.sin(Alpha) + w*math.cos(Alpha))
        st.find("width").text=str(w_n)
        st.find("height").text=str(h_n)
        tree.write(filename)

    for obj in tree.findall('object'):
        # if not check(obj.find('name').text):
        #     continue
        obj_struct = {}
        obj_struct['name'] = obj.find('name').text
        bbox = obj.find('bndbox')
        obj_struct['bbox'] = [int(bbox.find('xmin').text) - 1,
                              int(bbox.find('ymin').text) - 1,
                              int(bbox.find('xmax').text) - 1,
                              int(bbox.find('ymax').text) - 1]
        # Read the original coordination
        x1=int(bbox.find('xmin').text)
        y1=int(bbox.find('ymin').text)
        x2=int(bbox.find('xmax').text)
        y2=int(bbox.find('ymax').text)
        # Transformation
        y1_t=int(y1*math.cos(Alpha) + x1*math.sin(Alpha))
        x1_t=int(x1*math.cos(Alpha) + y1*math.sin(Alpha)) 
        x2_t=int(x2*math.cos(Alpha) + y2*math.sin(Alpha))
        y2_t=int(y2*math.cos(Alpha) + x2*math.sin(Alpha))


        x1_n=int((x1*math.cos(Alpha)-y1*math.sin(Alpha)) + (w_n-y2*(1-math.tan(Alpha)))*math.sin(Alpha))
        x2_n=x1_n+int((x2-x1)*math.cos(Alpha)+(y2-y1)*math.sin(Alpha))
        y1_n=y1_t
        y2_n=y2_t
        if(y2_n>w_n):
            y2_n=w_n
        if(x2_n>h_n):
            x2_n=h_n
        bbox.find('xmin').text=str(x1_n)
        bbox.find('ymin').text=str(y1_n)
        bbox.find('xmax').text=str(x2_n)
        bbox.find('ymax').text=str(y2_n)
        tree.write(filename)


file_image="new1.png"
rotate_file_image(file_image,5)


#rotate_xml("test2.xml", 5)