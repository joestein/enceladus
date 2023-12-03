local avro = import 'avro.libsonnet';

local ticker_record = import 'ticker.jsonnet';

local ticker_field = avro.Field(name="ticker", type=ticker_record);
local bought_at = avro.Field("boughtAt");

local position = avro.Record(
    name="position", 
    fields=[
            ticker_field,
            bought_at
        ], 
        namespace="domain.objects", 
        doc="main position object"
    );

position