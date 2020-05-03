from model.abstract_fishing_rod import AbstractFishingRod


class Spinning(AbstractFishingRod):

    def __init__(self, season, length_in_meters, folded_length_in_meters, number_of_sections, weight_in_kg,
                 type_of_wobbler):
        super().__init__(season, length_in_meters, folded_length_in_meters, number_of_sections, weight_in_kg)
        self.type_of_wobbler = type_of_wobbler

    def __str__(self):
        return super().__str__() + "Type Of Wobbler = {}".format(self.type_of_wobbler)

    def __repr__(self):
        return super().__repr__()