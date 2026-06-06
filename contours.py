import cv2
cap = cv2.VideoCapture(0)
while True:
    ret , frame = cap.read()
    gray = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(src=gray,thresh=120,maxval=255,type=cv2.THRESH_BINARY)
    contours , heirarchy = cv2.findContours(thresh,mode=cv2.RETR_TREE,method=cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(image=frame,contours=contours,contourIdx=-1,color=(0,255,0),thickness=3)
    cv2.imshow("contour_webcam_live",frame)
    if cv2.waitKey(1) & 0xFF == ord('r'):
        break
cap.release()
cv2.destroyAllWindows()    