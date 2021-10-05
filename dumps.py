

# import json
# a={"name":"sonam","age":20,"city":"Ghazipur"}
# mystring = json.dumps(a)
# print(mystring)




import json

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y) 