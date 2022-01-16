import csv
import random
#import numpy
import os



# Assign a variable for the file to load and the path.
file_to_load = 'Resources/election_results.csv'
file_to_load = os.path.join("Resources", "election_results.csv")

# Open the election results and read the file
with open(file_to_load) as election_data:

     # Print the file object.
     print(election_data)

# Close the file.
election_data.close()


# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

    # Write some data to the file.
    ##txt_file.write("Hello World")
    # Write three counties to the file.
    ##txt_file.write("Arapahoe, ")
    ##txt_file.write("Denver, ")
    ##txt_file.write("Jefferson, ")

    # Write three counties to the file.
    ##txt_file.write("Arapahoe, Denver, Jefferson")

     # Write three counties to the file.
    txt_file.write("Counties in the Election\n----------------------\nArapahoe\nDenver\nJefferson")