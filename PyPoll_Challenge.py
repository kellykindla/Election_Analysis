# Add our dependencies.
import csv
import os

#Add a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Add a variable to save the file to a path.
file_to_save = os.path.join("Analysis","challenge_election_analysis copy.txt")

# Initialize a total vote counter.
total_votes = 0

# Create candidate_options- a list of candidates and candidate votes.
candidate_options = []
#create candidate_votes- a dictionary where candidates are the key 
    # and their votes are the value
candidate_votes = {}
#create county_list- a list holding the name of each county 
county_list = []
#create count_votes- a dictionary where each county is the key and 
    # it's votes are the values 
county_votes = {}

# variables created to track the winning candidate, vote count, and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0
#variables created to track the largest county and county voter turnout.
largest_county = ""
county_voter_turnout = 0 
county_voter_percentage = 0 

# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header row 
    header = next(reader)

    # For each row in the CSV file.
    for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1

        # Get the candidate name from each row.
        candidate_name = row[2]

        # Get the county name from each row
        county_name = row [1]

        # If the candidate does not match any existing candidate add it to
        # the candidate list
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        #if the county does not match any existing county, 
        # add it to the county list.
        if county_name not in county_list: 

            #add the county name to the county list
            county_list.append(county_name)

            #begin tracking that county's vote count 
            county_votes[county_name] = 0 
        #add a vote to that county's count 
        county_votes[county_name] += 1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

    # Print the final vote count (to terminal)
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")
    print(election_results, end="")

    txt_file.write(election_results)

     # For loop to get the county from the county dictionary
    for county_name in county_votes:

         #get the county vote count
         votes_per_county = county_votes[county_name]

         #calculate the percentage of votes for each county 
         county_percentage = (float(votes_per_county) / float(total_votes))*100

         #print the county results to the terminal 
         county_results = (f"{county_name}: {county_percentage:.1f} % ({votes_per_county:,})")
         print(county_results)

         # 6e: Save the county votes to a text file.
         txt_file.write(county_results+"\n")

         #create an if statement to determine the winning county and get its vote count.
         if (votes_per_county > county_voter_turnout) and (county_percentage > county_voter_percentage):
                #if true then set winning_county_count = votes per county and the winning counter_voter_percentage = county_percentage
                winning_county_count = votes_per_county
                county_voter_percentage = county_percentage
                # set winning_county equal to county name  
                largest_county = county_name
    # Print the county with the largest turnout to the terminal
    winning_county_summary = (
            f"\n-------------------------\n"
            f"Largest County Turnout: {largest_county}\n"
            f"--------------------------\n")
    print(winning_county_summary)
    #Save the county with the largest turnout to a text file.
    txt_file.write(winning_county_summary)

    # Save the final candidate vote count to the text file.
    for candidate_name in candidate_votes:

        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine the winning vote count, winning percentage, and winning candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    # Print the winning candidate results to the terminal
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)



        

