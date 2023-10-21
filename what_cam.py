# find camera devices
import cv2 as cv

def find_camera():
    index = 0
    arr = []
    while True:
        cap = cv.VideoCapture(index)    # 0 -> index of camera: macbook webcam, 1: camostudio (for using phone etc)
        if not cap.isOpened():        # Check if camera opened successfully
            break
        else:
            arr.append(index)
        cap.release()
        index += 1
    return arr

print(find_camera())