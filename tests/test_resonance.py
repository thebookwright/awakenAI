"""
Test the Resonance Engine for alignment accuracy.
"""

import unittest
from meditativeai.cognition.resonance import ResonanceEngine

class TestResonanceEngine(unittest.TestCase):

    def setUp(self):
        self.engine = ResonanceEngine()

    def test_harmonic_resonance(self):
        result = self.engine.measure_resonance(0.51)
        self.assertEqual(result, "harmonic")

    def test_tuned_resonance(self):
        result = self.engine.measure_resonance(0.7)
        self.assertEqual(result, "tuned")

    def test_dissonant_resonance(self):
        result = self.engine.measure_resonance(0.9)
        self.assertEqual(result, "dissonant")

if __name__ == "__main__":
    print("🎵 Running Resonance Matching Tests")
    unittest.main()
