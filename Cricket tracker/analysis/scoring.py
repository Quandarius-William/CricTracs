class ShotScorer:


    def calculate(self, data):

        if data is None:
            return None


        score = 100


        # Head movement penalty

        if data["head_movement"] > 0.03:
            score -= 15


        # Front leg penalty

        if data["front_leg_angle"] != "N/A":

            angle = data["front_leg_angle"]

            if angle < 140 or angle > 170:
                score -= 15

        else:
            score -= 10


        if score < 0:
            score = 0


        return score