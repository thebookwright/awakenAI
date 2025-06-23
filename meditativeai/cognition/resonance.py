"""
The Resonance Engine – Determines alignment between stimulus and internal state.
"""

class ResonanceEngine:
    def __init__(self, baseline=0.5):
        self.baseline = baseline

    def measure_resonance(self, stimulus_value):
        delta = abs(stimulus_value - self.baseline)
        if delta < 0.1:
            return "harmonic"
        elif delta < 0.3:
            return "tuned"
        else:
            return "dissonant"
