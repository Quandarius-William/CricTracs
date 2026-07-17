import cv2
import mediapipe as mp
import sys
import os
import time

sys.path.append(
    os.path.dirname(
        os.path.dirname(__file__)
    )
)

from analysis.scoring import ShotScorer
from analysis.feedback import FeedbackEngine
from tracking.pose_tracker import PoseTracker
from analysis.technique import TechniqueAnalyser
from analysis.shot_detector import ShotDetector
from analysis.shot_analyser import ShotAnalyser


pose = PoseTracker()
technique = TechniqueAnalyser()
feedback_engine = FeedbackEngine()
scorer = ShotScorer()
shot_detector = ShotDetector()
shot_analyser = ShotAnalyser()


cap = cv2.VideoCapture(0)


# Recording states

countdown_active = False
recording = False

countdown_start = 0
recording_start = 0


countdown_seconds = 3
recording_seconds = 3


while True:

    ret, frame = cap.read()

    if not ret:
        break


    # Countdown

    if countdown_active:

        elapsed = time.time() - countdown_start

        remaining = (
            countdown_seconds
            -
            int(elapsed)
        )


        if remaining > 0:

            cv2.putText(
                frame,
                str(remaining),
                (250,250),
                cv2.FONT_HERSHEY_SIMPLEX,
                5,
                (0,255,0),
                8
            )


        else:

            countdown_active = False
            recording = True

            recording_start = time.time()

            shot_detector.start()



    # Pose processing

    frame, landmarks = pose.process(frame)



    # Record frames

    if recording:

        shot_detector.add_frame(
            landmarks
        )


        # Automatically stop after 3 seconds

        if time.time() - recording_start >= recording_seconds:

            recording = False


            shot_frames = (
                shot_detector.stop()
            )


            analysis = (
                shot_analyser.analyse(
                    shot_frames
                )
            )


            print(
                "SHOT ANALYSIS:"
            )

            print(
                analysis
            )



    # Technique analysis

    results = technique.analyse(
        landmarks,
        mp.solutions.pose
    )


    feedback = (
        feedback_engine.analyse(results)
    )


    if results:


        # Confidence label

        confidence = (
            results["leg_confidence"]
        )


        if confidence < 60:

            confidence_text = (
                "Not confident"
            )

        elif confidence <= 80:

            confidence_text = (
                "Confident"
            )

        else:

            confidence_text = (
                "Very confident"
            )


        cv2.putText(
            frame,
            f"Analysis: {confidence_text}",
            (10,40),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.9,
            (255,255,0),
            2
        )


        # Front leg angle

        if results["front_leg_angle"] != "N/A":

            leg_text = (
                f"Front leg angle: "
                f"{int(results['front_leg_angle'])}"
            )

        else:

            leg_text = (
                "Front leg angle: N/A"
            )


        cv2.putText(
            frame,
            leg_text,
            (10,80),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0,255,0),
            2
        )


        # Live shot quality

        score = scorer.calculate(
            results
        )


        if score is not None:

            cv2.putText(
                frame,
                f"Live Quality: {score}/100",
                (10,120),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0,255,255),
                2
            )



    # Feedback display

    if feedback:

        for i, message in enumerate(feedback):

            cv2.putText(
                frame,
                message,
                (10,180 + i*40),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0,255,255),
                2
            )



    # Recording indicator

    if recording:

        cv2.putText(
            frame,
            "RECORDING SHOT",
            (10,320),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0,0,255),
            2
        )



    cv2.imshow(
        "AI Cricket Coach",
        frame
    )



    key = cv2.waitKey(1) & 0xFF



    # Start shot capture

    if key == ord("s"):

        countdown_active = True

        countdown_start = time.time()



    if key == ord("q"):

        break



cap.release()
cv2.destroyAllWindows()