from capritools2.models import Dscan, DscanObject
from capritools2.stuff import random_key

class DscanParser:
    scan = None


    def __init__(self):
        self.scan = Dscan(
            key=random_key(7)
        )