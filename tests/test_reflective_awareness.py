"""
Test the self-reflective capacity of the Awareness module.
"""

import unittest
from meditativeai.cognition.awareness import Awareness

class TestAwareness(unittest.TestCase):

    def test_initial_state(self):
        ai = Awareness()
        self.assertEqual(ai.state, "resting")
        self.assertEqual(ai.reflect(), "Current meditative state: resting")

    def test_stimuli_responses(self):
        ai = Awareness()
        ai.update_state("distraction")
        self.assertEqual(ai.state, "redirecting")
        ai.update_state("stillness")
        self.assertEqual(ai.state, "deepening")
        ai.update_state("unknown")
        self.assertEqual(ai.state, "observing")

    def test_reflection_output(self):
        ai = Awareness()
        ai.update_state("stillness")
        reflection = ai.reflect()
        self.assertIn("deepening", reflection)

if __name__ == "__main__":
    print("🪞 Running Reflective Awareness Tests")
    unittest.main()
