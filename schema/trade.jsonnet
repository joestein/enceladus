local avro = import 'avro.libsonnet';

local ticker_record = import 'ticker.jsonnet';
local ticker_field = avro.Field("ticker", type=ticker_record);
local total_purchase = avro.Field("total_purchase", type="int");
local purchase_date = avro.Field("purchase_date", nullable=true);

local trade = avro.Record(
    name="trade", 
    fields=[
            ticker_field,
            total_purchase,
            purchase_date
        ], 
        namespace="domain.objects",
        doc="main trade object"
    );

trade