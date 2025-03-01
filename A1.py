import cv2
import matplotlib.pyplot as plt

image = cv2.imread("example.jpg")

#convert bgr to rgb
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.imshow(image_rgb)
plt.title("rgb image")
plt.show()

#convert bgr to grayscale
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
plt.imshow(image_gray, cmap="gray")
plt.title("grayscale image")
plt.show()

#cropping the image
cropped_image = image[100:400,100:500]
cropped_rgb = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2RGB)
plt.imshow(cropped_rgb)
plt.title("cropped region")
plt.show()


