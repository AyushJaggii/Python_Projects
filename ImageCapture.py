## Capture Images Using your Webcam.

# Import the OpenCV library
import cv2

# Create a VideoCapture object for capturing video from the default camera (0)
imgcapture = cv2.VideoCapture(0)
result = True


while(result):
    ret, frame = imgcapture.read()           # Read a frame from the camera
    cv2.imwrite("test.jpg", frame )          # Write the frame to a file named test.jpg
    result = False
    print("Image Clicked")

# Release the VideoCapture object to free up system resources
imgcapture.release()
