import json
from pathlib import Path
from bike import Bike
from rental import Rental


class DataManager:
    def __init__(self):
        folder = Path(__file__).parent

        self.bikes_file = folder / "bikes.json"
        self.rentals_file = folder / "rentals.json"
    
    def load_bikes(self):
        if not self.bikes_file.exists():
            return []

        with open(self.bikes_file, "r", encoding="utf-8") as file:
            bikes = json.load(file)
            return [Bike.from_dict(data) for data in bikes]
    
    def load_rentals(self):
        if not self.rentals_file.exists():
            return []

        with open(self.rentals_file, "r", encoding="utf-8") as file:
            rentals = json.load(file)
            return [Rental.from_dict(data) for data in rentals]
    
    def save_bikes(self, bikes):
        bikes_data = [bike.to_dict() for bike in bikes]

        with open(self.bikes_file, "w", encoding="utf-8") as file:
            json.dump(bikes, file, indent=2, ensure_ascii=False)
    
    def save_rentals(self, rentals):
        rentals_data = [rental.to_dict() for rental in rentals]

        with open(self.rentals_file, "w", encoding="utf-8") as file:
            json.dump(rentals, file, indent=2, ensure_ascii=False)
