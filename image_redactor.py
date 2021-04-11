import cv2
from logic import logical

class Image_redactor:
    #конструктор
    def __init__(self,image_name):
        self.img = self.get_image(image_name)
        self.logic = logical()
    #возвращает изображение как 3-х мерный массив
    def get_image(self,image_name):
        return cv2.imread(image_name)

    #демонстрирует изображение на waitKey милисекунд, если waitKey = 0, то изображение самостоятельно не закроеться
    def show(self,waitKey):
        cv2.imshow("image remake",self.img)
        cv2.waitKey(waitKey)

        