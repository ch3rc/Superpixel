"""
Author:     Cody Hawkins
Date:       4/27/21
Desc:       Implementation of SLIC pixels
            where user chooses the size of
            the pixel and the smoothness
"""
import os
import sys
import getopt
import tkinter
import cv2 as cv
import numpy as np
from slic_algo import get_slic


def usage():
    print("\n---------HELP-----------\n")
    print("Help message [-h or --help]")
    print("Choose the algorithm type [-a or --algorithm] [SLIC:1, SLICO:2, MSLIC:3] [default: 1]")
    print("Choose the average superpixel size measured in pixels [-s or --size] [default: 10]")
    print("Choose the enforcement of superpixel smoothness [-r or --ruler] [default 10.0]")
    print("Manually search for image rather than providing as input [-m or --manual")


def find_image(directory, filename):
    result = []
    for root, dir, files in os.walk(directory):
        if filename in files:
            result.append(os.path.join(root, filename))
    if len(result) == 0:
        assert False, "Filename does not exist!"

    return result[0]


def main():
    try:
        opts, args = getopt.getopt(
            sys.argv[1:],
            "hma:s:r:",
            ["help", "algorithm", "size", "ruler", "manual"])
    except getopt.GetoptError as err:
        print(err)
        sys.exit(1)

    path = "C:\\Users\\codyh\\Desktop\\Test Pics\\High Quality"
    algo = cv.ximgproc.SLIC
    size = 10
    rule = 10.0
    image = None
    manual = False

    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
            sys.exit(1)
        elif o in ("-a", "--algorithm"):
            if int(a) == 2:
                algo = cv.ximgproc.SLICO
            elif int(a) == 3:
                algo = cv.ximgproc.MSLIC
        elif o in ("-s", "--size"):
            size = int(a)
        elif o in ("-r", "--ruler"):
            rule = float(a)
        elif o in ("-m", "--manual"):
            import tkinter as tk
            from tkinter import filedialog

            root = tk.Tk()
            root.withdraw()
            image = filedialog.askopenfilename()
            manual = True
        else:
            assert False, "Unknown Option!"

    print(f"algorithm chosen {algo}")
    print(f"size chosen {size}")
    print(f"ruler chosen {rule}")
    if manual is False:
        image = find_image(path, args[0])
        try:
            img = cv.imread(image)
            if img is not None:
                get_slic(img, algo, size, rule)
            else:
                print("Image not found!")
        except cv.Error as e:
            print(e)
            sys.exit(2)
    elif manual is True:
        try:
            img = cv.imread(image)
            if img is not None:
                get_slic(img, algo, size, rule)
            else:
                print("Image not found!")
        except cv.Error as e:
            print(e)
            sys.exit(2)


if __name__=='__main__':
    main()