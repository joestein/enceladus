import unittest
from io import BytesIO
import avro
from avro.io import BinaryEncoder, BinaryDecoder, DatumReader
from domain.objects import User
from domain.objects import Address
import json

#handles testing of objects like the address TODO move to utils
def to_dict(obj):
    return json.loads(json.dumps(obj, default=lambda o: o.__dict__))

class TestUser(unittest.TestCase):

    def test_encode_decode(self):
        user = User(email="test@example.com", first_name="Joe", last_name="Tester")

        file_of_schema = open("schema/avro/user.avsc", "rb")
        schema = avro.schema.parse(file_of_schema.read())
        file_of_schema.close()

        writer = avro.io.DatumWriter(schema)

        bytes_writer = BytesIO()
        encoder = BinaryEncoder(bytes_writer)
        writer.write(to_dict(user), encoder)

        raw_bytes = bytes_writer.getvalue()

        bytes_reader = BytesIO(raw_bytes)
        decoder = BinaryDecoder(bytes_reader)
        reader = DatumReader(schema)
        user_read = reader.read(decoder)

        self.assertEqual(to_dict(user), user_read)

    def test_address(self):
        address = Address(street_address="123 Elm St.")
        user = User(email="test@example.com", first_name="Joe", last_name="Tester", address=address)
        
        file_of_schema = open("schema/avro/user.avsc", "rb")
        schema = avro.schema.parse(file_of_schema.read())
        file_of_schema.close()

        writer = avro.io.DatumWriter(schema)

        bytes_writer = BytesIO()
        encoder = BinaryEncoder(bytes_writer)
        writer.write(to_dict(user), encoder)

        raw_bytes = bytes_writer.getvalue()

        bytes_reader = BytesIO(raw_bytes)
        decoder = BinaryDecoder(bytes_reader)
        reader = DatumReader(schema)
        user_read = reader.read(decoder)

        self.assertEqual(to_dict(user), user_read)     

if __name__ == '__main__':
    unittest.main()