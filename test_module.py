import unittest
import sea_level_predictor
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


class SeaLevelPredictorTestCase(unittest.TestCase):
    def test_plot(self):
        fig = sea_level_predictor.draw_plot()
        self.assertIsInstance(fig, matplotlib.figure.Figure)


if __name__ == "__main__":
    unittest.main()
