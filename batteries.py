from datetime import date

from base_class import Battery


class SpindlerBattery(Battery):
    
    def __init__(self, current_date: date, last_service_date: date):
        self._current_date = current_date
        self._last_service_date = last_service_date

    def needs_service(self):
        service_threshold = 365 * 2  
        time_since_last_service = self._current_date - self._last_service_date 
        return time_since_last_service.days > service_threshold 


class NubbinBattery(Battery):
    
    def __init__(self, current_date: date, last_service_date: date):
        self._current_date = current_date
        self._last_service_date = last_service_date

    def needs_service(self):
        service_threshold = 365 * 4  
        time_since_last_service = self._current_date - self._last_service_date 
        return time_since_last_service.days > service_threshold 
