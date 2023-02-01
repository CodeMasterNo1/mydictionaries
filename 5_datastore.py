# Below is a dictionary that contains information about real estate space for
# a doctor's office. Using the dictionary, create a csv file that has details
# for each space represented as rows. Name your file 'retail_space.csv.


"""
Your final output should look like:

room-number,use,sq-ft,price
100,reception,50,75
101,waiting,250,75
102,examination,125,150
103,examination,125,150
104,office,150,100

"""


import csv

datastore = {
    "medical": [
        {"room-number": 100, "use": "reception", "sq-ft": 50, "price": 75},
        {"room-number": 101, "use": "waiting", "sq-ft": 250, "price": 75},
        {"room-number": 102, "use": "examination", "sq-ft": 125, "price": 150},
        {"room-number": 103, "use": "examination", "sq-ft": 125, "price": 150},
        {"room-number": 104, "use": "office", "sq-ft": 150, "price": 100},
    ]
}

csvfile = open("retail_space.csv", "w", newline="")
fieldnames = ["room-number", "use", "sq-ft", "price"]
writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

writer.writeheader()
for space in datastore["medical"]:
    writer.writerow(space)

csvfile.close()


outfile = open("retail_space.csv", "w")
outfile.write("room-number, use, sq-ft, price\n")

list1 = datastore["medical"]

for dict in list1:
    rn = dict["room-number"]
    use = dict["use"]
    sq = dict["sq-ft"]
    price = dict["price"]

    outfile.write(str(rn) + "," + use + "," + str(sq) + "," + str(price) + "\n")


outfile.close()
