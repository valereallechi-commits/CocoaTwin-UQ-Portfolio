import unittest
import numpy as np
from examples.spectral_demo import normalized_difference, artificial_reflectance
from examples.surface_demo import artificial_surface


class DemoTests(unittest.TestCase):
    def test_index_known_value(self):
        self.assertAlmostEqual(float(normalized_difference(0.6, 0.2)), 0.5)

    def test_index_invalid(self):
        self.assertTrue(np.isnan(normalized_difference(0.0, 0.0)))
        self.assertTrue(np.isnan(normalized_difference(np.nan, 0.1)))

    def test_reflectance(self):
        red, nir = artificial_reflectance(15)
        self.assertEqual(red.shape, (15, 15))
        self.assertTrue(np.all(np.abs(normalized_difference(nir, red)) <= 1))

    def test_surface(self):
        pts = artificial_surface(10)
        self.assertEqual(pts.shape, (100, 3))
        self.assertTrue(np.isfinite(pts).all())


if __name__ == '__main__':
    unittest.main()
