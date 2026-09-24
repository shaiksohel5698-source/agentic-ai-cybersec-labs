# Dictionary is nothing but key values pairs
d1 = {}
# print(type(d1))
d2 = {"harry": "burger", "rohan": "fish", "skillf": "Roti","shubham": {"B": "maggie", "L": "roti", "D": "chicken"}}
# print(d2["rohan"])  # it will print the value of key rohan
# print(d2["shubham"]["B"])  # it will print the value of key B in the nested dictionary of key shubham
#d2["ankit"] = "Junk Food"  # it will add a new key value pair in the dictionary
#d2[420] = "Kachori"  # it will add a new key value pair in the dictionary
# print(d2)  # it will print the whole dictionary
# del d2["rohan"]  # it will delete the key value pair with key "rohan"

# print(d2)  # it will print the whole dictionary with new key value pair

# d3 = d2.copy()  # it will create a copy of d2 and store it in d3
# del d3["harry"]  # it will delete the key value pair with key "harry" from d3 and also from d2 because both are pointing to same dictionary
# print(d2)  # it will print the whole dictionary without key value pair of 
#d2.update({"leena": "toffee"}) # it will add a new key value pair in the dictionary
#print(d2)  # it will print the whole dictionary with new key value pair
#print(d2.keys())  # it will print all the keys of the dictionary
# print(d2.items())  # it will print all the key value pairs of the dictionary
# print(d2.values())  # it will print all the values of the dictionary
print(d2.get("harry"))  # it will print the value of key "harry"