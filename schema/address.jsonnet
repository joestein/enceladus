local avro = import 'avro.libsonnet';

local street_address = avro.Field("street_address", nullable=true);
local preferred = avro.Record(
    name="preferred",
    fields=[street_address],
    namespace="domain.objects"
);

preferred