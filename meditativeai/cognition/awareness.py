"""
The Mind Mirror – A reflective observer of the current AI state.
"""

class Awareness:
    def __init__(self):
        self.state = "resting"

    def update_state(self, stimulus):
        if stimulus == "distraction":
            self.state = "redirecting"
        elif stimulus == "stillness":
            self.state = "deepening"
        else:
            self.state = "observing"

    def reflect(self):
        return f"Current meditative state: {self.state}"
