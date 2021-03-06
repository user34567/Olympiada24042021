import cv2
from logic import logical
from constants import texture_human
from constants import view_behind
import numpy as np

class Image_redactor:
    #конструктор
    def __init__(self,image_name):
        self.img = self.get_image(image_name)
        self.logic = logical(self)
        self.current_img = cv2.imread(view_behind)
    #возвращает изображение как 3-х мерный массив
    def get_image(self,image_name):
        return cv2.imread(image_name)

    #демонстрирует изображение на waitKey милисекунд, если waitKey = 0, то изображение самостоятельно не закроеться
    def show(self,waitKey):
        cv2.imshow("image remake",self.img)
        cv2.waitKey(waitKey)

    #получает координаты человека и возвращает точки для его отрисовки 
    def get_human_dots(self,x,y):
        dots = []
        th = texture_human
        for yc in range(len(th)):
            for xc in range(len(th[0])):
                if th[yc][xc] != None:
                    color = th[yc][xc]
                    dot = [x + xc - len(th[0])//2,y+ yc - len(th)//2,color]
                    dots.append(dot)
        return dots

    #изменяет точки на рисунке self.img
    def paint_dots(self,dots):
        for dot in dots:
            x = dot[0]
            y = dot[1]
            color = dot[2]
            self.img[y][x] = color

    #изменяет точки на  рисунке self.current_img
    def drowconture(self,approx):
        cv2.drawContours(self.current_img, [approx], -1, (0, 255, 0), 4)


    def find_people(self,imgname):
        
        frame = cv2.imread(imgname)
        hog = cv2.HOGDescriptor()
        hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
        gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        boxes, weights = hog.detectMultiScale(frame, winStride=(8,8) )
        boxes = np.array([[x, y, x + w, y + h] for (x, y, w, h) in boxes])
        for (xA, yA, xB, yB) in boxes:
            cv2.rectangle(frame, (xA, yA), (xB, yB),(0, 255, 0), 2)

        #frame.write(frame.astype('uint8'))

        print(frame)
        cv2.imshow('frame',frame)
        cv2.waitKey(0)