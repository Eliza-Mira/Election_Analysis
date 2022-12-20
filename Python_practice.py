print("hello world")
type(3)
type(2,019)
type("2,019")
type(2019)
ballots = 1,341
ballots
type(ballots)
type(73.81)
float(73.81)
type("hello world")
type(" ")
type(True)
type('True')
type('True')
print("Where am i?")

counties = ["Arapahoe", "Denver", "Jefferson"]
my_list=list()
counties

print(counties[2])
print(counties[-1])
print(counties[-2])

len(counties)
counties[0:2]

counties[0:3]
counties[0:1]
len(counties)

counties[1:]
counties

counties.append("El Paso")
counties

counties.insert(2, "El Paso")
counties

counties.pop(2)
counties

counties[2]="El Paso"
counties

counties.insert(1, "El Paso")
counties

counties.remove("Arapahoe")
counties

counties.insert(1, "Jefferson")
counties

counties.append("Arapahoe")
counties
# testing comment

counties_tuple = ("Arapahoe","Denver","Jefferson")
len(counties_tuple)

counties_tuple[1]

counties_tuple[:-2]
counties_tuple[:2]
counties_tuple[:-1]
counties_tuple[1:2]

# create a dictionary
#create an empty dictionary 1st
counties_dict = {}

counties_dict["Arapahoe"] = 422829
counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438

counties_dict

# To get only the keys
counties_dict.keys()
# retrieve only the values
counties_dict.values()
# Get a Specific Value
counties_dict.get("Denver")

# How would you get # of Arapahoe registered voters
# ALL have the same output of 422829
counties_dict['Arapahoe']
counties_dict.get("Arapahoe")
print(counties_dict['Arapahoe'])
print(counties_dict.get("Arapahoe")) 
# same quest but w/o quotes (single or double)
counties_dict[Arapahoe]
# INCLUDE the quotes
counties_dict['Arapahoe']
counties_dict["Arapahoe"]

#create a list of dictionaries
#Keys: country & registered voters

# FIRST create empty list
voting_data = []
# add/append ea dict
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})
#test voting data dict
voting_data

#quiz Add El Paso & reg voters to 2nd position
voting_data.append({"county": "El Paso", "registered_voters":461149})
#test voting data dict
voting_data

#quiz Remove Arapanhoe & voters
voting_data.remove({"county":"Arapahoe", "registered_voters": 422829})
#test voting data dict
voting_data

#Keep Jefferson in 2nd but Move Denver & voters to 3rd