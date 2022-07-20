import unittest

from tires import CarriganTires, OctoprimeTires


class TestCarriganTires(unittest.TestCase):
    def test_set_up(self):
        
        self.carrigan_tires_that_need_service = CarriganTires((0.8, 0.9, 1, 0.8))
        self.carrigan_tires_that_dont_need_service = CarriganTires((0.1, 0, 0.2, 0.1))

    def test_should_need_service(self):
        self.assertTrue(
            self.carrigan_tires_that_need_service.needs_service()
        )

    def test_should_not_need_service(self):
        self.assertFalse(
            self.carrigan_tires_that_dont_need_service.needs_service()
        )


class TestOctoprimeTires(unittest.TestCase):
    def test_set_up(self):
        
        self.octoprime_tires_that_need_service = OctoprimeTires((0.8, 0.9, 1, 0.8))
        self.octoprime_tires_that_dont_need_service = OctoprimeTires((0.7, 0.8, 0.7, 0.7))

    def test_should_need_service(self):
        self.assertTrue(
            self.octoprime_tires_that_need_service.needs_service()
        )

    def test_should_not_need_service(self):
        self.assertFalse(
            self.octoprime_tires_that_dont_need_service.needs_service()
        ) 