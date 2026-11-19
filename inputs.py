from validations import *
from datetime import *

class Inputs:
    @staticmethod
    def get_choice(number):
        valid_choice = False

        while not valid_choice:
            choice = Validations.get_integer("Choice")

            if choice > number:
                print(f"Choice must be between 1 and {number}, try again.")
                continue

            valid_choice = True
        
        return choice

    @staticmethod
    def get_model():
        return Validations.get_string("Model").title()
    
    @staticmethod
    def get_bike_type():
        valid_bike_type = False

        while not valid_bike_type:
            bike_type = Validations.get_string("Bike Type (Regular/Electric/Mountain)").title()

            if bike_type not in ("Regular", "Electric", "Mountain"):
                print("Bike Type must be Regular/Electric/Mountain, try again.")
                continue

            valid_bike_type = True
        
        return bike_type
    
    @staticmethod
    def get_hourly_price():
        return Validations.get_float("Hourly Price")
    
    @staticmethod
    def get_daily_price():
        return Validations.get_float("Daily Price")
    
    @staticmethod
    def get_customer_name():
        return Validations.get_string("Customer Name").title()
    
    @staticmethod
    def get_bike_id(bikes):
        valid_bike_id = False

        while not valid_bike_id:
            bike_id = Validations.get_integer("Bike ID")

            if bike_id <= len(bikes):
                return f"R{bike_id:03d}"
            
            print("Bike ID not valid, try again.")
    
    @staticmethod
    def get_rental_id(rentals):
        valid_rental_id = False

        while not valid_rental_id:
            rental_id = Validations.get_integer("Rental ID")

            if rental_id <= len(rentals):
                return f"R{rental_id:03d}"
            
            print("Rental ID not valid, try again.")
    
    @staticmethod
    def get_year():
        valid_year = False

        while not valid_year:
            year = Validations.get_integer("Year")

            valid_year = True
        
        return year
    
    @staticmethod
    def get_month():
        valid_month = False

        while not valid_month:
            month = Validations.get_integer("Month")

            if month > 12:
                print("\nMonth cannot be more than 12, try again.")
                continue

            valid_month = True
        
        return month

    @staticmethod
    def get_day():
        valid_day = False

        while not valid_day:
            day = Validations.get_integer("Day")

            if day > 31:
                print("\nDay cannot be more than 31.")
                continue

            valid_day = True
        
        return day

    @staticmethod
    def get_hour():
        valid_hour = False

        while not valid_hour:
            hour = Validations.get_integer("Hour")

            if hour > 23:
                print("\nHour cannot be more than 23, try again.")
                continue

            valid_hour = True
        
        return hour
    
    @staticmethod
    def get_minute():
        valid_minute = False

        while not valid_minute:
            minute = Validations.get_integer("Minute")

            if minute > 59:
                print("\nMinutes cannotbe more than 29, try again.")

            valid_minute = True
        
        return minute
    
    @staticmethod
    def get_excepted_return_datetime():
        valid_date = False
        
        while not valid_date:
            try:
                expected_datetime = datetime(Inputs.get_year(), Inputs.get_month(), Inputs.get_day(), Inputs.get_hour(), Inputs.get_minute())
            except ValueError:
                print("\nDate not valid, try again.")
                continue

            if expected_datetime < datetime.now():
                print("\nDatetime is aready past, try again..")
                continue

            valid_date = True
        
        return expected_datetime
    
    @staticmethod
    def get_update_bike():
        valid_choice = False

        while not valid_choice:
            choice = Validations.get_string("Hourly Price / Daily Price").title()

            if choice not in ("Hourly Price", "Daily Price"):
                print("Choice must be Hourly Price / Daily Price, try again.")
                continue
            
            valid_choice = True

        return choice
    
    @staticmethod
    def get_operational_status():
        valid_status = False

        while not valid_status:
            status = Validations.get_string("Is Operational? (True/False)").title
            
            if status not in ("True", "False"):
                print("Operational status must be True / False, try again.")
                continue

            valid_status = True

        return status        


inputs = Inputs()