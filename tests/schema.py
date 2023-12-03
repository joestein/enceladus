import unittest
from io import BytesIO
import avro
from avro.io import BinaryEncoder, BinaryDecoder, DatumReader
from domain.objects import User, Address, Trade, Position, Ticker
from domain.utils import to_dict, get_avro_schema, avro_bytes_from_object, avro_bytes_to_dict

def avro_write_read(avsc, object):
    schema = get_avro_schema(avsc)

    raw_bytes = avro_bytes_from_object(schema, object)

    return avro_bytes_to_dict(schema, raw_bytes)

class TestSchemas(unittest.TestCase):

    def test_user(self):
        user = User(email="test@example.com", first_name="Joe", last_name="Tester")

        read = avro_write_read("schema/avro/user.avsc", user)

        self.assertEqual(to_dict(user), read)

    def test_address_embedded_user(self):
        address = Address(street_address="123 Elm St.")
        user = User(email="test@example.com", first_name="Joe", last_name="Tester", address=address)
        
        read = avro_write_read("schema/avro/user.avsc", user)

        self.assertEqual(to_dict(user), read) 

    def test_position_array_trade_nested_ticker(self):
        ticker1 = Ticker(symbol="AAPL", price="190.23")
        ticker2 = Ticker(symbol="XYZ", price="23.23")

        trade1 = Trade(ticker=ticker1, total_purchase=10, purchase_date="2023-12-3")
        trade2 = Trade(ticker=ticker2, total_purchase=10, purchase_date="2023-12-3")
        
        position = Position(holding=[trade1, trade2])
        
        read = avro_write_read("schema/avro/position.avsc", position)

        self.assertEqual(to_dict(position), read) 

if __name__ == '__main__':
    unittest.main()