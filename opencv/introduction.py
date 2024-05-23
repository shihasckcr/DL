import cv2

img = cv2.imread('/home/shihas/Documents/DL/opencv/#2.jpg')
# print(img)
# img2=cv2.imread('/home/shihas/Documents/DL/opencv/#2.jpg')

# cv2.imshow('image2',img2)
# cv2.imshow('image',img)
# cv2.waitKey()
# cv2.destroyAllWindows()

# to greyscale image
grey_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
(thresh,bw_img) = cv2.threshold(grey_img,128,255 ,cv2.THRESH_BINARY | cv2.THRESH_OTSU)
# print(thresh)

# to save 
cv2.imwrite('imgg.jpg',bw_img)

# cv2.imshow('image2',bw_img)
# cv2.waitKey()
# cv2.destroyAllWindows()

# to blacknwhite
# (thresh,bw_img) = cv2.threshold(grey_img,128,255 ,cv2.THRESH_BINARY )

# resize_image
# resized_img = cv2.resize(img,(200,200))
# print(img.shape) # shape of image(h,w,c)
# cv2.imshow('resize',resized_img)
# cv2.waitKey()
# cv2.destroyAllWindows()

# rectangle
# img5 = cv2.rectangle(img,pt1=(98,136),pt2=(202,105),color=(0,255,0),thickness=5) 
# for filled thickness=-1 or thickness=cv2.FILLED
# cv2.imshow('rect',img5)
# cv2.waitKey()
# cv2.destroyAllWindows()

# circle
# img6 = cv2.circle(img,center=(155,155),radius=150,color=(0,0,255),thickness=5)
# cv2.imshow('circ',img6)
# cv2.waitKey()
# cv2.destroyAllWindows()

# text
# img7 = cv2.putText(
#         img,
#         text='GOAT',
#         org=(155,100),
#         fontFace=cv2.FONT_HERSHEY_COMPLEX,
#         fontScale=2,
#         color=(0,255,0),
#         thickness=5)
# cv2.imshow('txt',img7)
# cv2.waitKey()
# cv2.destroyAllWindows()

img007 = cv2.rectangle(img,pt1=(20,96),pt2=(570,220),color=(0,0,255),thickness=-1)
img007 = cv2.circle(img,center=(475,155),radius=64,color=(0,255,0),thickness=-1)
img007 = cv2.putText(img,text='REAL MADRID',org=(25,155),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=2,color=(255,0,0),thickness=5)
# cv2.imshow('work',img007)
# cv2.waitKey()
# cv2.destroyAllWindows()


cv2.imwrite('new_img.jpg',img007)