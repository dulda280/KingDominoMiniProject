import glob
import cv2
import os
import numpy as np

image_directory = os.listdir("./KingDominoData/image_boards/")
print(image_directory)
all_images = []

for images in image_directory:
    image = cv2.imread("./KingDominoData/image_boards/" + str(images))
    # image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # image = cv2.resize(image, (100, 100))
    all_images.append(image)
    cv2.imshow("img", image)
    cv2.waitKey(0)

print(all_images)

# cv2.imshow(all_images[0])

# for y in all_images:
#     cv2.imshow(y, all_images)


# read_images = []
# for image in image_list:
#     read_images.append(cv2.imread(image, cv2.IMREAD_GRAYSCALE))
#
# cv2.imshow(read_images[0])

# cv2.imshow("image", read_images[0])


# def load_images(image_file_number):
#     image = cv2.imread(image_boards[image_file_number])
#     image_resized = cv2.resize(image, (100, 100))
#     return image, image_resized


# for image in image_path:
#     image = load_images(image_path)
#     cv2.imshow("Image", image)
