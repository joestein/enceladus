class User():
    def __init__(self, email="", first_name="", last_name="", address=None):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.address = address

class Address():
    def __init__(self, street_address=""):
        self.street_address = street_address