import imageio
import numpy as np
import scipy.ndimage
import matplotlib.pyplot as plt
imgaddress = input("Please enter the image location: ")
imgdestination = input(
    "Please enter the name of the image to save: ")
mysigma = input("Enter the sigma level (higher means more detail): ")
mysigma = int(mysigma)
start_img = imageio.imread(imgaddress)
gray_img = np.dot(start_img[..., :3], [0.299, 0.587, 0.114])
gray_inv_img = 255 - gray_img
inverted_img = gray_inv_img


def dodge(front, back):
    result = front * 256 / (256 - back)
    result[np.logical_or(result > 255, back >= 255)] = 255
    return result.astype('uint8')


blur_img = scipy.ndimage.filters.gaussian_filter(inverted_img, sigma=mysigma)
final_img = dodge(blur_img, gray_img)
plt.imshow(final_img, cmap='gray')
print("This is the preview of your image. Close this plot and it will save.")
plt.show()

# make sure the file exists
import os

if not os.path.exists(imgdestination):
    with open(imgdestination, 'w'):
        pass

plt.imsave(imgdestination, final_img, cmap='gray', vmin=0, vmax=255)
# plt.imsave(‘img2.png’, final_img, cmap=’gray’, vmin=0, vmax=255)
