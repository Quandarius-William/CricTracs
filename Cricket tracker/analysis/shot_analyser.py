from analysis.shot_metrics import ShotMetrics


class ShotAnalyser:


    def __init__(self):

        self.metrics = ShotMetrics()



    def analyse(self, shot_frames):

        if not shot_frames:

            return None



        head_score = (
            self.metrics.calculate_head_stability(
                shot_frames
            )
        )



        return {

            "frames": len(shot_frames),

            "head_stability": head_score

        }