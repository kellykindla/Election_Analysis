# Election_Analysis- Module3
## Project Overview 
###### For this module, we were presented with the election results for a Colorado Congressional Election. The election results file contained voter information including the Ballot ID, the county the vote was placed, and who the vote was for. From this data, we were challenged to practice our Python skills to:
	1. Calculate the total number of votes cast
	2. Get a complete list of candidates who received votes 
	3. Calculate the total number of votes each candidate received 
	4. Calculate the percentage of votes each candidate won 
	5. Determine the winner of the election based on popular vote

## Resources 
###### The data for the Module 3 analysis was from the **_election_results.csv_** file. 
###### Software used: 
	-Python 3.10.0
	-Visual Studio Code 1.62.0

## Summary and Results
### Summary of PyPoll 
###### From the initial analysis of our data, we found that the election results file contained 3 columns (Ballot ID, County, and Candidate) and 369,712 rows— that’s 369,711 votes. Although we were able to a basic understanding of the file from simply looking at it, we were challenged to take it a step further and analyze the data through Python. 
###### To do so, we first had to import the file into our script using the 
	‘Import csv’ and ‘import os’ dependencies and the following line of code:
		‘file_to_load = os.path.join("Resources", "election_results.csv”)’

###### After importing our data, we were able to perform our analysis. To count the total number of votes cast, we first created a variable, **total_votes**, and set it equal to zero so as we later looped through each row, we could add to the total vote count for each row present. Next, to create a complete list of candidates that received votes, we created an empty list, **candidate_options** where we added each original candidate name to the list as we cycled through each row. This was done through a conditional if statement looking to see if the candidate name was in the candidate option list and if it was not, the new name would be added. We further expanded this process and loop to collect the total number of votes that each candidate received by creating an empty dictionary, **candidate_votes**, that would later contain each candidate as the key and their votes as the value. For each occurrence of the candidate’s name, the value in the dictionary would increase by one, or add a vote to the candidates count. This dictionary was also used to find the percentage of votes that each candidate won. This was done by finding the vote count of each candidate and dividing it by the total number of votes. Lastly, to find the winner of each election by popular vote, we created a winning count tracker that would determine if, for each candidate, their votes were greater than the winning count. If their votes were greater than the winning count, they would be considered the winning candidate. 

### Results 
###### From our analysis, we found that:
	1. There were 369,711 total votes in the Colorado Congressional Election.
	2. The candidates in the election were:
		- Charles Casper Stockham
		- Diana DeGette
		- Raymon Anthony Doane
	3. The total number of votes each candidate received were:
		- Charles Casper Stockham received 85,213 votes
		- Diana DeGette received 272,892 votes
		- Raymon Anthony Doane received 11,606 votes 
	4. The percentage of votes each candidate won were:
		- Charles Casper Stockham = 23.0% of the votes
		- Diana DeGette = 73.8% of the votes
		- Raymon Anthony Doane = 3.1% of the votes
	5. Based on the analysis results, we find that the winner of the election based on popular vote was Diana Delete! 
##### The findings of our anlaysis were also output to a text file, as seen in the output below. 

<img width="331" alt="Module3_ElectionResults" src="https://user-images.githubusercontent.com/92558842/140550646-cdbede51-632f-4984-a8d9-fc3fc13c29ea.png">

