# Election_Analysis Module 3 

## Project Overview 
### Purpose of Module 3
In this module, we were introduced to Python and given data and instructions in aims for us to create scripts that utilize decision statements for complex comparisons, perform mathematical operations, and potentially read, store, and write data to and from files. To do this, we were introduced to election results and challenged to complete and audit of this election data. Our purpose was to sort and read the data and analyze its contents so conclusions can be drawn based on the election results. 

### Overview of Assignment 
For this assignment, we were given election results for three counties in Colorado pertaining to the congressional election.  This data contained the Ballot ID, the county, and the candidate the vote was cast for. From this data, we were challenged to find the total number of votes cast, the votes and their associated percentage for each candidate and county, the county with the largest voter turnout, and the overall winner based on popular vote. 

### Resources 
The data for the Module 3 analysis was from the **_election_results.csv_** file. 
#### Software used: 
	-Python 3.10.0
	-Visual Studio Code 1.62.0


## Election Audit Results 
### Initial Analysis of Election Results 
From a visual analysis of the **“election_results.csv“** file, we are able to see that the data contains 3 columns: Ballot ID, County, and Candidate. We are also able to conclude that there is 369,712 rows of data— that’s 369,711 votes! In order to expedite this analysis, we turn to Python to further analyze the data. To do so, we have to read the file by first importing our dependencies and load the file from its path. Since we also want to write our results to a text file, we initialize that variable and find its path so the file can be called later on. This is all done through the first 8 lines of code below: 

<img width="661" alt="Module3_pathsAndDependencies" src="https://user-images.githubusercontent.com/92558842/140799540-dfef85ce-fe63-4973-8451-b6e6ea50b100.png">


### Overview of the Script 
After reading the data, we are able to perform our analysis. To begin, we created a variable, **total_votes**, which was set equal to zero and acted as our vote counter to obtain the total votes from the election by looping through each row of data and adding to the counter for each row present. We next defined two empty lists and two empty dictionaries which would contain a list of all candidates and counties and their associated votes. The contents of the list were acquired through the logical operation below for both the candidate list and county list in which we looped through each row, collected the name, checked to see if that name was in the list already and if it wasn’t, we added it to the list and counted its occurrence in the data. The votes cast were then stored in the empty dictionaries where the candidate or county were the key and their respected votes were the value. 

<img width="634" alt="Module3_CreatingLists" src="https://user-images.githubusercontent.com/92558842/140799598-f676f05c-8668-4593-9133-8dc574fdacb2.png">

We then looped through the contents of each dictionary to get the votes for each county and each candidate. After discovering their respected votes, we then calculated its percentage by dividing it by the total number of votes. For example, with a county, we used the following code:
	
	county_percentage = (float(votes_per_county) / float(total_votes))*100 

Lastly, to discover the largest county and the overall winner of the election by popular vote, we created a vote tracker for the candidate selection and county options and by using conditionals, we checked to see if the total votes for each candidate or county were greater than the others in their respected lists. If the candidate or county had the largest vote count compared to the others, it would be stored as the winning variable and thus, be deemed the winner. 

### Results 
From the analysis of the election results, we find that:

	1. There were 369,711 total votes in the Colorado Congressional Election. 
	2. The counties in the election and their associated voter turnout were:
		- Jefferson County with 38,855 voters, resulting in 10.5% of the voters being from this county. 
		- Denver County with 306,055 voters, resulting in 82.8% of the voters being from this county. 
		- Arapahoe County with 24,801 voters, resulting in 6.7% of the voters being from this county. 
	3. The candidates in the election were: 
		- Charles Casper Stockham
		- Diana DeGette
		- Raymon Anthony Doane
	4. The total number of votes each candidate received were:
		- Charles Casper Stockham received 85,213 votes or 23.0% of the votes. 
		- Diana DeGette received 272,892 votes or 73.8% of the votes. 
		- Raymon Anthony Doane received 11,606 votes or 3.1% of the votes. 
	5. Denver had the largest county turnout. 
	6. Diana DeGette was the winner of the election by popular vote, receiving 73.8% of the votes or rather, 272,892 total votes. 
The results for the analysis were not only output to the terminal but were saved to the text file we created. The outputs for both are shown below: 
#### Terminal Output: 
<img width="752" alt="Module3_TerminalOutput" src="https://user-images.githubusercontent.com/92558842/140799756-5efe4d34-5ccc-4bf3-bf70-cb3cf64a8d92.png">

#### Text File: 
<img width="310" alt="Module3_TextFileOutput" src="https://user-images.githubusercontent.com/92558842/140799817-b239fee0-fc1f-4094-b966-aefa46d94740.png">


### Election Audit Summary 
This script can become the backbone for an expanded analyses for the election committee. Not only can the file simply be changed to analyze a congressional election for another state or even results with a larger data set with more counties, it has the potential to do much more. This script alone is beneficial for the committee by presenting the winner of the election and by providing data regarding voter turnout by county. This information can be used by the candidates party to gather which county had the lowest margins so the candidate can put resources into that county to win over their votes and potentially win the campaign. Similarly, the script and data set can be expanded to collect something like voter zip codes or demographics (by adding a list and collecting votes for each like we did with each candidate and county) to determine voter turnout so political parties know where to send their resources to potentially receive more votes. We can also expand the script to collect data regarding candidate and voter political party association to gather data regarding any correlations between voter party and candidate party. By initializing nested for loops we can also sort through counties or zip codes for each candidate to determine how many votes were cast for each candidate in each county or zip code. In essence, this script can be used for any election by simply analyzing what was voted for (i.e. change candidate name to proposition name) and loop through the results to determine the outcome in an efficient manner. It can also be used in any election to gather voter turnout and determine if there is any association between variables like age or region and vote cast by creating more complex logical operations for that variable within the candidate or proposition vote list. 




