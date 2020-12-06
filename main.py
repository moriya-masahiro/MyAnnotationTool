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

    gui = SimpleGUI(Path(params["source_directory"]))

    gui.run()
