from battery.battery import Battery
from datetime import datetime, date


class SpindlerBattery(Battery):
    def __init__(self, last_service_date: date):
        self.last_service_date = last_service_date
        self.current_date = datetime.today().date()

    def needs_service(self) -> bool:
        return (self.current_date - self.last_service_date).days >= (2 * 360)