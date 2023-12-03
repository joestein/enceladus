local avro = import 'avro.libsonnet';

local label = avro.Field("symbol");
local description = avro.Field("price");

local portfolio = avro.Record(
    name="portfolio", 
    fields=[
            label, 
            description
        ], 
        namespace="domain.objects", 
        doc="main portfolio object"
    );

portfolio