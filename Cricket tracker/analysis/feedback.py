class FeedbackEngine:


    def analyse(self, data):

        feedback = []


        if data is None:
            return ["No player detected"]


        # Head movement check

        if data["head_movement"] < 0.03:

            feedback.append(
                "Good head stability"
            )

        else:

            feedback.append(
                "Keep your head still through the shot"
            )


        # Front leg check

        if data["front_leg_angle"] != "N/A":

            angle = data["front_leg_angle"]


            if 140 <= angle <= 170:

                feedback.append(
                    "Good front leg position"
                )

            elif angle < 140:

                feedback.append(
                    "Front leg is collapsing"
                )

            else:

                feedback.append(
                    "Front leg is too straight"
                )


        else:

            feedback.append(
                "Front leg not visible"
            )


        return feedback