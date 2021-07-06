import numpy as np
import matplotlib.pyplot as plt
import base64 as b64

def count_cars(serialdata):
    # 1. Read Video from pi which comes from uno Note the video comes in base64 format then, it is likely you decode it first
    # 2. Conver the video to grayscale format
    # 3. Either perform canny detection or thresholding on the grayscale frame
    # 4. Find all the contours in the video
    # 5. Filter the contours based on the contourArea
    # 6. Return the cont which is probably of the cars
    pass
