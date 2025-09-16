import cv2 as cv

drawing = False
ix, iy = -1, -1
fx, fy = -1, -1
rect_done = False

def draw_rectangle(event, x, y, flags, param):
    global ix, iy, fx, fy, drawing, rect_done, img, img_show

    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
        fx, fy = x, y
        img_show = img.copy()

    elif event == cv.EVENT_MOUSEMOVE:
        if drawing:
            img_show = img.copy()
            cv.rectangle(img_show, (ix, iy), (x, y), (0, 255, 0), 2)
            fx, fy = x, y

    elif event == cv.EVENT_LBUTTONUP:
        drawing = False
        fx, fy = x, y
        rect_done = True
        img_show = img.copy()
        cv.rectangle(img_show, (ix, iy), (fx, fy), (0, 255, 0), 2)

img = cv.imread(r'C:\Users\user\Documents\llm-programming\rose.png')
if img is None:
    print("오류: 이미지를 찾을 수 없거나 열 수 없습니다.")
    exit()
img_show = img.copy()

cv.namedWindow('Select ROI')
cv.setMouseCallback('Select ROI', draw_rectangle)

while True:
    cv.imshow('Select ROI', img_show)
    key = cv.waitKey(1) & 0xFF
    if rect_done:
        break
    if key == 27:  # ESC 누르면 종료
        cv.destroyAllWindows()
        exit()

# 좌상단, 우하단 좌표 정렬
x1, y1 = min(ix, fx), min(iy, fy)
x2, y2 = max(ix, fx), max(iy, fy)

patch = img[y1:y2, x1:x2, :]
h, w = patch.shape[:2]

scale = 5  # 확대 배율

patch1 = cv.resize(patch, dsize=(w*scale, h*scale), interpolation=cv.INTER_NEAREST)
patch2 = cv.resize(patch, dsize=(w*scale, h*scale), interpolation=cv.INTER_LINEAR)
patch3 = cv.resize(patch, dsize=(w*scale, h*scale), interpolation=cv.INTER_CUBIC)

cv.imshow('Resize - Nearest', patch1)
cv.imshow('Resize - Linear', patch2)
cv.imshow('Resize - Cubic', patch3)

cv.waitKey()
cv.destroyAllWindows()