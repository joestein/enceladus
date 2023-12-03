class User():
    def __init__(self, email="", firstName="", lastName="", address=None):
        self.email = email
        self.firstName = firstName
        self.lastName = lastName
        self.address = address

class Address():
    def __init__(self, street_address=""):
        self.street_address = street_address