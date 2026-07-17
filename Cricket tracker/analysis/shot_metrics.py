class ShotMetrics:


    def calculate_head_stability(self, shot_frames):

        if len(shot_frames) < 5:
            return 0


        head_positions = []


        for landmarks in shot_frames:

            if landmarks is None:
                continue


            nose = landmarks[0]

            left_shoulder = landmarks[11]
            right_shoulder = landmarks[12]


            # Use shoulders as body reference

            shoulder_x = (
                left_shoulder.x +
                right_shoulder.x
            ) / 2


            shoulder_y = (
                left_shoulder.y +
                right_shoulder.y
            ) / 2


            relative_head = (

                nose.x - shoulder_x,

                nose.y - shoulder_y

            )


            head_positions.append(
                relative_head
            )


        if len(head_positions) < 5:
            return 0



        # Find average head position

        avg_x = sum(
            p[0] for p in head_positions
        ) / len(head_positions)


        avg_y = sum(
            p[1] for p in head_positions
        ) / len(head_positions)



        movement = 0


        for x, y in head_positions:

            movement += (
                abs(x - avg_x)
                +
                abs(y - avg_y)
            )


        movement /= len(head_positions)



        # Convert movement into score

        if movement < 0.015:
            return 100

        elif movement < 0.025:
            return 90

        elif movement < 0.040:
            return 75

        elif movement < 0.060:
            return 60

        else:
            return 40