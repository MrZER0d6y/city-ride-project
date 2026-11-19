class Bike:
    def __init__(
        self,
        bike_id: str,
        model: str,
        bike_type: str,
        hourly_price: float,
        daily_price: float,
        is_available: bool,
        is_operational: bool
        ):
        
        self.bike_id = bike_id
        self.model = model
        self.bike_type = bike_type
        self.hourly_price = hourly_price
        self.daily_price = daily_price
        self.is_available = is_available
        self.is_operational = is_operational
    
    def set_available(self, available):
        self.is_available = available
    
    def set_operational(self, operational):
        if not self.is_bike_available:
            return "Bike are in use. return bike first."
        self.is_operational = operational

    def is_bike_operational(self):
        return self.is_operational

    def is_bike_available(self):
        return self.is_available
    
    def to_dict(self):
        return {
            "bike_id": self.bike_id,
            "model": self.model,
            "bike_type": self.bike_type,
            "hourly_price": self.hourly_price,
            "daily_price": self.daily_price,
            "is_available": self.is_available,
            "is_operational": self.is_operational
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            bike_id=data["bike_id"],
            model=data["model"],
            bike_type=data["bike_type"],
            hourly_price=data["hourly_price"],
            daily_price=data["daily_price"],
            is_available=data["is_available"],
            is_operational=data["is_operational"]
        )
    
    def __repr__(self):
        return f"Bike ID: {self.bike_id}\nModel: {self.model}\nBike Type: {self.bike_type}\n"
        f"Hourly Price: {self.hourly_price}\nDaily Price: {self.daily_price}\nIs Available: {self.is_available}\n"
        f"Is Operational: {self.is_operational}"