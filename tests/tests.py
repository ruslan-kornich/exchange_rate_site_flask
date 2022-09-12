import unittest
from api import test_api, privat_api
import models


class Test(unittest.TestCase):
    def setUp(self):
        models.init_db()

    def test_main(self):
        xrate = models.XRate.get(id=1)
        self.assertEqual(xrate.rate, 1.0)
        test_api.update_xrates(840, 980)
        xrate = models.XRate.get(id=1)

        self.assertEqual(xrate.rate, 1.01)

    def test_privat(self):
        xrate = models.XRate.get(id=1)
        updated_before = xrate.updated
        self.assertEqual(xrate.rate, 1.0)
        privat_api.update_xrates(840, 980)
        xrate = models.XRate.get(id=1)
        updated_after = xrate.updated

        self.assertGreater(xrate.rate, 25)
        self.assertGreater(updated_after, updated_before)


if __name__ == "__main__":
    unittest.main()
