counties = ["Arapahoe","Denver","Jefferson"]
counties_dict = {}
counties_dict["Arapahoe"] = 422829
counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438
#print(counties_dict)
#print(len(counties_dict))
#print(counties_dict.items())
voting_data = []
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})
#print(voting_data)

#counties = ["Arapahoe","Denver","Jefferson"]
#if counties[1] == 'Denver':
#    print(counties[1])

#for county in counties_dict.keys():
#    print(county)

#counties_dict = {"Arapahoe": 422829, "Denver":463353, "Jefferson": 432438}
#for county, voters in counties_dict.items():
#    print(county + " county has " + str(voters) + " registered voters.")

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
    {"county":"Denver", "registered_voters": 463353},
    {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)

for county_dict in voting_data:
    for value in county_dict.values():
        print(value)
