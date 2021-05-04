"""
Author:     Cody Hawkins
Class:      CS6420
Desc:       SLIC Implementation
"""

import cv2 as cv
import numpy as np


def get_slic(image, algorithm, size, ruler):

    slicc = cv.ximgproc.createSuperpixelSLIC(image, algorithm, size, ruler)

    slicc.iterate(50) # test number of iterations

    mask_slic = slicc.getLabelContourMask()
    mask_inv_slic = cv.bitwise_not(mask_slic)

    label_slic = slicc.getLabels()
    number_slic = slicc.getNumberOfSuperpixels()

    img_slic = cv.bitwise_and(image, image, mask=mask_inv_slic)

    # cv.imshow("slicced up", img_slic)
    # cv.waitKey(0)
    # cv.destroyAllWindows()

    img = np.zeros_like(image)

    for label in np.unique(label_slic):
        indices = np.nonzero(label_slic == label)
        img[indices] = np.mean(image[indices], axis=0)

    cv.imshow("Original image", image)
    cv.imshow("SLIC Areas", img_slic)
    cv.imshow("Mean SLIC pixels", img)
    cv.waitKey(0)
    cv.destroyAllWindows()