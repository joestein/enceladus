local avro = import 'avro.libsonnet';

local symbol = avro.Field("symbol");
local price = avro.Field("price");

local ticker = avro.Record(
    name="ticker", 
    fields=[
            symbol, 
            price
        ], 
        namespace="domain", 
        doc="main ticker object"
    );

ticker