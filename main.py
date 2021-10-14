# Usage
# python main.py --image imagefile
# import the necessary packages
import numpy as np
import cv2 as cv
import argparse


def adjust_gamma(image, gamma=1.0):
    # build a look up table mapping the pixel values [0, 255] to their adjusted gamma values
    invGamma = 1.0/gamma
    table = np.array([((i / 255.0) ** invGamma) * 255 for i in np.arange(0, 256)]).astype("uint8")

    # apply Gamma correction using the lookup table
    return cv.LUT(image, table)


# construct an argparse to parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help="path to input file", required=True, type=str)
args = vars(ap.parse_args())

# load the original image
original = cv.imread(args["image"])

# loop over various values of gamma
for gamma in np.arange(0.0, 3.5, 0.5):
    # When when gamma is 1 (because there will be no change)
    if gamma == 1:
        continue

    # apply gamma correction and show the image
    gamma = gamma if gamma > 0 else 0.1
    adjusted = adjust_gamma(original, gamma)
    cv.putText(adjusted, f"g={gamma}", (10, 30), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
    cv.imshow("images", np.hstack([original, adjusted]))
    cv.waitKey(0)
