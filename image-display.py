import cv2

img = cv2.imread("raspberries.jpeg")

# To resize the image
width = int(img.shape[1] * 0.25)
height = int(img.shape[0] * 0.25)
dim = (width, height)

resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
cv2.imshow('Raspberries', resized)

cv2.waitKey(0)
cv2.destroyAllWindows()

