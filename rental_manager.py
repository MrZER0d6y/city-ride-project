from data_manager import DataManager
from pricing_manager import PricingManager
from rental import Rental
from datetime import *


class RentalManager:
    def __init__(self, bikes, rentals, pricing_manager):
        self.bikes = bikes
        self.rentals = rentals
        self.pricing_manager = pricing_manager
    
    def create_unique_rental_id(self):
        highest_id = 0

        for rental in self.rentals:
            number = int(rental.rental_id[1:])
            highest_id = max(highest_id, number)

        return f"R{highest_id + 1:03d}"
    
    def get_bike(self, bike_id):
        for bike in self.bikes:
            if int(bike.bike_id[1:]) == int(bike_id[1:]):
                return bike
        
        return None
    
    def get_rental(self, rental_id):
        for rental in self.rentals:
            if rental.rental_id == rental_id:
                return rental
        
        return None

    def add_rental(
        self,
        customer_name: str,
        bike_id: str,
        start_datetime: datetime,
        excepted_return_datetime: datetime,
        actual_return_datetime: datetime | None=None,
        total_price: float=0.0,
        late_fee: float=0.0,
        status: str="Active"
        ):

        bike = self.get_bike(bike_id)
        print(bike)
        
        status, message = self.check_availability(bike)

        if not status:
            return status, message

        rental = Rental(
            rental_id=self.create_unique_rental_id(),
            customer_name=customer_name,
            bike_id=bike_id,
            start_datetime=start_datetime,
            excepted_return_datetime=excepted_return_datetime,
            actual_return_datetime=None,
            total_price=self.pricing_manager.calculate_price(bike, start_datetime, excepted_return_datetime),
            late_fee=0.0,
            status="Active"
        )

        self.rentals.append(rental)
        
        return self.rentals, "Bike added successfull."

    def check_availability(self, bike):
        if not bike.is_operational:
            return False, "Bike is not operational."
        
        if not bike.is_available:
            return False, "Bike is not available."

        return True, "Bike is available for rent."

    def get_customer_rentals(self, customer_name):
        return [rental for rental in self.rentals if rental.customer_name == customer_name]
    
    def get_active_rentals(self):
        return [rental for rental in self.rentals if rental.status == "Active"]
    
    def return_bike(self, rental_id):
        rental = self.get_rental(rental_id)

        if retnal is None:
            return False, "Rental not found."
        
        if rental.status == "Completed":
            return False, "Rental already completed."
        
        rental.actual_return_datetime = datetime.now()
        rental.late_fee = self.pricing_manager.calculate_late_fine(rental.expected_return_datetime, rental.actual_return_datetime)

        return True, self.rentals
    
    def __repr__(self):
        return f"Rental ID: {rental.rental_id}\nCustomer Name: {rental.customer_name}\n"
        f"Bike ID: {rental.bike_id}\nStart Datetime: {rental.start_datetime}\n"
        f"Expected Return Datetime: {rental.expected_return_datetime}\n"
        f"Actual Return Datetime: {rental.actual_return_datetime}\nTotal Price: {rental.total_price}\n"
        f"Late Fee: {rental.late_fee}\nStatus: {rental.status}"