import numpy as np

# Camera
CAMERA_INDEX = 0

# Ball colour (yellow tennis ball)
LOWER_HSV = np.array([20, 100, 100])
UPPER_HSV = np.array([40, 255, 255])

# Ignore tiny blobs
MIN_AREA = 500

# Trail length
MAX_TRAIL = 30

PIXELS_PER_METRE = 100