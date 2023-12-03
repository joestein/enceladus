class User():
    def __init__(self, email="", first_name="", last_name="", address=None):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.address = address

class Address():
    def __init__(self, street_address=""):
        self.street_address = street_address

class Ticker():
    def __init__(self, symbol="", price="0.0"):
        self.symbol = symbol
        self.price = price

class Trade():
    def __init__(self, ticker=Ticker(), total_purchase=0, purchase_date=""):
        self.ticker = ticker
        self.total_purchase = total_purchase
        self.purchase_date = purchase_date

class Position():
    def __init__(self, holding=[]):
        self.holding = holding