import cv2


class CameraCapture:
    def __init__(self,fps):
        self.cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        self.fps = fps
        self.slow = 1 / fps


    def capture_frame(self):
        ret, frame = self.cap.read()
        return frame
