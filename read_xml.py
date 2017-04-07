import lxml.etree as et
import xml.etree.ElementTree as ET
import math


def rotate_xml(filename, Alpha):
    """ Parse a PASCAL VOC xml file """
    Alpha=math.radians(Alpha)
    tree = ET.parse(filename)
    objects = []
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
        x1_n=x1+ int(y1*math.sin(Alpha))
        y1_n=y1-int(x1*math.sin(Alpha))
        x2_n=x2+int(y2*math.sin(Alpha))
        y2_n=y2-int(x2*math.sin(Alpha))
        print x1_n, y1_n, x2_n, y2_n, math.sin(Alpha), math.cos(Alpha)
        x1_new=x1_n
        y1_new=y1_n-int((x2-x1)*math.sin(Alpha)) 
        x2_new=x1_n+int((x2-x1)*math.cos(Alpha)+(y2-y1)*math.sin(Alpha))
        y2_new=y1_n+int((y2-y1)*math.cos(Alpha))
        bbox.find('xmin').text=str(x1_new)
        bbox.find('ymin').text=str(y1_new)
        bbox.find('xmax').text=str(x2_new)
        bbox.find('ymax').text=str(y2_new)
        tree.write(filename)
rotate_xml("test2.xml", 5)