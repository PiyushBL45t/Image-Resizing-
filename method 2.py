import cv2
import sys

def change_height(scale):
    image = cv2.imread('mountain.jpg') # takes the image as an input
    cv2.imshow("Mountain", image) # shows the image

    print("The shape of the image is: ",image.shape)

    width = int(image.shape[0]) # change the width of the image according to the scale
    height = int(image.shape[1]*scale)# change the height of the image according to the scale

    # storing them in a tuple
    resolution = (width, height)
    print("Resolution of the converted image is: ",resolution)

    new_image = cv2.resize(image, resolution, interpolation = cv2.INTER_AREA)
    cv2.imshow('New Image', new_image)
    cv2.imwrite('converted.jpg', new_image) # to save the image in the current working directory
    print(new_image.shape)


    cv2.waitKey(0)
    cv2.destroyAllWindows()


   
def change_width(scale):
    image = cv2.imread('mountain.jpg') # takes the image as an input
    cv2.imshow("Mountain", image) # shows the image

    print("The shape of the image is: ",image.shape)

    width = int(image.shape[1]*scale) # change the width of the image according to the scale
    height = int(image.shape[0])# change the height of the image according to the scale

    # storing them in a tuple
    resolution = (width, height)
    print("Resolution of the converted image is: ",resolution)

    new_image = cv2.resize(image, resolution, interpolation = cv2.INTER_AREA)
    cv2.imshow('New Image', new_image)
    cv2.imwrite('converted.jpg', new_image) # to save the image in the current working directory
    print("The new shape of the image is: ", new_image.shape)


    cv2.waitKey(0)
    cv2.destroyAllWindows()
    

def main():
    print()
    
    choice = 1
    while choice != 0:
        print("1. Change the width of the image")
        print("2. Change the height of the image")
        print("3. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            scale = float(input("Enter the scale: "))
            change_width(scale)

        elif choice == 2:
            scale = float(input("Enter the scale: "))
            change_height(scale)

        elif choice == 3:
            sys.exit()

        else:
            print('Invalid choice')

main()