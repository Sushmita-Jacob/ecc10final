import cv2
import numpy as np
from pupil_apriltags import Detector

# ---------------- SETTINGS ----------------

TARGET_ID = 12
TAG_SIZE = 0.204 # meters (measure your real printed tag!)

# Camera intrinsics (approximate — calibrate for better accuracy)
fx = 1000
fy = 1000
cx = 640
cy = 360
camera_params = (fx, fy, cx, cy)
# ------------------------------------------

cap = cv2.VideoCapture(0)

detector = Detector(families="tag36h11")

while True:
    ret, frame = cap.read()
    if not ret:
        break

gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)