from datetime import *

class Rental:
    def __init__(
        self,
        rental_id: str,
        customer_name: str,
        bike_id: str,
        start_datetime: datetime,
        expected_return_datetime: datetime,
        actual_return_datetime: datetime | None,
        total_price: float,
        late_fee: float,
        status: str
    ):

        self.rental_id = rental_id
        self.customer_name = customer_name
        self.bike_id = bike_id
        self.start_datetime = start_datetime
        self.excepted_return_datetime = expected_return_datetime
        self.actual_return_datetime = actual_return_datetime
        self.total_price = total_price
        self.late_fee = late_fee
        self.status = status

    def complete_rental(self, return_datetime, late_fee):
        pass

    def to_dict(self):
        return {
            "rental_id": self.rental_id,
            "customer_name": self.customer_name,
            "bike_id": self.bike_id,
            "start_datetime": self.start_datetime,
            "expected_return_datetime": self.excepted_return_datetime,
            "actual_return_datetime": self.actual_return_datetime,
            "total_price": self.total_price,
            "late_fee": self.late_fee,
            "status": self.status
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            rental_id=data["rental_id"],
            customer_name=data["customer_name"],
            bike_id=data["bike_id"],
            start_datetime=data["start_datetime"],
            expected_return_datetime=data["expected_return_datetime"],
            actual_return_datetime=data["actual_return_datetime"],
            total_price=data["total_price"],
            late_fee=data["late_fee"],
            status=data["status"]
        )