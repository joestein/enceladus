local avro = import 'avro.libsonnet';
local position_record = import 'position_record.jsonnet';

local label = avro.Field("label");
local description = avro.Field("description");

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