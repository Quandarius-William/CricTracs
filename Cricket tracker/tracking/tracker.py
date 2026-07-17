import cv2

def find_ball(mask):

    contours, _ = cv2.findContours(
        mask,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    if not contours:
        return None

    biggest = max(contours, key=cv2.contourArea)

    if cv2.contourArea(biggest) < 500:
        return None

    (x, y), radius = cv2.minEnclosingCircle(biggest)

    return int(x), int(y), int(radius)