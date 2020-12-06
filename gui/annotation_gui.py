import functools

import cv2

def printing(position):
    print(position)

class SimpleGUI:
    # only hogehoge

    def __init__(self, source_directory, window_name="hogehoge annotater"):
        self.window_name = window_name
        self.source_directory = source_directory

        self.image_list = list(self.source_directory.glob("**/*.jpg"))

        self.read_header = 0

    # @functools.lru_cache(maxsize=128)
    def read_image(self, path):
        img = cv2.imread(str(path))

        return img


    def run(self):
        # create window
        cv2.namedWindow(self.window_name, cv2.WINDOW_NORMAL)
        cv2.createTrackbar("image_id", 0, len(self.image_list)-1, printing)

        # read first image
        image_now = self.read_image(self.image_list[0])
        print(image_now.shape)
        cv2.imshow(self.window_name, image_now)

        while(True):
            k = cv2.waitKey(0)
            if k == ord('q'):
                break
            # key is "->", read and show next image
            elif k == 65364:
                self.read_header = min(self.read_header+1, len(self.image_list)+1)
                image_now = self.read_image(self.image_list[self.read_header])
                cv2.setTrackbarPos("image_id", self.window_name, self.read_header)
                cv2.imshow(self.window_name, image_now)

            # key is "<-", read and show past image
            elif k == 65361:
                self.read_header = max(self.read_header-1, 0)
                image_now = self.read_image(self.image_list[self.read_header])
                cv2.setTrackbarPos("image_id", self.window_name, self.read_header)
                cv2.imshow(self.window_name, image_now)

            # get trackbar pos and set to read_header if changed
            image_id_trackbar = cv2.getTrackbarPos("image_id", self.window_name)
            if image_id_trackbar != self.read_header:
                self.read_header = image_id_trackbar
                image_now = self.read_image(self.image_list[self.read_header])
                cv2.imshow(self.window_name, image_now)

        cv2.destroyWindow(self.window_name)












