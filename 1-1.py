import cv2 as cv
import sys

img = cv.imread(r"C:\Users\user\Documents\llm-programming\soccer.jpg")

if img is None:
    sys.exit("Could not read the image.")   

print(img.shape)
cv.imshow("Super left half", img[0:img.shape[0], 0:int(img.shape[1]/2)])
cv.imshow("Center half", img[0:img.shape[0], int(img.shape[1]/4):int(3*img.shape[1]/4)])

cv.imshow("R channel", img[:,:,2])
cv.imshow("G channel", img[:,:,1])
cv.imshow("B channel", img[:,:,0])

cv.waitKey(0)
cv.destroyAllWindows()