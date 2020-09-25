import glob
import cv2
import os
import numpy as np

# Listing a path to the main image directory where all of the image boards is stored
image_directory = os.listdir("./KingDominoData/image_boards/")
print(image_directory)
# Defining an array responsible for holding the images which is going to be printed
all_images = []

# A loop, which is looping through all of the images to then display them in a sequence
for images in image_directory:
    image = cv2.imread("./KingDominoData/image_boards/" + str(images))
    all_images.append(image)
    cv2.imshow("img", image)
    print(all_images)
    cv2.waitKey(0)