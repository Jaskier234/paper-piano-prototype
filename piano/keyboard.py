import cv2
import requests
import numpy as np
from sequence import Sequence


class Keyboard():
    def __init__(self, debug=False):
        self.debug = debug

    @staticmethod
    def getPointsFromFrame(frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        canny = cv2.Canny(gray, 200, 100)

        MIN_BOX_SIZE = 3
        MAX_BOX_SIZE = 20

        def filter_contour(contour):
            left = min([point[0][0] for point in contour])
            right = max([point[0][0] for point in contour])
            top = min([point[0][1] for point in contour])
            bottom = max([point[0][1] for point in contour])

            d_hor = right - left
            d_ver = bottom - top

            return ((right - left) > MIN_BOX_SIZE and (bottom - top) > MIN_BOX_SIZE and
                    (right - left) < MAX_BOX_SIZE and (bottom - top) < MAX_BOX_SIZE and
                    abs(d_hor - d_ver) < 10)

        contours, hierarhy = cv2.findContours(canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        contour_img = frame.copy()
        filtered_contours = [contour for contour in contours if filter_contour(contour)]
        cv2.drawContours(contour_img, filtered_contours, -1, (255, 255, 0), 1)

        def getMarkPos(contour):
            left = min([point[0][0] for point in contour])
            right = max([point[0][0] for point in contour])
            top = min([point[0][1] for point in contour])
            bottom = max([point[0][1] for point in contour])

            return (int((left + right) / 2), int((top + bottom) / 2))

        return [getMarkPos(cont) for cont in filtered_contours]

    def refresh(self, frame):
        # get points from frame
        seq_frame = frame.copy()
        points = Keyboard.getPointsFromFrame(frame)
        for x, y in points:
            cv2.circle(frame, (x, y), 2, (0, 0, 255), 3)

        marks = Sequence(points).marks
        for x, y in marks:
            cv2.circle(seq_frame, (x, y), 2, (0, 0, 255), 3)

        if self.debug:
            cv2.imshow('frame', frame)
            cv2.imshow('seq_frame', seq_frame)
#           cv2.imshow('cont', contour_img)

        # generate sequences based on points
        # calculate keys based on sequences

    def getNotes(self, finger_positions):
        pass


if __name__ == '__main__':
    cap = cv2.VideoCapture(0)
    k = Keyboard(True)
    while(True):
        img_res = requests.get("http://192.168.1.101:8080/shot.jpg")
        img_arr = np.array(bytearray(img_res.content), dtype=np.uint8)
        frame = cv2.imdecode(img_arr, -1)
#       ret, frame = self.capture.read()

        k.refresh(frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
