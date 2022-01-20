import cv2
import matplotlib.pyplot as plt
image = cv2.imread('Images/TCGA_CS_4941_19960909_1.tif')

# cv2.imshow("shiva", image)
# print('shape of the image is: ', image.shape)
plt.imshow(image)


cv2.waitKey(0)
cv2.destroyAllWindows()



