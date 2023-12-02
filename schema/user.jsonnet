local avro = import 'avro.libsonnet';

local email = avro.Field("email");
local firstName = avro.Field("firstName");
local lastName = avro.Field("lastName");

local street_address = avro.Field("street_address", nullable=true);
local preferred = avro.Record(
    name="preferred",
    fields=[street_address]
);

local address = avro.Field("address", preferred, nullable=true);

local user = avro.Record(
    name="user", 
    fields=[
            email, 
            firstName, 
            lastName,
            address
        ], 
        namespace="domain", 
        doc="main user object"
    );

user
