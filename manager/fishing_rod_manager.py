from manager import fishing_rod_manager
from models.float_rod import FloatRod
from models.ice_rod import IceRod
from models.season import Season
from models.spinning import Spinning


class FishingRodManager:

    def __init__(self, rods_list):
        self.rods_list = rods_list

    def add_rod(self, fishing_rod):
        self.rods_list.append(fishing_rod)

    def add_rods(self, fishing_rods):
        self.rods_list.extend(fishing_rods)

    def find_fishing_rods_for_season(self, season):
        """
        >>> fishing_rod_manager.find_fishing_rods_for_season(Season.WINTER)[0].season
        <Season.WINTER: 2>
        >>> fishing_rod_manager.find_fishing_rods_for_season(Season.WINTER)[1].season
        <Season.WINTER: 2>
        """
        found_rods = list(
            filter(lambda iterated_rod: season == iterated_rod.season, self.rods_list))
        return found_rods


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True, extraglobs={'fishing_rod_manager': FishingRodManager(rods_list=[
        FloatRod(Season.SUMMER, 2, 1, 4, 0.2, "Very coll"),
        IceRod(Season.WINTER, 1, 0.5, 3, 0.4, "Maran"),
        Spinning(Season.SUMMER, 2, 1, 2, 0.3, "Osada"),
        IceRod(Season.WINTER, 1.4, 0.7, 4, 0.2, "Maran")])})
