import os
import _jsonnet
import json

directory_in_str = "schema"
directory = os.fsencode(directory_in_str)
    
for file in os.listdir(directory):
     filename = os.fsdecode(file)
     if filename.endswith(".jsonnet"): 
         res = json.loads(_jsonnet.evaluate_file(f"schema/{filename}"))
         avsc = open(f"schema/avro/{filename.replace('.jsonnet','.avsc')}" , "w")
         json.dump(res, avsc, indent=4)
         avsc.close()
