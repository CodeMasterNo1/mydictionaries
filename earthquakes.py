"""
the eq_data file is a json file that contains detailed information about
earthquakes around the world for a period of a month.

NOTE: No hard-coding allowed except for keys for the dictionaries

1) print out the number of earthquakes

2) iterate through the dictionary and extract the location, magnitude, 
   longitude and latitude of the location and put it in a new
   dictionary, name it 'eq_dict'. We are only interested in earthquakes that have a 
   magnitude > 6. Print out the new dictionary.

3) using the eq_dict dictionary, print out the information as shown below (first three shown):

Location: Northern Mid-Atlantic Ridge
Magnitude: 6.2
Longitude: -36.0923
Latitude: 35.4364


Location: 166km SSE of Muara Siberut, Indonesia
Magnitude: 6.1
Longitude: 100.0208
Latitude: -2.8604


Location: 14km ENE of Puerto Madero, Mexico
Magnitude: 6.6
Longitude: -92.2981
Latitude: 14.7628

"""


import json

# 1 print out the number of earthquakes
infile = open("eq_data.json", "r")
eq_data = json.load(infile)
eqs = eq_data["features"]
print("Number of earthquakes: ", len(eqs))
print()

# 2) iterate through the dictionary and extract the location, magnitude, longitude and latitude of the location and put it in a new
#   dictionary, name it 'eq_dict'. We are only interested in earthquakes that have a magnitude > 6. Print out the new dictionary.

eq_dict = {}
for eq in eqs:
    if eq["properties"]["mag"] > 6:
        eq_dict[eq["properties"]["place"]] = {
            "magnitude": eq["properties"]["mag"],
            "longitude": eq["geometry"]["coordinates"][0],
            "latitude": eq["geometry"]["coordinates"][1],
        }
print("Earthquakes with magnitude greater than 6 dictionary: \n\n", eq_dict)


# 3) using the eq_dict dictionary, print out the information as shown below (first three shown):

# for eq_info in eq_dict:
# print("Location: ", eq_info)
# print("Magnitude: ", eq_info["magnitude"])

print("\nEarthquakes with magnitude greater than 6 location details: \n\n")
for location in eq_dict:
    details = eq_dict[location]
    magnitude = details["magnitude"]
    longitude = details["longitude"]
    latitude = details["latitude"]
    print(f"Location: {location}")
    print(f"Magnitude: {magnitude}")
    print(f"Longitude: {longitude}")
    print(f"Latitude: {latitude}")
    print("\n")
