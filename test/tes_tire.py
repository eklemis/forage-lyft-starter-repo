import unittest
from tire.tire import Tire, Carrigan, Octoprime


def all_need_service(tires: list[Tire]):
    for tire in tires:
        if not tire.needs_service():
            return False
        return True


def no_one_need_service(tires: list[Tire]):
    for tire in tires:
        if tire.needs_service():
            return False
    return True


class TestCarrigan(unittest.TestCase):
    def test_tire_should_be_service(self):
        carigan_tires = [Carrigan([0, 0, 0, 0.9]), Carrigan([1, 0, 0, 0.89]), Carrigan([1, 0, 0, 0.89]), Carrigan([0, 1, 1, 1])]
        self.assertTrue(all_need_service(carigan_tires))

    def test_tire_should_not_be_service(self):
        carigan_tires = [Carrigan([0, 0, 0, 0]),Carrigan([0, 0, 0, 0.89]), Carrigan([0, 0.1, 0, 0]), Carrigan([0.89, 0.1, 0.8999, 0])]
        self.assertTrue(no_one_need_service(carigan_tires))

    def test_invalid_tire_length(self):
        with self.assertRaises(ValueError):
            Carrigan([0, 0, 0])

        with self.assertRaises(ValueError):
            Carrigan([0, 0, 0, 0, 0])

    def test_invalid_tire_value(self):
        with self.assertRaises(ValueError):
            Carrigan([0, 0, 0, 1.1])

        with self.assertRaises(ValueError):
            Carrigan([0, 0, 0, -0.1])

class TestOctoprime(unittest.TestCase):
    def test_tire_should_be_service(self):
        octoprime_tires = [Octoprime([1, 1, 1, 1]), Octoprime([1, 1, 1, 0]), Octoprime([0.60, 0.75, 0.75, 0.9]), Octoprime([0.75, 0.75, 0.75, 0.75]),  Octoprime([1, 0.75, 0.75, 0.5])]
        self.assertTrue(all_need_service(octoprime_tires))

    def test_tire_should_not_be_service(self):
        octoprime_tires = [Octoprime([0, 0, 0, 0]), Octoprime([1, 1, 0.99, 0]), Octoprime([0.49, 1, 1, 0.5]), Octoprime([0.49, 0.001, 1, 0.5])]
        self.assertTrue(no_one_need_service(octoprime_tires))

    def test_invalid_tire_length(self):
        with self.assertRaises(ValueError):
            Octoprime([0, 0, 0])

        with self.assertRaises(ValueError):
            Octoprime([0, 0, 0, 0, 0])

    def test_invalid_tire_value(self):
        with self.assertRaises(ValueError):
            Octoprime([0, 0, 0, 1.1])

        with self.assertRaises(ValueError):
            Octoprime([0, 0, 0, -0.1])


if __name__ == '__main__':
    unittest.main()
