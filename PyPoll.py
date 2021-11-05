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
#open the total_votes variable before file opens because the value must be zero every time we run the file
total_votes = 0 
#list of candidates
candidate_options = [] 
#dictionary of candidates and their votes 
candidate_votes = {}
#winning candidate and count tracker 
winning_candidate = ""
winning_count = 0 
winning_percentage = 0 

#open the election results and read the file 
with open(file_to_load) as election_data:

    #to do: perform analysis- read and analyze data 
    #read the file object with the reader function; file_reader references the file object
    file_reader = csv.reader(election_data)  

    #read the header row 
    headers = next(file_reader)
    
    #print each row in the csv file
    for row in file_reader:
        #add to the total vote count 
        total_votes += 1
        #print the candidate name from each row 
        candidate_name = row[2]
        #if the candidate does not match any existing candidate then add to list
        if candidate_name not in candidate_options:
            #add candidates name to candidate list 
            candidate_options.append(candidate_name)
            #create each candidate as a key for dictionary and track that candidates vote count by setting it equal to zero
            candidate_votes[candidate_name] = 0 
        #add a vote to that candidate count
        candidate_votes[candidate_name] +=1

        

     #determine percentage of votes for each candidate by looping through the counts
    #iterate through candidate list 
    for candidate_name in candidate_votes:
        #get vote count of a candidate
        votes = candidate_votes[candidate_name]
        #calculate the percentage of votes using float decimals
        vote_perecentage = (float(votes) / float(total_votes))*100
        #print candidate name and percentage of votes 
        print(f"{candidate_name}: {vote_perecentage:.1f} % ({votes:,})\n")
        
        #determine winning vote and candidate
        #determine if votes are greater than winning count 
        if (votes > winning_count) and (vote_perecentage > winning_percentage):
            #if true then set winning_count = votes and winning_percent = vote_percent
            winning_count = votes
            winning_percentage = vote_perecentage
            # set winning_candidate equal to candidates name 
            winning_candidate = candidate_name
    #winning candidate summary
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"--------------------------\n")
    print(winning_candidate_summary)

#print total votes (should be equal to the number of rows in file minus the header)
#print(total_votes)
#print candidate list 
#print(candidate_options)
#print candidate vote dictionary 
#print (candidate_votes) 
  
    

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




