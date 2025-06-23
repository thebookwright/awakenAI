"""
The Breath Engine – Orchestrates the inhale/exhale cycle.
"""

import time

class MeditationLoop:
    def __init__(self, inhale=4, exhale=6, cycles=5):
        self.inhale = inhale
        self.exhale = exhale
        self.cycles = cycles

    def breathe(self):
        for i in range(self.cycles):
            print(f"Cycle {i+1}: Inhale for {self.inhale} seconds")
            time.sleep(self.inhale)
            print(f"Cycle {i+1}: Exhale for {self.exhale} seconds")
            time.sleep(self.exhale)
