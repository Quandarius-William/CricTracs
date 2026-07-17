import cv2


def draw_ball(frame, x, y, radius):

    cv2.circle(
        frame,
        (x, y),
        radius,
        (0, 255, 0),
        3
    )

    cv2.circle(
        frame,
        (x, y),
        5,
        (0, 0, 255),
        -1
    )


def draw_text(frame, text):

    cv2.putText(
        frame,
        text,
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (255,255,255),
        2
    )