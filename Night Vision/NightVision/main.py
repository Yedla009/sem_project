import cv2
import numpy as np
from matplotlib import pyplot as plt


def hist_match(source, target):
    old_shape = source.shape
    source = source.ravel()
    target = target.ravel()

    s, ind = np.unique(source, return_inverse='true')

    hist = cv2.calcHist([source], [0], None, [256], [0, 256])
    source_cdf = hist.cumsum()
    source_cdf = source_cdf / source_cdf.max()

    hist = cv2.calcHist([target], [0], None, [256], [0, 256])
    target_cdf = hist.cumsum()
    target_cdf = target_cdf / target_cdf.max()

    interp_t_values = np.interp(source_cdf, target_cdf, range(0, 256))

    return interp_t_values[ind].reshape(old_shape)
# import numpy as np
def adaptive_histogram_equalization(img):

    # Convert to Lab color space
    lab = cv2.cvtColor(img, cv2.COLOR_BGR2Lab)

    # Split the channels
    l, a, b = cv2.split(lab)

    # Create a CLAHE object (with optional arguments)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))

    # Apply CLAHE to the L-channel
    cl = clahe.apply(l)

    # Merge the CLAHE enhanced L-channel back with the a and b channels
    limg = cv2.merge((cl, a, b))

    # Convert back to BGR color space
    final_img = cv2.cvtColor(limg, cv2.COLOR_Lab2BGR)

    # Display the original and equalized image
    cv2.imwrite("enhanced_AHE.jpg", final_img)



img_dark = cv2.imread('Dark.jpg')
img_pink = cv2.imread('Pink.jpg')

img_dark[:, :, 0] = hist_match(img_dark[:, :, 0], img_pink[:, :, 0])
img_dark[:, :, 1] = hist_match(img_dark[:, :, 1], img_pink[:, :, 1])
img_dark[:, :, 2] = hist_match(img_dark[:, :, 2], img_pink[:, :, 2])

cv2.imwrite('enhanced_HE.jpg', img_dark)

img_dark = cv2.imread('Dark.jpg')
# Replace 'path_to_image.jpg' with the path to the image file you want to process
adaptive_histogram_equalization(img_dark)

