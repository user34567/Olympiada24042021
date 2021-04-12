
import cv2
class logical:
    def __init__(self,ir):
        self.ir = ir

    def find_point(self):
        img = self.ir.current_img
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (3, 3), 0)
        edged = cv2.Canny(gray, 10, 250)
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))
        closed = cv2.morphologyEx(edged, cv2.MORPH_CLOSE, kernel)
        cnts = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
        
        for c in cnts:
            peri = cv2.arcLength(c, True)
            approx = cv2.approxPolyDP(c, 0.02 * peri, True)
            if len(approx) == 4:
                color = self.average_color(c,self.ir.current_img)
                if color[0] > 70 and color[0]< 80 and color[1] > 75 and color[1]< 85 and color[2] > 80 and color[2]< 90 :
                                                        #прверка на цвет
                    self.ir.drowconture(approx)
        cv2.imshow("sadsa",self.ir.current_img)
        cv2.waitKey(0)

    def get_distanse_to_door(self):
        pass

    def average_color(self,c,img):
        color = [0,0,0]
        for arr in c:
            xy = arr[0]
            x = xy[0]
            y = xy[1]
            for i in {0,1,2}:
                color[i] = color[i] + img[y][x][i]
        for i in {0,1,2}:
                color[i] = color[i]/len(c)
        return color

    
        



        
