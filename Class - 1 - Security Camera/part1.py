# Import necessary Libraries
# pip3 install opencv-python
import time
import cv2

# Get the video
webcam = cv2.VideoCapture(0)
width = int(webcam.get(3))
height = int(webcam.get(4))

# Explanation : cv2.VideoWriter_fourcc("M", "J", "P", "G") -> Motion-JPEG
videoStream = cv2.VideoWriter("face_detected.avi", cv2.VideoWriter_fourcc("M", "J", "P", "G"), 10, (width, height))

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

if webcam.isOpened() == False:
    print("Unable to read Camera feed")

font = cv2.FONT_HERSHEY_SIMPLEX
last_time = 0

while True:
    # Get image from camera
    ret, frame = webcam.read()

    if ret == True:
        gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Get the faces
        faces = face_cascade.detectMultiScale(gray_image)
        for (x, y, w, h) in faces:
            # Draw the rectangles on the screen
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)


        # Time Stamp
        current_time = time.asctime(time.localtime(time.time()))
        cv2.putText(frame, current_time, (10, 450), font, 0.98, (0, 0, 255), 2, cv2.LINE_AA)

        # Store face if there
        if time.time() - last_time > 5 and len(faces) > 0:
            # face_image = frame[y:y + h, x:x + w]
            last_time = time.time()
            cv2.imwrite(str(last_time) + "_face.jpg", frame)


        videoStream.write(frame)
        cv2.imshow("Face detection", frame)
        if cv2.waitKey(25) == ord('q'):
            break

webcam.release()
videoStream.release()
cv2.destroyAllWindows()
