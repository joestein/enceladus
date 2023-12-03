local avro = import 'avro.libsonnet';

local label = avro.Field("symbol");
local description = avro.Field("price");

local simulation = avro.Record(
    name="simulation", 
    fields=[
            label, 
            description
        ], 
        namespace="domain", 
        doc="main simulation object"
    );

simulation