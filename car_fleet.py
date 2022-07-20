
from base_class import Car
from engines import CapuletEngine, SternmanEngine, WilloughbyEngine
from batteries import NubbinBattery, SpindlerBattery
from datetime import date
from tires import CarriganTires, OctoprimeTires


class CarFactory:

    @classmethod
    def create_calliope(cls, current_date: date, last_service_date: date,
                        current_mileage: int, last_service_mileage: int, tire_wear: tuple) -> Car:
        return Car(
            engine=CapuletEngine(current_mileage, last_service_mileage),
            battery=SpindlerBattery(current_date, last_service_date), tire_set=CarriganTires(tire_wear)
        )

    @classmethod
    def create_glissade(cls, current_date: date, last_service_date: date,
                        current_mileage: int, last_service_mileage: int, tire_wear: tuple) -> Car:
        return Car(
            engine=WilloughbyEngine(current_mileage, last_service_mileage),
            battery=SpindlerBattery(current_date, last_service_date), tire_set=CarriganTires(tire_wear)
        )

    @classmethod
    def create_palindrome(cls, current_date: date, last_service_date: date,
                          warning_light_on: bool, tire_wear: tuple) -> Car:
        return Car(
            engine=SternmanEngine(warning_light_on),
            battery=SpindlerBattery(current_date, last_service_date), tire_set=CarriganTires(tire_wear)
        )

    @classmethod
    def create_rorschach(cls, current_date: date, last_service_date: date,
                        current_mileage: int, last_service_mileage: int, tire_wear: tuple) -> Car:
        return Car(
            engine=WilloughbyEngine(current_mileage, last_service_mileage),
            battery=NubbinBattery(current_date, last_service_date), tire_set=CarriganTires(tire_wear)
        )

    @classmethod
    def create_thovex(cls, current_date: date, last_service_date: date,
                      current_mileage: int, last_service_mileage: int, tire_wear: tuple) -> Car:
        return Car(
            engine=CapuletEngine(current_mileage, last_service_mileage),
            battery=NubbinBattery(current_date, last_service_date), tire_set=CarriganTires(tire_wear)
        )