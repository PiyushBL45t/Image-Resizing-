import cv2
import sys # importing the modules

def resize_image(scale):
    image = cv2.imread('Images/mountain.jpg') # takes the image as an input
    cv2.imshow("Mountain", image) # shows the image

    print("The shape of the image is: ", image.shape)

    width = int(image.shape[1]*scale) # change the width of the image according to the scale
    height = int(image.shape[0]*scale) # change the height of the image according to the scale

    # storing them in a tuple
    resolution = (width, height)
    print("Resolution of the converted image is: ",resolution)

    new_image = cv2.resize(image, resolution, interpolation = cv2.INTER_AREA)
    cv2.imshow('New Image', new_image)
    cv2.imwrite('converted.jpg', new_image) # to save the image in the current working directory
    print(new_image.shape)


    cv2.waitKey(0)
    cv2.destroyAllWindows()


def main():
    scale = float(input('Enter the scale of the image: ')) 
    resize_image(scale)
    sys.exit() # to saely exit the system

main()

