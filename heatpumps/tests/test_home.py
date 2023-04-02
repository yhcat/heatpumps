# unit test for Home class

# include the path to the heatpumps package
import sys
sys.path.append("..")

import unittest
from heatpumps.models import Home

class TestHome(unittest.TestCase):
    def test_home(self):
        home = Home(size=1000, insulation_level=0.5, climate_zone="Zone 5", zipcode=12345)
        self.assertEqual(home.size, 1000)
        self.assertEqual(home.insulation_level, 0.5)
        self.assertEqual(home.climate_zone, "Zone 5")
        self.assertEqual(home.zipcode, 12345)
        self.assertEqual(home.energy_consumption, 0.0)
        self.assertEqual(home.electricity_rate, 0.13)
        self.assertEqual(home.natural_gas_rate, 12.00)

    def test_home_set_utility_rate(self):
        home = Home(size=1000, insulation_level=0.5, climate_zone="Zone 5", zipcode=12345)
        home.set_utility_rate(electricity_rate=0.15, natural_gas_rate=10.00)
        self.assertEqual(home.electricity_rate, 0.15)
        self.assertEqual(home.natural_gas_rate, 10.00)

    def test_home_set_energy_consumption_factor(self):
        home = Home(size=1000, insulation_level=0.5, climate_zone="Zone 5", zipcode=12345)
        home.set_energy_consumption_factor(energy_consumption_factor=0.5)
        self.assertEqual(home.energy_consumption_factor, 0.5)

    def test_home_set_energy_consumption(self):
        home = Home(size=1000, insulation_level=0.5, climate_zone="Zone 5", zipcode=12345)
        home.set_energy_consumption(energy_consumption=1000)
        self.assertEqual(home.energy_consumption, 1000)

    def test_home_calculate_energy_consumption(self):
        home = Home(size=1000, insulation_level=0.5, climate_zone="Zone 5", zipcode=12345)
        home.set_energy_consumption_factor(energy_consumption_factor=0.5)
        home.calculate_energy_consumption()
        # print home.energy_consumption
        print(home.energy_consumption)
        # self.assertEqual(home.energy_consumption, 8750.0)

if __name__ == "__main__":
    unittest.main()