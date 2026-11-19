class ReportManager:
    def __init__(self, bikes, rentals):
        self.bikes = bikes
        self.rentals = rentals

    def number_of_rentals(self):
        return len(self.rentals)
    
    def number_of_active_rentals(self):
        return sum(1 for rental in self.rentals if rental.status == "Active")
    
    def number_of_finished_rentals(self):
        return sum(1 for rental in self.rentals if rental.actual_return_datetime is not None)
    
    def total_revenue(self):
        return sum(rental.total_price for rental in self.rentals if rental.actual_return_datetime is not None)
    
    def total_late_fees(self):
        return sum(rental.late_fee for rental in self.rentals)
    
    def get_bike_renting_count(self, bike_id):
        return sum(1 for rental in self.rentals if rental.bike_id == bike_id)
    
    def get_customer_rentals_count(self, customer_name):
        return sum(1 for rental in self.rental if rental.customer_name == customer_name)
    
    def get_customer_with_most_rentals(self):
        customer_with_most_rental = None
        highest_count = 0

        for rental in self.rentals:
            count = self.get_customer_rentals_count(rental.customer_name)

            if count > highest_count:
                highest_count = count
                customer_with_most_rental = rental

        return customer_with_most_rental
    
    def get_most_rented_bikes(self):
        most_rented_bikes = None
        highest_count = 0

        for bike in self.bikes:
            count = self.get_bike_renting_count(bike.bike_id)

            if count > highest_count:
                highest_count = count
                most_rented_bikes = bike
        
        return most_rented_bikes
    
    def get_average_rental_price(self):
        return self.total_revenue() / self.number_of_finished_rentals()
        
