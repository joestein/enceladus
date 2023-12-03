local avro = import 'avro.libsonnet';

local email = avro.Field("email");
local firstName = avro.Field("firstName");
local lastName = avro.Field("lastName");


local address = import 'address.jsonnet';

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
