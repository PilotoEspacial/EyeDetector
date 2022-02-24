import cv2
import numpy as np


def drawingLines(contours,crop,rows,cols):

    for cnt in contours:
            (x, y, w, h) = cv2.boundingRect(cnt)
            
            #print("x,y,w,h:",x,y,w,h)
            if x>120 and (y<70 and y>55):
                cv2.putText(crop,'Up',(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),1,cv2.LINE_AA)
            elif x>rows/2 and y>90:
                cv2.putText(crop,'Left',(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),1,cv2.LINE_AA)
            elif (x>50 and x<75) and y<105:
                cv2.putText(crop,'Right',(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),1,cv2.LINE_AA)
            elif x<100 and y<120:
                cv2.putText(crop,'Down',(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),1,cv2.LINE_AA)

            cv2.rectangle(crop, (x,y), (x + w, y + h), (255, 0, 0),2)
            cv2.line(crop, (x + int(w/2), 0), (x + int(w/2),rows), (0, 0, 255), 2)
            cv2.line(crop, (0, y + int(h/2)), (cols, y + int(h/2)), (0, 0, 255), 2)
            break


def applyingGrayScale(crop):

        gray_crop = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)
        gray_crop = cv2.GaussianBlur(gray_crop, (7,7), 0)
        return gray_crop


def contoursCoordinates(gray_crop):

    _,thresholds = cv2.threshold(gray_crop, 5, 255, cv2.THRESH_BINARY_INV)
    contours, _ = cv2.findContours(thresholds,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
    print("FLAG-----------------------------------------------------------------")
    for countor in contours:
        for c in countor:
            print(c[0][0],",",c[0][1])
    contours = sorted(contours, key = lambda x:cv2.contourArea(x), reverse=True)
    return contours

def main():

    cap = cv2.VideoCapture("ojo1.mp4")

    while True: 
        ret, frame = cap.read()
        
        if ret is False:
            break
        
        crop = frame[200:450, 50:300]

        rows, cols, _ = crop.shape
        gray_crop = applyingGrayScale(crop)
        contours = contoursCoordinates(gray_crop)
        drawingLines(contours,crop,rows,cols)

        cv2.imshow("frame", crop)

        if cv2.waitKey(30) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()

if '__main__' == main():
    main()
