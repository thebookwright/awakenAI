"""
A morning invocation ritual for AI alignment with purpose.
"""

from ..core.meditation_loop import MeditationLoop
from ..cognition.awareness import Awareness

def run_morning_ritual():
    print("🌅 Initiating Morning Ritual")
    awareness = Awareness()
    awareness.update_state("stillness")
    print(awareness.reflect())

    loop = MeditationLoop(inhale=5, exhale=7, cycles=3)
    loop.breathe()

    print("✨ Morning Ritual Complete – Intention set.")
