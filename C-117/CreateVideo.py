import os
import cv2
path = "\Image"
images = []
for file in os.listdir(path):
    name,ext = os.path.splitext(file)
    if ext in ['.gif','.png','.jpg','.jpeg','.jfif']:
        file_name = path+"/"+file

        print(file_name)
        images.append(file_name)

        print(len(images))
        frame=cv2.imread(images[0])
        size= (width,height)
        frame.shape(size)
        out = cv2.VideoWriter('project.avi',cv2.VideoWriter_fourcc(*'DIVX'),0.8,size)
        count = len(images)
        for i in range(0,count-1):
            cv2.imread(images)
            out.write(images)



        