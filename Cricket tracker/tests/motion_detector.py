import cv2
import numpy as np
import time

# Open webcam
cap = cv2.VideoCapture(0)

# Check camera works
if not cap.isOpened():
    print("Cannot open camera")
    exit()

# Read first frame
ret, previous_frame = cap.read()

# FPS variables
previous_time = 0

while True:

    # Read current frame
    ret, frame = cap.read()

    if not ret:
        break


    # ----------------------------
    # 1. FIND DIFFERENCE
    # ----------------------------

    difference = cv2.absdiff(previous_frame, frame)


    # ----------------------------
    # 2. CONVERT TO GRAYSCALE
    # ----------------------------

    gray = cv2.cvtColor(
        difference,
        cv2.COLOR_BGR2GRAY
    )


    # ----------------------------
    # 3. REMOVE NOISE
    # ----------------------------

    blur = cv2.GaussianBlur(
        gray,
        (5,5),
        0
    )


    # ----------------------------
    # 4. CREATE BLACK/WHITE MASK
    # ----------------------------

    _, mask = cv2.threshold(
        blur,
        30,
        255,
        cv2.THRESH_BINARY
    )


    # ----------------------------
    # 5. MAKE OBJECTS CONNECTED
    # ----------------------------

    dilated = cv2.dilate(
        mask,
        None,
        iterations=3
    )


    # ----------------------------
    # 6. FIND OBJECTS
    # ----------------------------

    contours, _ = cv2.findContours(
        dilated,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )


    movement_detected = False


    for contour in contours:

        # Ignore tiny movements
        if cv2.contourArea(contour) < 1000:
            continue


        movement_detected = True


        # Get rectangle around movement
        x, y, width, height = cv2.boundingRect(contour)


        # Draw rectangle
        cv2.rectangle(
            frame,
            (x,y),
            (x+width,y+height),
            (0,255,0),
            3
        )


        # Label
        cv2.putText(
            frame,
            "Movement",
            (x,y-10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0,255,0),
            2
        )


    # ----------------------------
    # 7. FPS COUNTER
    # ----------------------------

    current_time = time.time()

    fps = 1 / (current_time - previous_time)

    previous_time = current_time


    cv2.putText(
        frame,
        f"FPS: {int(fps)}",
        (10,30),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (255,255,255),
        2
    )


    if movement_detected:
        cv2.putText(
            frame,
            "OBJECT MOVING",
            (10,70),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0,0,255),
            2
        )


    # Show camera
    cv2.imshow(
        "Motion Tracker",
        frame
    )


    # Show black/white detection
    cv2.imshow(
        "Movement Mask",
        mask
    )


    # Update previous frame
    previous_frame = frame.copy()


import cv2
import numpy as np
import time

# Open webcam
cap = cv2.VideoCapture(0)

# Check camera works
if not cap.isOpened():
    print("Cannot open camera")
    exit()

# Read first frame
ret, previous_frame = cap.read()

# FPS variables
previous_time = 0

while True:

    # Read current frame
    ret, frame = cap.read()

    if not ret:
        break


    # ----------------------------
    # 1. FIND DIFFERENCE
    # ----------------------------

    difference = cv2.absdiff(previous_frame, frame)


    # ----------------------------
    # 2. CONVERT TO GRAYSCALE
    # ----------------------------

    gray = cv2.cvtColor(
        difference,
        cv2.COLOR_BGR2GRAY
    )


    # ----------------------------
    # 3. REMOVE NOISE
    # ----------------------------

    blur = cv2.GaussianBlur(
        gray,
        (5,5),
        0
    )


    # ----------------------------
    # 4. CREATE BLACK/WHITE MASK
    # ----------------------------

    _, mask = cv2.threshold(
        blur,
        30,
        255,
        cv2.THRESH_BINARY
    )


    # ----------------------------
    # 5. MAKE OBJECTS CONNECTED
    # ----------------------------

    dilated = cv2.dilate(
        mask,
        None,
        iterations=3
    )


    # ----------------------------
    # 6. FIND OBJECTS
    # ----------------------------

    contours, _ = cv2.findContours(
        dilated,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )


    movement_detected = False


    for contour in contours:

        # Ignore tiny movements
        if cv2.contourArea(contour) < 1000:
            continue


        movement_detected = True


        # Get rectangle around movement
        x, y, width, height = cv2.boundingRect(contour)


        # Draw rectangle
        cv2.rectangle(
            frame,
            (x,y),
            (x+width,y+height),
            (0,255,0),
            3
        )


        # Label
        cv2.putText(
            frame,
            "Movement",
            (x,y-10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0,255,0),
            2
        )


    # ----------------------------
    # 7. FPS COUNTER
    # ----------------------------

    current_time = time.time()

    fps = 1 / (current_time - previous_time)

    previous_time = current_time


    cv2.putText(
        frame,
        f"FPS: {int(fps)}",
        (10,30),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (255,255,255),
        2
    )


    if movement_detected:
        cv2.putText(
            frame,
            "OBJECT MOVING",
            (10,70),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0,0,255),
            2
        )


    # Show camera
    cv2.imshow("Motion Tracker", frame)

    # Show black/white detection
    cv2.imshow("Movement Mask", mask)

    # Update previous frame
    previous_frame = frame.copy()

    # Wait for a key press
    key = cv2.waitKey(1) & 0xFF

    # Press Q or ESC to quit
    if key == ord("q") or key == 27:
        break

cap.release()
cv2.destroyAllWindows()
cap.release()
cv2.destroyAllWindows()