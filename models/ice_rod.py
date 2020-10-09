from models.abstract_fishing_rod import AbstractFishingRod


class IceRod(AbstractFishingRod):

    def __init__(self, season, length_in_meters, folded_length_in_meters, number_of_sections, weight_in_kg,
                 type_of_fishing_lure):
        super().__init__(season, length_in_meters, folded_length_in_meters, number_of_sections, weight_in_kg)
        self.type_of_fishing_lure = type_of_fishing_lure

    def __str__(self):
        return super().__str__() + "Type Of Fishing Lure = {}".format(self.type_of_fishing_lure)

    def __repr__(self):
        return super().__repr__()