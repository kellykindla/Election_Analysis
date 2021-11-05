#The data we need to retrieve
# 1. The toal number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won 
# 4. The toal number of votes each candidate won 
# 5. The winner of the election based on popular vote 

#importing the csv module and os dependencies
import csv
import os
#dir(csv)

#assign a variable for the file to load and the path- using direct path
# for direct path: 
# file_to_load = 'Resources/election_results.csv'
#for indirect path:
file_to_load = os.path.join("Resources", "election_results.csv")

#open the election results and read the file 
with open(file_to_load) as election_data:

    #to do: perform analysis- read and analyze data 
    #read the file object with the reader function; file_reader references the file object
    file_reader = csv.reader(election_data)  

    #print each row in the csv file
    #for row in file_reader:
    #    print(row) 
    #print the header row 
    headers = next(file_reader)
    print(headers)

#create a filename variable to a direct or indirect path to the file 
file_to_save = os.path.join("Analysis", "election_analysis.txt")
#use the open() funciton with the "W" mode t write data to the file 
#outfile = open(file_to_save, "w")
#write some data to the file ; write function is from the os module
#outfile.write("Hello World")
#close outfile 
#outfile.close()

#use the with statement to open the file as a text file 
with open(file_to_save, "w") as txt_file:

    #write three counties to the file using the newline escape sequence 
    txt_file.write("Counties in the Election\n")
    txt_file.write("--------------------------\n")
    txt_file.write("Arapahoe\nDenver\nJefferson")




