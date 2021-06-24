#import packages
import imutils
import cv2

#load the image and find out the Height, Width and Depth(RGB Color)
#Syntax: var = cv2.imread("<filename.png>")
image = cv2.imread("jp.png")
(h , w , d)  = image.shape
print ("width = {}, height = {}, depth = {}".format(w,h,d))

#display the image on the screen
#Syntax: var = cv2.imshow("<image title>",imageVariable)
cv2.imshow("Image", image)
cv2.waitKey(0)

# access the RGB pixel located at x=50, y=100, keepind in mind that
# OpenCV stores images in BGR order rather than RGB
(B, G, R) = image[100, 50]
print("R={}, G={}, B={}".format(R, G, B))

# extract a 100x100 pixel square ROI (Region of Interest) from the
# input image starting at x=320,y=60 at ending at x=420,y=160
roi = image[60:160, 320:420]
cv2.imshow("ROI", roi)
cv2.waitKey(0)

# resize the image to 200x200px, ignoring aspect ratio
# Syntax: var = cv2.resize(imageVariable , ratio(h,w))
resized = cv2.resize(image, (200, 200))
cv2.imshow("Fixed Resizing", resized)
cv2.waitKey(0)

# fixed resizing and distort aspect ratio so let's resize the width
# to be 300px but compute the new height based on the aspect ratio
# r = 300.0 / w 
# dim = (300, int(h * r))
# resized = cv2.resize(image, dim)
# cv2.imshow("Aspect Ratio Resize", resized)
# cv2.waitKey(0) 

# manually computing the aspect ratio can be a pain so let's use the
# imutils library instead
resized = imutils.resize(image, width=300)
cv2.imshow("Imutils Resize", resized)
cv2.waitKey(0)

# let's rotate an image 45 degrees clockwise using OpenCV by first
# computing the image center, then constructing the rotation matrix,
# and then finally applying the affine warp
# center = (w // 2, h // 2)
# M = cv2.getRotationMatrix2D(center, -45, 1.0)
# rotated = cv2.warpAffine(image, M, (w, h))
# cv2.imshow("OpenCV Rotation", rotated)
# cv2.waitKey(0)

# rotation using imutil but cropped out
# rotated = imutils.rotate(image, -45)
# cv2.imshow("Imutils Rotation", rotated)
# cv2.waitKey(0)

#rotation with complete image
rotated = imutils.rotate_bound(image, 45)
cv2.imshow("Imutils Bound Rotation", rotated)
cv2.waitKey(0)

# Gaussian Blur - To blur the image
# useful when reducing high frequency noise
# Larger kernels would yield a more blurry image. Smaller kernels will create less blurry images
# Syntax: var = cv2.GaussianBlur(imageVariable, (kernal,kernal), 0)
blurred = cv2.GaussianBlur(image, (11, 11), 0)
cv2.imshow("Blurred", blurred)
cv2.waitKey(0)

# draw a 2px thick red RECTANGLE surrounding the face
# Syntax: cv2.rectangle(imageVariable, (x,y of starting point), (x,y of ending point), (B,G,R) , thickness)
output = image.copy()
cv2.rectangle(output, (320, 60), (420, 160), (0, 0, 255), 2)
cv2.imshow("Rectangle", output)
cv2.waitKey(0)

# draw a blue 20px (filled in) CIRCLE on the image centered at x=300,y=150
# Syntax: cv2.circle(imageVariable, (x,y of center coordinate), radius , (B,G,R) , thickness)
output = image.copy()
cv2.circle(output, (300, 150), 20, (255, 0, 0), -1)
cv2.imshow("Circle", output)
cv2.waitKey(0)

# draw a 5px thick red LINE from x=60,y=20 to x=400,y=200
# Syntax: cv2.rectangle(imageVariable, (x,y of starting point), (x,y of ending point), (B,G,R) , thickness)
output = image.copy()
cv2.line(output, (60, 20), (400, 200), (0, 0, 255), 5)
cv2.imshow("Line", output)
cv2.waitKey(0)

# draw green TEXT on the image
# Syntax: cv2.putText(imageVariable, "<Text>", (x,y of starting point), font, font size, (B,G,R) , thickness)
output = image.copy()
cv2.putText(output, "OpenCV + Jurassic Park!!!", (10, 25), 
	cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
cv2.imshow("Text", output)
cv2.waitKey(0)

