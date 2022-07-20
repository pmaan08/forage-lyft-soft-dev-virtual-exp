import unittest

from engines import CapuletEngine, WilloughbyEngine, SternmanEngine


class TestCapuletEngine(unittest.TestCase):
    def test_set_up(self):
        self.capulet_that_needs_service = CapuletEngine(30_001, 0)
        self.capulet_that_doesnt_need_service = CapuletEngine(150, 50)

    def test_should_need_service(self):
        self.assertTrue(
            self.capulet_that_needs_service.needs_service()
        )

    def test_should_not_need_service(self):
        self.assertFalse(
            self.capulet_that_doesnt_need_service.needs_service()
        )


class TestWilloughbyEngine(unittest.TestCase):
    def test_set_up(self):
        self.willoughby_that_needs_service = WilloughbyEngine(60_001, 0)
        self.willoughby_that_doesnt_need_service = WilloughbyEngine(15_000, 5)

    def test_should_need_service(self):
        self.assertTrue(
            self.willoughby_that_needs_service.needs_service()
        )

    def test_should_not_need_service(self):
        self.assertFalse(
            self.willoughby_that_doesnt_need_service.needs_service()
        )


class TestSternmanEngine(unittest.TestCase):
    def test_set_up(self):
        self.sternman_that_needs_service = SternmanEngine(warning_light_on=True)
        self.sternman_that_doesnt_need_service = SternmanEngine(warning_light_on=False)

    def test_should_need_service(self):
        self.assertTrue(
            self.sternman_that_needs_service.needs_service()
        )

    def test_should_not_need_service(self):
        self.assertFalse(
            self.sternman_that_doesnt_need_service.needs_service()
        )


if __name__ == "__main__":
    unittest.main()