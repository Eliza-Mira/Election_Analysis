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
# retrieve only the values from dictionary
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
# counties_dict[Arapahoe]
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

#QUIZ-1 Add El Paso & reg voters to 2nd position
voting_data.append({"county": "El Paso", "registered_voters":461149})
#test voting data dict
voting_data

#QUIZ-2 Remove Arapanhoe & voters
voting_data.remove({"county":"Arapahoe", "registered_voters": 422829})
#test voting data dict
voting_data

#QUIZ-3 Keep Jefferson in 2nd but Move Denver to 3rd
voting_data.remove({"county": "Jefferson", "registered_voters": 432438})
voting_data.remove({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county": "Jefferson", "registered_voters": 432438})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data

#QUIZ-4 Arapanhoe & registered voters
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data

# 3.2.8 Practice DECISION STATEMENTS
# How many votes did you get?
my_votes=int(input("How many votes did you get in the election? "))

#  Total votes in the election
total_votes=int(input("What is the total votes in the election? "))

# Calculate the percentage of votes you received.
percentage_votes=(my_votes/total_votes) * 100
print("I received " + str(percentage_votes)+"% of the total votes.")

#Per 3.2.8 lesson: Create new file named python_practice.py.  BUT I've been in python_practice.py this entire time.  Confused.
counties = ["Arapahoe","Denver","Jefferson"]
if counties[1] == 'Denver':
   print(counties[1])
#Code is GOOD here

#3.2.9 MEMBERSHIP & LOGICAL OPERATORS

#Practice creating a membership operation
counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")

#3.2.10 REPETITION STATEMENTS : Create/Implement FOR LOOP by iterating thru list of counties.
counties = ["Arapahoe","Denver","Jefferson"]
counties
for county in counties:
    print(county)

    numbers = [0, 1, 2, 3, 4]
for num in numbers:
    print(num)

for num in range(5):
    print(num)

for i in range(len(counties)):
    print(counties[i])

#3.2.10 Iterate Through a Dictionary
#Practice getting the keys and values from a dictionary
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
counties_dict

for county in counties_dict:
    print(county)

for county in counties_dict.keys():
    print(county)

# #Get the Values of a Dictionary
# for voters in counties_dict.values():
#     print(voters)

#3.2.10 modify the for loop and use the key, county to reference the value
for county in counties_dict:
    print(counties_dict[county])

#Another method get() method
for county in counties_dict:
    print(counties_dict.get(county))

