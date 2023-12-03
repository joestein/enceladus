local avro = import 'avro.libsonnet';

local label = avro.Field("label");
local description = avro.Field("description");

local simulation = avro.Record(
    name="simulation", 
    fields=[
            label, 
            description
        ], 
        namespace="domain.objects",
        doc="main simulation object"
    );

simulation