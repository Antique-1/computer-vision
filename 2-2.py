import cv2 as cv
import sys  

img = cv.imread(r'C:\Users\user\Desktop\cv\girl_laughing.jpg')

if img is None:
    sys.exit("Could not read the image.")

def draw(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        cv.rectangle(img, (x, y), (x+200, y+200), (0, 0, 255), 2)
    elif event == cv.EVENT_RBUTTONDOWN:
        cv.circle(img, (x, y), 100, (255, 0, 0), 2)
    
        cv.imshow('Draw', img)

cv.namedWindow('Draw')
cv.imshow('Draw', img)

cv.setMouseCallback('Draw', draw)

while True:
    if cv.waitKey(1)==ord('q'):
        cv.destroyAllWindows()
        break

