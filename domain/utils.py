def dict_to_instance(instance, dict):
   for key in dict: 
     setattr(instance, key, dict[key])