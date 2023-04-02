import pandas as pd

# create a class called ZipCode to store weather data
class ZipCode:
    """
    Goal: store weather data
    A zipcode with a given climate zone, average temperature, and average heating degree days.
    """
    def __init__(self, climate_zone, average_temperature, average_heating_degree_days):
        # write a docstring
        """
        Parameters
        ----------
        climate_zone : str
            The climate zone of the zipcode. default = "Zone 5"
        average_temperature : float
            The average temperature of the zipcode. default = 50
        average_heating_degree_days : float
            The average heating degree days of the zipcode. default = 5000
        """
        self.climate_zone = climate_zone
        self.average_temperature = average_temperature
        self.average_heating_degree_days = average_heating_degree_days

    def heat_pump_cop_hourly(self, T_target=20):
        # Calculate the coefficient of performance of the heat pump based on the home's climate zone.
        # ...
        cop_by_hour = 3.5 + 0.033 * (self.average_temperature - T_target)

        return cop_by_hour

class Home:
    """
    Goal: calculate the heating demand of a home
    A home with a given size, insulation level, climate zone, and energy consumption patterns.
    """
    def __init__(self, size, insulation_level, climate_zone, zipcode):
        # write a docstring
        """
        Parameters
        ----------
        size : float
            The size of the home in square feet. default = 1000
        insulation_level : float
            The insulation level of the home. default = 0.5
        climate_zone : str
            The climate zone of the home. default = "Zone 5"
        zipcode : int
            The zipcode of the home. default = 12345
        """
        self.size = size
        self.insulation_level = insulation_level
        self.climate_zone = climate_zone
        self.zipcode = zipcode

        self.energy_consumption = 0.0  # units are kWh
        self.electricity_rate = 0.13  # units are $/kWh
        self.natural_gas_rate = 12.00  # units are $/cubic feet

    # get utility rate
    def set_utility_rate(self, electricity_rate, natural_gas_rate):
        # Get the utility rate for the home's climate zone.
        self.electricity_rate = electricity_rate
        self.natural_gas_rate = natural_gas_rate

    # set energy consumption rate factor
    def set_energy_consumption_factor(self, energy_consumption_factor):
        # Set the energy consumption factor of the home.
        self.energy_consumption_factor = energy_consumption_factor

    # set energy consumption instead of calculating it
    def set_energy_consumption(self, energy_consumption):
        # Set the energy consumption of the home.
        self.energy_consumption = energy_consumption
        
    def calculate_energy_consumption(self):
        # Calculate the energy consumption of the home based on its size, insulation level, climate zone, and energy consumption patterns.
         # Load the climate zone data

        climate_zones = pd.read_csv("data/climate_zones.csv")
        
        # Calculate the heating degree days based on the climate zone
        heating_degree_days = climate_zones.loc[climate_zones["Zone"] == self.climate_zone, "Heating Degree Days"].values[0]
        
        # Calculate the energy consumption based on the home's size and insulation level
        energy_consumption = self.size * self.insulation_level * heating_degree_days
        
        # Adjust the energy consumption based on the energy consumption patterns of the home
        energy_consumption *= self.energy_consumption_factor

        self.energy_consumption = energy_consumption

        return self.energy_consumption
    
    # estimate heating energy consumption based on natual gas bill
    def estimate_energy_consumption(self, natural_gas_bill):
        
        gas_volume = natural_gas_bill / self.natural_gas_rate

        energy_consumption = gas_volume * 1000 * 1.055

        self.energy_consumption = energy_consumption

        return self.energy_consumption
    
    # estimate heating energy consumption by month
    def estimate_energy_consumption_by_month(self, natural_gas_bill_by_month):
            
        gas_volume_by_month = natural_gas_bill_by_month / self.natural_gas_rate

        energy_consumption_by_month = gas_volume_by_month * 1000 * 1.055

        self.energy_consumption_by_month = energy_consumption_by_month

        return self.energy_consumption_by_month
    
    # calculate theoretical heat pump COP by month average temperature
    # Ideally run a Monte Carlo with hourly temperature data
    def calculate_theoretical_cop_by_month(self, average_temperature_by_month):

        cop_by_month = 3.5 + 0.033 * average_temperature_by_month

        self.cop_by_month = cop_by_month

        return self.cop_by_month
    
    # calculate cop by hour
    def calculate_cop_by_hour(self, average_temperature_by_hour):

        cop_by_hour = 3.5 + 0.033 * average_temperature_by_hour

        self.cop_by_hour = cop_by_hour

        return self.cop_by_hour
    
    # calculate electricity cost by month
    def calculate_electricity_cost_by_month(self, energy_consumption_by_month, cop_by_month):
            
        electricity_cost_by_month = energy_consumption_by_month / cop_by_month * self.electricity_rate

        self.electricity_cost_by_month = electricity_cost_by_month

        return self.electricity_cost_by_month
    
    # calculate yearly cost savings
    def calculate_yearly_cost_savings(self, electricity_cost_by_month, natural_gas_bill_by_month):

        yearly_cost_savings = natural_gas_bill_by_month.sum() - electricity_cost_by_month.sum()

        self.yearly_cost_savings = yearly_cost_savings

        return self.yearly_cost_savings
    
    # calculate payback period
    def calculate_payback_period(self, cost, yearly_cost_savings):

        payback_period = cost / yearly_cost_savings

        self.payback_period = payback_period

        return self.payback_period
    
    
class HeatPump:
    def __init__(self, type, cost, maintenance_cost):
        # write a docstring
        """
        Parameters
        ----------
        type : str
            The type of heat pump. default = "Air Source", options = ["Air Source", "Ground Source"]
        cost : float
            The cost of the heat pump. default = 10000
        maintenance_cost : float
            The maintenance cost of the heat pump. default = 1000 per year
        """

        self.type = type
        self.cost = cost
        self.maintenance_cost = maintenance_cost

    # calculate COP
    def calculate_cop(self, home):
        # Calculate the coefficient of performance of the heat pump based on the home's climate zone.
        pass
        
    def calculate_savings(self, home):
        # Calculate the cost savings of installing a heat pump in the given home based on its energy consumption and the cost of the heat pump and fuel.
        pass
