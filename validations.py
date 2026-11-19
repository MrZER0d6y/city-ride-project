class Validations:
    @staticmethod
    def get_string(text):
        valid_string = False

        while not valid_string:
            string = input(f"{text}: ").strip()

            if not string:
                print(f"{text} cannot be empty, try again.")
                continue

            valid_string = True
        
        return string
    
    @staticmethod
    def get_float(text, negative=False):
        valid_float = False
        
        while not valid_float:
            try:
                number = float(input(f"{text}: "))
            except ValueError:
                print(f"{text} must be float, try again.")
                continue

            if not negative and number < 1:
                print(f"{text} must be positive, try again.")
                continue

            valid_float = True
        
        return float(number)
    
    @staticmethod
    def get_integer(text, negative=False):
        valid_integer = False

        while not valid_integer:
            try:
                number = float(input(f"{text}: "))
            except ValueError:
                print(f"{text} must be integer, try again.")
                continue

            if not negative and number < 1:
                print(f"{text} must be positive, try again.")
                continue

            valid_integer = True
        
        return int(number)

validations = Validations()