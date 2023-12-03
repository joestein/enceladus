import avro
from avro.io import BinaryEncoder, BinaryDecoder, DatumReader
from io import BytesIO
import json

def to_dict(obj):
    return json.loads(json.dumps(obj, default=lambda o: o.__dict__))

def dict_to_instance(instance, dict):
   for key in dict: 
     setattr(instance, key, dict[key])

def get_avro_schema(avsc):
    file_of_schema = open(avsc, "rb")
    schema = avro.schema.parse(file_of_schema.read())
    file_of_schema.close()
    return schema

def avro_bytes_from_object(schema, object):
    writer = avro.io.DatumWriter(schema)

    bytes_writer = BytesIO()
    encoder = BinaryEncoder(bytes_writer)
    writer.write(to_dict(object), encoder)

    raw_bytes = bytes_writer.getvalue()   

    return raw_bytes

def avro_bytes_to_dict(schema, raw_bytes):
    bytes_reader = BytesIO(raw_bytes)
    decoder = BinaryDecoder(bytes_reader)
    reader = DatumReader(schema)
    dict = reader.read(decoder)   
    return dict