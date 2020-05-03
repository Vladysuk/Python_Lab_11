from abc import ABC


class AbstractFishingRod(ABC):

    def __init__(self, season, length_in_meters, folded_length_in_meters, number_of_sections, weight_in_kg):
        self.season = season
        self.length_in_meters = length_in_meters
        self.folded_length_in_meters = folded_length_in_meters
        self.number_of_sections = number_of_sections
        self.weight_in_kg = weight_in_kg

    def __str__(self):
        return "Season = {}, Length = {} m, Folded Length = {} m, \
        Number of sections = {}, Weight = {} kg".format(self.season, self.length_in_meters,
                                                        self.folded_length_in_meters, self.number_of_sections,
                                                        self.weight_in_kg)

    def __repr__(self):
        return "(Season: {})".format(self.season)
