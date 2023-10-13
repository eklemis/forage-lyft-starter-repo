from battery.battery import Battery
from datetime import datetime


class SpindlerBattery(Battery):
    def __init__(self, last_service_date: datetime):
        self.last_service_date = last_service_date
        self.current_date = datetime.today()

    def needs_service(self) -> bool:
        return (self.current_date - self.last_service_date).days >= (2 * 360)