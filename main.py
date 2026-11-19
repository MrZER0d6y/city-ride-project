from data_manager import DataManager
from bike_manager import BikeManager
from rental_manager import RentalManager
from pricing_manager import PricingManager
from report_manager import ReportManager
from inputs import inputs
from datetime import *


class CityRideSystem:
    def __init__(self):
        self.data_manager = DataManager()

        self.bikes = self.data_manager.load_bikes()
        self.rentals = self.data_manager.load_rentals()

        self.pricing_manager = PricingManager()
        self.bike_manager = BikeManager(self.bikes)
        self.rental_manager = RentalManager(self.bikes, self.rentals, self.pricing_manager)
        self.report_manager = ReportManager(self.bikes, self.rentals)
    
    def save_data(self):
        self.data_manager.save_bikes(self.bikes)
        self.data_manager.save_rentals(self.rentals)
    
    @staticmethod
    def main_menu():
        print("""
=================================
        CITY RIDE SYSTEM
       Bike Rental Company
=================================

1. Bikes Managment
2. Rentals Managment
3. Reports
4. Exit
        """)
    
    @staticmethod
    def bike_managment_menu():
        print("""
========= PRODUCTS MANAGEMENT =========

1. Display All Bikes
2. Display Available Bikes
3. Add Bike
4. Update Bike Details
5. Set Bike's Operational Status
6. Back to Main Menu
        """)
    
    def bikes_managment(self):
        back_to_main_menu = False

        while not back_to_main_menu:
            CityRideSystem.bike_managment_menu()

            choice = inputs.get_choice(6)

            if choice == 1:
                print(f"\n--------- ALL BIKES ---------")
                self.bike_manager.display_all_bikes()
            
            elif choice == 2:
                print(f"\n--------- AVAILABLE BIKES ---------")
                self.bike_manager.display_available_bikes()

            elif choice == 3:
                print(f"\n--------- ADD BIKE ---------")
                model = inputs.get_model()
                bike_type = inputs.get_bike_type()
                hourly_price = inputs.get_hourly_price()
                daily_price = inputs.get_daily_price()

                bikes = self.bike_manager.add_bike(model, bike_type, hourly_price, daily_price)
                self.data_manager.save_bikes(bikes)
            
            elif choice == 4:
                print(f"\n--------- UPDATE BIKE DETAILS ---------")
                bike_id = inputs.get_bike_id()

                print("What do you want to update?")
                choice = inputs.get_update_bike()

                if choice == "Hourly Price":
                    bikes = self.bike_manager.update_bike_details(hourly_price=choice)

                elif choice == "Daily Price":
                    bikes = self.bike_manager.update_bike_details(daily_price=choice)
                
                self.data_manager.save_bikes(bikes)
            
            elif choice == 5:
                print(f"\n--------- SET BIKE'S OPERATIONAL STATUS ---------")
                bike_id = inputs.get_bike_id()
                operational_status = inputs.get_operational_status()

                bikes = self.bike_manager.set_bike_operational(bike_id, operational_status)
                self.data_manager.save_bikes(bikes)
            
            elif choice == 6:
                back_to_main_menu = True

    @staticmethod
    def rental_managment_menu():
        print("""
========= RENTALS MANAGEMENT =========

1. Add Rental
2. Display Customer's Rentals
3. Display Active Rentals
4. Return Bike
5. Back to Main Menu
        """)

    def rental_managment(self):
        back_to_main_menu = False
        
        while not back_to_main_menu:
            CityRideSystem.rental_managment_menu()

            choice = inputs.get_choice(5)

            if choice == 1:
                print(f"\n--------- ADD RENTAL ---------")
                customer_name = inputs.get_customer_name()
                bike_id = inputs.get_bike_id(self.bikes)
                start_datetime = datetime.now()
                expected_return_datetime = inputs.get_excepted_return_datetime()
                
                rentals, message = self.rental_manager.add_rental(
                    customer_name,
                    bike_id,
                    start_datetime,
                    expected_return_datetime,
                    )
                print(message)
                self.data_manager.save_rentals(rentals)

            elif choice == 2:
                print(f"\n--------- DISPLAY CUSTOMER'S RENTALS ---------")
                customer_name = inputs.get_customer_name()
                counter = 0

                for counter, rental in enumerate(self.rental_manager.get_customer_rentals(customer_name), start=1):
                    print(rental)
                
                if counter == 0:
                    print(f"No rentals for {customer_name} found.")
                    continue

                print(f"{counter} rentals of {customer_name}.")

            elif choice == 3:
                print(f"\n--------- DISPLAY ACTIVE RENTALS ---------")
                counter = 0

                for counter, rental in enumerate(self.rental_manager.get_active_rentals(), start=1):
                    self.rental_manager.print_rental(rental)
                
                if counter == 0:
                    print("No active rentals found.")
                    continue

                print(f"{counter} active rentals.")
            
            elif choice == 4:
                print(f"\n--------- RETURN BIKE ---------")
                rental_id = inputs.get_rental_id(self.rentals)
                result, retnals = self.rental_manager.return_bike(rental_id)

                if result is False:
                    print(retnals)
                    continue

                self.data_manager.save_rentals(rentals)

            elif choice == 5:
                back_to_main_menu = True

    @staticmethod
    def reports_menu():
        print("""
========= REPORTS =========

1. Number Of Rentals
2. Number Of Active Rentals
3. Number Of finished Rentals
4. Total Revenue
5. Total Late Fees
6. Bike's Number Of Rentals
7. Customer's Rentals Count
8. Customer With The Most Rentals
9. Most Rented Bikes
10. Average Rentals Price
11. Back to Main Menu
        """)

    def reports_managment(self):
        back_to_main_menu = False
        
        while not back_to_main_menu:
            CityRideSystem.reports_menu()

            choice = inputs.get_choice(10)

            if choice == 1:
                print(f"\n--------- NUMBER OF RENTALS ---------")
                print(self.report_manager.number_of_rentals())
            
            elif choice == 2:
                print(f"\n--------- NUMBER OF ACTIVE RENTALS ---------")
                print(self.report_manager.number_of_active_rentals())

            elif choice == 3:
                print(f"\n--------- NUMBER OF FINISHED RENTALS RENTALS ---------")
                print(self.report_manager.number_of_finished_rentals())
            
            elif choice == 4:
                print(f"\n--------- TOTAL REVENUE ---------")
                print(self.report_manager.total_revenue())
            
            elif choice == 5:
                print(f"\n--------- TOTAL LATE FEES ---------")
                print(self.report_manager.total_late_fees())
            
            elif choice == 6:
                print(f"\n--------- BIKE'S NUMBER OF RENTALS ---------")
                print(self.report_manager.get_bike_renting_count(inputs.get_bike_id()))
            
            elif choice == 7:
                print(f"\n--------- CUSTOMER'S RENTALS COUNT ---------")
                print(self.report_manager.get_customer_rentals_count(inputs.get_customer_name()))
            
            elif choice == 8:
                print(f"\n--------- CUSTOMER WITH THE MOST RENTALS ---------")
                print(self.report_manager.get_customer_with_most_rentals())
            
            elif choice == 9:
                print(f"\n--------- MOST RENTED BIKES ---------")
                print(self.report_manager.get_most_rented_bikes())
            
            elif choice == 10:
                print(f"\n--------- AVERAGE RENTAL PRICE ---------")
                print(self.report_manager.get_average_rental_price())

            elif choice == 11:
                back_to_main_menu = True
    
    def run(self):
        exiting = False

        while not exiting:
            CityRideSystem.main_menu()

            choice = inputs.get_choice(4)

            if choice == 1:
                self.bikes_managment()

            elif choice == 2:
                self.rental_managment()

            elif choice == 3:
                self.reports_managment()
                
            elif choice == 4:
                print("Exiting...")
                exiting = True
        
        return 0
        

if __name__ == "__main__":
    system = CityRideSystem()
    system.run()
