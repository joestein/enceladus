{
    Record(name, fields, namespace="", doc="")::
    {
        "name": name,
        [if namespace != "" then "namespace"]: namespace,
        [if doc != "" then "doc"]: doc,
        "fields": fields,
        "type": "record"
    },
    Field(name, type="string", default={}, nullable=false, doc="")::
    {   
        [if doc != "" then "doc"]: doc,
        "name": name,
        "type": if nullable then [type, "null"] else type,
        [if default != {} then "default"]: default,
    },
    Array(items)::
    {
        "type": "array",
        "items": items
    }
}