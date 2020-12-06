import functools
import shutil
import argparse
import os
import random

from pathlib import Path

import cv2
import numpy as np
import yaml

from gui.annotation_gui import SimpleGUI

supported_extension = ["jpg", "jpeg", "png"]
supported_feature = ["akaze"]

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='This is the python program for clustering images based on bag of words.')  # 2. パーサを作る

    parser.add_argument('param_file', help='the argment for a param file. Please set the path to xxx.yaml.')
    args = parser.parse_args()

    param_file = Path(args.param_file)

    with open(param_file) as file:
        params = yaml.safe_load(file)

    # gui = SimpleGUI(Path(params["source_directory"]))

    # cv2.imshow("frame", cv2.imread("/Users/moriyamasahiro/dataset/image/classification/256_ObjectCategories/001.ak47/001_0001.jpg"))
    # cv2.waitKey()

    cap = cv2.VideoCapture(0)

    while cap.isOpened():
        flags, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        print(gray.shape)
        cv2.imshow('img', gray)
        print("hoge")
        if cv2.waitKey(100):
            break

    cap.release()
    cv2.destroyAllWindows()

    # gui.run()
