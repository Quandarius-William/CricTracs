import math


class TechniqueAnalyser:

    def __init__(self):
        self.starting_head = None


    def calculate_angle(self, a, b, c):

        radians = (
            math.atan2(c.y - b.y, c.x - b.x)
            -
            math.atan2(a.y - b.y, a.x - b.x)
        )

        angle = abs(radians * 180.0 / math.pi)

        if angle > 180:
            angle = 360 - angle

        return angle


    def analyse(self, landmarks, mp_pose):

        if landmarks is None:
            return None


        # Head position
        nose = landmarks[
            mp_pose.PoseLandmark.NOSE
        ]
        if nose.visibility < 0.5:
            return {
                "head_position": "N/A",
                "head_movement": "N/A",
                "front_leg_angle": "N/A",
                "leg_confidence": 0
            }


        if self.starting_head is None:
            self.starting_head = (
                nose.x,
                nose.y
            )


        head_movement = (
            abs(nose.x - self.starting_head[0])
            +
            abs(nose.y - self.starting_head[1])
        )


        # Front leg analysis

        left_hip = landmarks[
            mp_pose.PoseLandmark.LEFT_HIP
        ]

        left_knee = landmarks[
            mp_pose.PoseLandmark.LEFT_KNEE
        ]

        left_ankle = landmarks[
            mp_pose.PoseLandmark.LEFT_ANKLE
        ]


        visibility_scores = [
            left_hip.visibility,
            left_knee.visibility,
            left_ankle.visibility
        ]


        leg_confidence = (
            sum(visibility_scores) / len(visibility_scores)
        ) * 100


        if leg_confidence > 50:

            front_leg_angle = self.calculate_angle(
                left_hip,
                left_knee,
                left_ankle
            )

        else:
            front_leg_angle = "N/A"


        return {
            "head_position": (
                nose.x,
                nose.y
            ),

            "head_movement": head_movement,

            "front_leg_angle": front_leg_angle,

            "leg_confidence": leg_confidence
        }