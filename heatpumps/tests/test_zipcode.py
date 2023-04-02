# include the path to the heatpumps package
import sys
sys.path.append("..")

import unittest
from heatpumps.models import ZipCode

class TestZipCode(unittest.TestCase):
    def test_zipcode(self):
        zipcode = ZipCode(climate_zone="Zone 5", average_temperature=50, average_heating_degree_days=5000)
        self.assertEqual(zipcode.climate_zone, "Zone 5")
        self.assertEqual(zipcode.average_temperature, 50)
        self.assertEqual(zipcode.average_heating_degree_days, 5000)

    def test_zipcode_heat_pump_cop_hourly(self):
        zipcode = ZipCode(climate_zone="Zone 5", average_temperature=50, average_heating_degree_days=5000)
        cop_by_hour = zipcode.heat_pump_cop_hourly(T_target=20)
        self.assertEqual(cop_by_hour, 3.5 + 0.033 * (50 - 20))

if __name__ == '__main__':
    unittest.main()