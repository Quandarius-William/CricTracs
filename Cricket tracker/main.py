import cv2
import numpy as np
from analysis.shot_detector import ShotDetector
shot_detector = ShotDetector()
from tracking.tracker import find_ball
from ui.draw import draw_ball, draw_text
from tracking.speed import calculate_speed
import config


# Open camera
cap = cv2.VideoCapture(config.CAMERA_INDEX)
previous_position = None
previous_time = 0
previous_position = None
while True:

    ret, frame = cap.read()

    if not ret:
        break


    # Flip camera
    frame = cv2.flip(frame, 1)


    # Convert BGR to HSV
    hsv = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2HSV
    )


    # Detect yellow
    mask = cv2.inRange(
        hsv,
        config.LOWER_HSV,
        config.UPPER_HSV
    )


    # Find ball
    ball = find_ball(mask)


    if ball:

        x, y, radius = ball

        current_position = (x, y)


        speed, previous_time = calculate_speed(
            previous_position,
            current_position,
            previous_time
        )


        previous_position = current_position


        draw_ball(
           frame,
          x,
           y,
           radius
        )


        draw_text(
            frame,
            f"Speed: {int(speed)} km/h",
        )


    cv2.imshow(
        "Cricket Ball Tracker",
        frame
    )


    cv2.imshow(
        "Mask",
        mask
    )


    # Quit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


cap.release()
cv2.destroyAllWindows()