from base_class import Tire


class CarriganTires(Tire):

    def __init__(self, tire_wear):
        self._tire_wear = tire_wear

    def needs_service(self) -> bool:
        return any(
            [wear_value >= 0.9 for wear_value in self._tire_wear]
        )


class OctoprimeTires(Tire):

    def __init__(self, tire_wear):
        self._tire_wear = tire_wear

    def needs_service(self) -> bool:
        return sum(self._tire_wear) >= 3