import cv2, time
#1. create an object. Zero for eksternal camera
video=cv2.VideoCapture(0)
#variable
a=0
while True:
    a= a + 1
    #3. Create a frame object
    check, frame = video.read()
    print(check)
    print(frame) #Representing image
#6. Converting to Grayscale
    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#4. Show the frame
    cv2.imshow("Capturing", gray)
#5. For press any key to out (milisecond)
    #cv2.waitKey(0)
#7. For playing
    key=cv2.waitKey(1)
    
    if key==ord('q'):
        break
        
print(a)
#2. Shutdown the Camera
video.release()
cv2.destroyAllWindows