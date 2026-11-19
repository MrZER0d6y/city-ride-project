from datetime import *
import math


class PricingManager:
    @staticmethod
    def calculate_price(bike, start_datetime, expected_return_datetime):
        duration = expected_return_datetime - start_datetime

        total_hours = math.ceil(duration.total_seconds() / 3600)
        days, hours = divmod(total_hours, 24)

        return days * bike.daily_price + hours * bike.hourly_price

    @staticmethod
    def calculate_late_fine(expected_return_time, actual_return_time):
        duration = actual_return_time - expected_return_time

        if duration <= 0:
            return 0.0

        elif duration.hour > 3:
            return 100.0
        
        elif duration.hour > 1:
            return 50.0
        
        return 20.0