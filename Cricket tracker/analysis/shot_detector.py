class ShotDetector:

    def __init__(self):
        self.recording = False
        self.shot_frames = []
        self.previous_wrist = None


    def start(self):
        self.recording = True
        self.shot_frames = []


    def add_frame(self, landmarks):

        if landmarks is None:
            return


        if self.recording:
            self.shot_frames.append(landmarks)


    def detect_movement(self, landmarks, mp_pose):

        if landmarks is None:
            return False


        wrist = landmarks[
            mp_pose.PoseLandmark.RIGHT_WRIST
        ]


        if self.previous_wrist is None:

            self.previous_wrist = (
                wrist.x,
                wrist.y
            )

            return False


        movement = (
            abs(wrist.x - self.previous_wrist[0])
            +
            abs(wrist.y - self.previous_wrist[1])
        )


        self.previous_wrist = (
            wrist.x,
            wrist.y
        )


        return movement > 0.05


    def stop(self):

        self.recording = False
        return self.shot_frames