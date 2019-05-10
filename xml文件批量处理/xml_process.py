# -*- coding: utf-8 -*-
"""
Created on Fri May 10 16:02:50 2019

@author: xk_wang
"""
import xml.dom.minidom
import os


def get_cordinates(path):
    DOMTree = xml.dom.minidom.parse(path)
    root = DOMTree.documentElement
    
    filename = root.getElementsByTagName("filename")[0]
    name = filename.childNodes[0].data
    print("name: ", name)
    
    objects = root.getElementsByTagName("object")
    
    f = open("坐标信息.txt", 'a')
    f.write(name + "\n")
    for each_object in objects:
        output = ""
        object_name = each_object.getElementsByTagName("name")[0]
        object_name = object_name.childNodes[0].data
        
        bndbox = each_object.getElementsByTagName('bndbox')[0]
        xmin = bndbox.getElementsByTagName('xmin')[0]
        xmin_data=xmin.childNodes[0].data
    
        ymin = bndbox.getElementsByTagName('ymin')[0]
        ymin_data=ymin.childNodes[0].data
    
        xmax = bndbox.getElementsByTagName('xmax')[0]
        xmax_data=xmax.childNodes[0].data
        
        ymax = bndbox.getElementsByTagName('ymax')[0]
        ymax_data=ymax.childNodes[0].data
        
        print("object name: {:}\nxmin:{:}\nymin:{:}\nxmax:{:}\nymax:{:}\n".format(object_name,
              xmin_data,ymin_data,xmax_data,ymax_data))
        output = object_name + ": " + xmin_data + " " + ymin_data + " " + xmax_data + " " + ymax_data + "\n"
        f.write(output)
    f.close()

def main():
    for filename in os.walk("Annotations"):
        for path in filename[2]:
            get_cordinates("Annotations/"+path)
     

if __name__ == '__main__':
    main()




        