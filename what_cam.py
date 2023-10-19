# find camera devices
import cv2 as cv

def find_camera():
    index = 0
    arr = []
    while True:
        cap = cv.VideoCapture(index)
        if not cap.read()[index]:
            break
        else:
            arr.append(index)
        cap.release()
        index += 1
    return arr

print(find_camera())