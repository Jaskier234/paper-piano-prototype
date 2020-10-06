import cv2
import requests
import numpy as np


class Keyboard():
    def __init__(self, capture, debug=False):
        self.capture = capture
        self.debug = debug

    def refresh(self):
        img_res = requests.get("http://192.168.1.101:8080/shot.jpg")
        img_arr = np.array(bytearray(img_res.content), dtype=np.uint8)
        frame = cv2.imdecode(img_arr, -1)
#       ret, laptop = self.capture.read()
        dot = cv2.imread('dot.png', 1)
        h, w, d = dot.shape

#       dot_match = cv2.matchTemplate(frame, dot, cv2.TM_CCOEFF)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        ret, thresh = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY_INV)  # + cv2.THRESH_OTSU)
        contours, hierarhy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        contour_img = np.zeros(frame.shape)
        cv2.drawContours(contour_img, contours, -1, (0, 255, 0), 1)
        print(contours)
#       blur = cv2.GaussianBlur(gray, (7, 7), 0)
#       blur = cv2.blur(img,(5,5))
#       kernel = np.array([
#           [0, 0, 0, 0, 0, 0, 0],
#           [0,  0, 0, 1, 0,  0, 0],
#           [0,  0, 1, 2, 1,  0, 0],
#           [0, 1, 2, 3, 2, 1, 0],
#           [0,  0, 1, 2, 1,  0, 0],
#           [0,  0, 0, 1, 0,  0, 0],
#           [0, 0, 0, 0, 0, 0, 0],
#           [-1, -1, -1, 0, -1, -1, -1],
#           [-1,  -1, 0, 1, 0,  -1, -1],
#           [-1,  0, 1, 2, 1,  0, -1],
#           [0, 1, 2, 3, 2, 1, 0],
#           [-1,  0, 1, 2, 1,  0, -1],
#           [-1,  -1, 0, 1, 0,  -1, -1],
#           [-1, -1, -1, 0, -1, -1, -1],
#               ])/49
#       dots = cv2.filter2D(invert, -1, kernel)
#       ret, img = cv2.threshold(blur, 100, 255, cv2.THRESH_BINARY_INV)  # + cv2.THRESH_OTSU)
#       img = cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
#           cv2.THRESH_BINARY,21,10)

        if self.debug:
            cv2.imshow('thresh', thresh)
            cv2.imshow('cont', contour_img)
#           cv2.imshow('diff', frame)
#           cv2.imshow('blur with threshold', img)

        # get points from frame
        # generate sequences based on points
        # calculate keys based on sequences

    def getNotes(self, finger_positions):
        pass


if __name__ == '__main__':
    cap = cv2.VideoCapture(0)
    k = Keyboard(cap, True)
    while(True):
        k.refresh()
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
