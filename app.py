def get_value(data, key):
    keys = key.split("/")  # Split the key with delimeter:'/' 
    value = data
    for k in keys: # iterate over the splited keys
        if isinstance(value, dict) and k in value: #checks for keys in object using built in functions/data type.
            value = value[k]
        else:
            return None  # Return None if the key is not found
    return value

# Simple Test:
nested_json = {
    "a":{
        "b":{"c":"d"}
    }
}
key = "a/b/c"
result = get_value(nested_json, key)
print(result) 

nested_json = {
    "x":{
        "y":{"z":"a"}
    }
}
key = "x/y/z"
result = get_value(nested_json, key)
print(result) 