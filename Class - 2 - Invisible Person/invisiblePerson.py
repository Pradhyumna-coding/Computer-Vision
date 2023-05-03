# Import necessary Libraries
import cv2
import time
# pip3 install numpy
import numpy as np

# Webcam
webcam = cv2.VideoCapture(0)
print("Taking Image of Background")
time.sleep(5)

# Get original Background
while True:
    ret, bg = webcam.read()
    if ret == True:
        break

width = int(webcam.get(3))
height = int(webcam.get(4))
# video = cv2.VideoWriter("video.avi", cv2.VideoWriter_fourcc("M", "J", "P", "G"), 10, (width, height))

while True:
    ret, frame = webcam.read()
    if ret == False:
        break
    # cv2.imwrite("captured.jpg",frame)

    # Convert to HSV -> Hue, Saturation, and Value
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Limits for the colour
    lower_red = np.array([0, 100, 20])
    upper_red = np.array([10, 255, 255])

    # Get Mask
    maskRed = cv2.inRange(hsv, lower_red, upper_red)
    # Morphological Transformation
    maskRed = cv2.morphologyEx(maskRed, cv2.MORPH_ERODE, np.ones((5, 5), np.uint8))
    maskRed = cv2.morphologyEx(maskRed, cv2.MORPH_DILATE, np.ones((5, 5), np.uint8))

    frame[np.where(maskRed == 255)] = 0

    background = bg.copy()
    background[np.where(maskRed == 0)] = 0

    # frame*alpha+background*beta + gamma
    final_img = cv2.addWeighted(frame, 1, background, 1, 0)

    cv2.imshow("Invisible Man", final_img)

    # Rvideo.write(final_img)
    if cv2.waitKey(12) == ord("s"):
        break

webcam.release()
cv2.destroyAllWindows()
# video.release()
