local avro = import 'avro.libsonnet';
local trade_record = import 'trade.jsonnet';

local trades = avro.Array(trade_record);
local holding = avro.Field("holding", type=trades, doc="what trades where made we still have to execute on");

local position = avro.Record(
    name="position", 
    fields=[
            holding
        ], 
        namespace="domain.objects", 
        doc="main position object"
    );

position