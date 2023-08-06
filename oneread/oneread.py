import cv2
import time
from CamClass import CameraCapture


class ONE(CameraCapture):
    def __init__(self,name,fps):
        super().__init__(fps)
        self.name = name


    def CAPTURE(self):
        while True:
            frame = self.capture_frame()

            if frame is not None:
                cv2.imshow(self.name,frame)
                time.sleep(self.slow)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break



