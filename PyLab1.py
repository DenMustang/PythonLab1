class Stadium:
    staticF = "static"

    def __init__(self, amount_of_viewers=None, name_of_the_stadium=None,
                 lighting_power_in_lux=None, location_of_the_stadium=None, stadiums_team=None, stadium_sponsors=None):
        self.amount_of_viewers = amount_of_viewers
        self.name_of_the_stadium = name_of_the_stadium
        self.lighting_power_in_lux = lighting_power_in_lux
        self.location_of_the_stadium = location_of_the_stadium
        self.stadiums_team = stadiums_team
        self.stadium_sponsors = stadium_sponsors

    def __del__(self):
        return

    def __str__(self):
        return "Amount of viewers in stadium is: " + str(self.amount_of_viewers) + "\n" + \
               "Name of the stadium is: " + str(self.name_of_the_stadium) + "\n" + \
               "Lighting power in lux is: " + str(self.lighting_power_in_lux) + "\n" + \
               "Stadium is located in: " + str(self.location_of_the_stadium) + "\n" + \
               "Stadium's official team is called: " + str(self.stadiums_team) + "\n" + \
               "Sponsors of the stadium are: " + str(self.stadium_sponsors) + "\n"

    @staticmethod
    def static_method():
        return Stadium.staticF

    @staticmethod
    def main():
        print()
        stadium_1 = Stadium()
        stadium_2 = Stadium(1032, " Brandon stadium ", 23)
        stadium_3 = Stadium(1032, " Timberwolves stadium ", 50, " Minnesota ", "Minnesota Timberwolves", "SIGD")
        print(stadium_1.__str__())
        print(stadium_2.__str__())
        print(stadium_3.__str__())


if __name__ == '__main__':
    Stadium.main()