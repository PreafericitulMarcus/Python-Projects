from airport_domain import Passangers, Plane


class AirportRepository:
    def __init__(self):
        self._passangers = []
        self._planes = []
