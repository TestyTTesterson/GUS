import cv2

cv2.namedWindow("GUS Vision")
burst = cv2.VideoCapture(0)

if burst.isOpened(): # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False

while rval:
    cv2.imshow("GUS Vision", frame)
    rval, frame = vc.read()
    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        break

vc.release()
cv2.destroyWindow("GUS Vision")
