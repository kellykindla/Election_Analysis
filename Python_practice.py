#if statement practice
# counties = ["Arapahoe","Denver","Jefferson"]
#if counties[1] == "Denver":
#    print(counties[1])
#temperature = int(input("What is the temperature outside?"))

#if else statememnt practice
#if temperature > 80:
#    print("Turn on the AC")
#else: 
#    print("Open the windows.")

#nested if statements 
#what is the score?
#score = int(input("What is your test score?"))

#determine the grade 
#if score >= 90:
#    print("your grade is an A")
#elif score >= 80:
#    print("Your grade is a B")
#elif score>=70:
#    print("your grade is a C")
#elif score >=60:
#    print("your grade is a D")
#else: 
#    print("your grade is an F")

#membership operation practice 
#counties = ["Arapahoe", "Denver","Jefferson"]
#if "El Paso" in counties:
#    print("El Paso is in the list of counties")
#else: 
#    print("El Paso is not in the list of counties")
#practice using logical operators 
#if "Arapahoe" in counties and "El Paso" not in counties:
#    print("Arapahoe is in the list of counties")
#else:
#    print("Arapahoe is in the list of counties and El Paso is not")

#practice using for loops
#for county in counties:
#    print (county)

#practice with for loops and dictionaries 
#counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
#get keys or value of dictionary
#for county in counties_dict:
#    print(counties_dict.get(county))
#skill drill 3.2.10
#for county,voters in counties_dict.items():
#    print(county +" county has "+ str(voters) +" registered voters")
#or using f string 
#   print(f"{county} county has {voters,} registered voters.")

#practice looping through a list of dictionaries 
#voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
#                {"county":"Denver", "registered_voters": 463353},
#                {"county":"Jefferson", "registered_voters": 432438}]
#print each dictionary
# for county_dict in range(len(voting_data)):
#    print(voting_data[county_dict])
#print values of dictionary
#for county_dict in voting_data:
#   for value in county_dict.values():
#        print(value)

#practice with while loops
#x = 0
#while x <= 5:
#    print(x)
#    x = x + 1

#practice with f string including number formating  
candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes:,} number of votes. "
    f"The total number of votes in the election was {total_votes:,}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

print(message_to_candidate)
