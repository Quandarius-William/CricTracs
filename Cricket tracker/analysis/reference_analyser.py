import json


class ReferenceAnalyser:


    def __init__(self):

        self.reference = {}



    def create_reference(
        self,
        shot_name,
        metrics
    ):

        self.reference = {

            "shot": shot_name,

            "metrics": metrics

        }


        return self.reference



    def save_reference(
        self,
        filename
    ):

        with open(
            filename,
            "w"
        ) as file:

            json.dump(
                self.reference,
                file,
                indent=4
            )