local avro = import 'avro.libsonnet';

local email = avro.Field("email");
local first_name = avro.Field("first_name");
local last_name = avro.Field("last_name");

local address_record = import 'address.jsonnet';

local address_field = avro.Field("address", address_record, nullable=true);

local user = avro.Record(
    name="user", 
    fields=[
            email, 
            first_name, 
            last_name,
            address_field
        ], 
        namespace="domain.objects",
        doc="main user object"
    );

user
