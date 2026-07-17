import cv2
import mediapipe as mp
import json
import os

PROJECT_ROOT = os.path.dirname(
    os.path.dirname(__file__)
)

VIDEO_PATH = os.path.join(
    PROJECT_ROOT,
    "reference_data",
    "virat_cover_drive.mp4"
)

OUTPUT_PATH = os.path.join(
    PROJECT_ROOT,
    "reference_data",
    "virat_cover_drive_landmarks.json"
)

mp_pose = mp.solutions.pose

pose = mp_pose.Pose(
    static_image_mode=False,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

cap = cv2.VideoCapture(VIDEO_PATH)

if not cap.isOpened():
    print("Couldn't open video.")
    exit()

frames = []

frame_number = 0

while True:

    ret, frame = cap.read()

    if not ret:
        break

    frame_number += 1

    rgb = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2RGB
    )

    results = pose.process(rgb)

    if not results.pose_landmarks:
        continue

    landmarks = []

    for landmark in results.pose_landmarks.landmark:

        landmarks.append({

            "x": landmark.x,

            "y": landmark.y,

            "z": landmark.z,

            "visibility": landmark.visibility

        })

    frames.append({

        "frame": frame_number,

        "landmarks": landmarks

    })

cap.release()

with open(
    OUTPUT_PATH,
    "w"
) as file:

    json.dump(
        frames,
        file,
        indent=4
    )

print()
print("Reference extracted successfully.")
print(f"Frames saved: {len(frames)}")
print(f"Output: {OUTPUT_PATH}")