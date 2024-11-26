

import json

dictionary = {

    "name": "John",
    "age": 30,
    "city": "New York"

}

json_dictionary = json.dumps(dictionary)

print(json_dictionary)