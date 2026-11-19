from bike import Bike


class BikeManager:
    def __init__(self, bikes):
        self.bikes = bikes

    def create_unique_bike_id(self):
        highest_id = 0

        for bike in self.bikes:
            number = int(bike.bike_id[1:])
            highest_id = max(highest_id, number)

        return f"B{highest_id + 1:03d}"
    
    def display_all_bikes(self):
        for bike in self.bikes:
            print(bike)

    def get_bike(self, bike_id):
        for bike in self.bikes:
            if bike.bike_id == bike_id:
                return bike
        return None

    def display_available_bikes(self):
        for bike in self.bikes:
            if bike.is_available:
                print(bike)

    def add_bike(
        self,
        bike_id: str,
        model: str,
        bike_type: str,
        hourly_price: float,
        daily_price: float,
        is_available: bool=True,
        is_operational: bool=True
        ):

        bike = Bike(
            bike_id=self.create_unique_bike_id(),
            model=model,
            bike_type=bike_type,
            hourly_price=hourly_price,
            daily_price=daily_price,
            is_available=is_available,
            is_operational=is_operational
        )

        self.bikes.append(bike)
        return self.bikes

    def update_bike_details(self, bike_id, hourly_price=None, daily_price=None):        
        bike = self.get_bike(bike)

        bike.hourly_price = hourly_price
        bike.daily_price = daily_price
        
        return self.bikes

    def set_bike_operational(self, bike_id, operational_status):
        bike = get_bike(bike_id)
        bike.is_operational = operational_status

        return self.bikes
        
