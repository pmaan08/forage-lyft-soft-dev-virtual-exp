from base_class import Engine


class CapuletEngine(Engine):

    def __init__(self, current_mileage: int, last_service_mileage: int):
            self._current_mileage = current_mileage
            self._last_service_mileage = last_service_mileage

    def needs_service(self) -> bool:
        return (self._current_mileage - self._last_service_mileage) > 30_000


class WilloughbyEngine(Engine):

    def __init__(self, current_mileage: int, last_service_mileage: int):
        self._current_mileage = current_mileage
        self._last_service_mileage = last_service_mileage

    def needs_service(self) -> bool:
        return (self._current_mileage - self._last_service_mileage) > 60_000


class SternmanEngine(Engine):

    def __init__(self, warning_light_on: bool):
        self._warning_light_on = warning_light_on

    def needs_service(self) -> bool:
        return self._warning_light_on