from typing import List

from model.abstract_fishing_rod import AbstractFishingRod
from model.float_rod import FloatRod
from model.ice_rod import IceRod
from model.season import Season
from model.sort_type import SortType
from model.spinning import Spinning


class FishingRodManagerUtils:

    @staticmethod
    def sort_by_length_in_meters(rods_list: List[AbstractFishingRod], sort_type: SortType):
        """
        >>> rods_list = [FloatRod(Season.SUMMER, 2, 1, 4, 0.2, "Very coll"),\
        IceRod(Season.WINTER, 1, 0.5, 3, 0.4, "Maran"),\
        Spinning(Season.SUMMER, 2, 1, 2, 0.3, "Osada"),\
        IceRod(Season.WINTER, 1.4, 0.7, 4, 0.2, "Maran")]
        >>> sort_type = SortType.ASCENDING
        >>> FishingRodManagerUtils.sort_by_length_in_meters(rods_list,sort_type)
        >>> rods_list[0].length_in_meters
        1
        >>> rods_list[1].length_in_meters
        1.4
        >>> rods_list[2].length_in_meters
        2
        >>> rods_list[3].length_in_meters
        2
        """
        if sort_type == SortType.ASCENDING:
            rods_list.sort(key=lambda rod: rod.length_in_meters)
        else:
            rods_list.sort(key=lambda rod: rod.length_in_meters, reverse=True)

    @staticmethod
    def sort_by_weight(rods_list: List[AbstractFishingRod], sort_type: SortType):
        """
        >>> rods_list = [FloatRod(Season.SUMMER, 2, 1, 4, 0.2, "Very cool"),\
        IceRod(Season.WINTER, 1, 0.5, 3, 0.4, "Maran"),\
        Spinning(Season.SUMMER, 2, 1, 2, 0.3, "Long"),\
        IceRod(Season.WINTER, 1.4, 0.7, 4, 0.2, "Super")]
        >>> sort_type = SortType.ASCENDING
        >>> FishingRodManagerUtils.sort_by_weight(rods_list,sort_type)
        >>> rods_list[0].weight_in_kg
        0.2
        >>> rods_list[1].weight_in_kg
        0.2
        >>> rods_list[2].weight_in_kg
        0.3
        >>> rods_list[3].weight_in_kg
        0.4
        """
        if sort_type == SortType.ASCENDING:
            rods_list.sort(key=lambda rod: rod.weight_in_kg)
        else:
            rods_list.sort(key=lambda rod: rod.weight_in_kg, reverse=True)


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)
