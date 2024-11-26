import json

# Example dictionary
data_dict = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# Convert the dictionary to a JSON-formatted string
json_data = json.dumps(data_dict, indent=4)

# Print the JSON data
print(json_data)
