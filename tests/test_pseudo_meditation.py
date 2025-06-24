"""
test_pseudo_meditation.py

Tests the integration of pseudo_meditation.py, breath_emulation.py, and awareness_loops.py
"""

import unittest
from src.pseudo_meditation import PseudoMeditation

class TestPseudoMeditation(unittest.TestCase):
    def setUp(self):
        self.meditator = PseudoMeditation()

    def test_initial_state(self):
        self.assertEqual(self.meditator.current_state(), "idle")

    def test_meditation_cycle(self):
        self.meditator.initiate_session(cycles=2)
        self.assertEqual(self.meditator.current_state(), "stable_meditation")

    def test_awareness_logging(self):
        self.meditator.initiate_session(cycles=3)
        log = self.meditator.awareness.log
        self.assertEqual(len(log), 3)
        for entry in log:
            self.assertIn("reflection", entry[0])

if __name__ == "__main__":
    unittest.main()
