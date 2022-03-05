# Project #1 
# EPL Seasons 09-10 to 18-19

import pandas as pd
from operator import getitem
import copy
import re

"""
Step 1
Import the data of all CSV files and create a DataFrame for each CSV file
"""

df_0910 = pd.read_csv("season_0910.csv", index_col=0)
df_1011 = pd.read_csv("season_1011.csv", index_col=0)
df_1112 = pd.read_csv("season_1112.csv", index_col=0)
df_1213 = pd.read_csv("season_1213.csv", index_col=0)
df_1314 = pd.read_csv("season_1314.csv", index_col=0)
df_1415 = pd.read_csv("season_1415.csv", index_col=0)
df_1516 = pd.read_csv("season_1516.csv", index_col=0)
df_1617 = pd.read_csv("season_1617.csv", index_col=0)
df_1718 = pd.read_csv("season_1718.csv", index_col=0)
df_1819 = pd.read_csv("season_1819.csv", index_col=0)

#Function to create lists of the teams that played in each season
def createTeamNamesList(df, df_length):
	team_list = []
	# Traverse each row in the data frame
	for i in range(df_length):
		# Get the team name from the home team column
		team_name = df.iat[i, 1]
		# If team name is not in team list, add the team name to list 
		if team_name not in team_list:
			team_list.append(team_name)
	#Return list
	return team_list

"""
Step 2
Declare lists to store that teams that played in each season
Call the createTeamNamesList function to create the list of teams
"""
teams_0910 = createTeamNamesList(df_0910, len(df_0910)) #Season 0910
teams_1011 = createTeamNamesList(df_1011, len(df_1011)) #Season 1011
teams_1112 = createTeamNamesList(df_1112, len(df_1112)) #Season 1112
teams_1213 = createTeamNamesList(df_1213, len(df_1213)) #Season 1213
teams_1314 = createTeamNamesList(df_1314, len(df_1314)) #Season 1314
teams_1415 = createTeamNamesList(df_1415, len(df_1415)) #Season 1415
teams_1516 = createTeamNamesList(df_1516, len(df_1516)) #Season 1516
teams_1617 = createTeamNamesList(df_1617, len(df_1617)) #Season 1617
teams_1718 = createTeamNamesList(df_1718, len(df_1718)) #Season 1718
teams_1819 = createTeamNamesList(df_1819, len(df_1819)) #Season 1819

"""
Function to create dictionaries of the teams that played in each season
Iniliaze six stats for each team: goals scored, goals conceded, games played,
actual goal average, rounded goal average, and goal difference
"""
def createSeasonTeamsDict(team_list):
	season_dict = {}
	for i in range(20):
		season_dict[team_list[i]] = {
			"goals_scored" : 0,
			"goals_conceded" : 0,
			"games_played" : 0,
			"goal_average_actual" : 0,
			"goal_average_rounded" : 0,
			"goal_difference": 0
		}

	return season_dict

"""
Step 3
Declare dictionaries to store nested dictionaries (1 for each team that played in the season)
Call createSeasonTeamsDict function to create the nested dictionaries
"""
season_0910 = createSeasonTeamsDict(teams_0910)
season_1011 = createSeasonTeamsDict(teams_1011)
season_1112 = createSeasonTeamsDict(teams_1112)
season_1213 = createSeasonTeamsDict(teams_1213)
season_1314 = createSeasonTeamsDict(teams_1314)
season_1415 = createSeasonTeamsDict(teams_1415)
season_1516 = createSeasonTeamsDict(teams_1516)
season_1617 = createSeasonTeamsDict(teams_1617)
season_1718 = createSeasonTeamsDict(teams_1718)
season_1819 = createSeasonTeamsDict(teams_1819)


"""
Function to traverse the passed dataframe
Traverse the dataframe row by row, gathering data on the home team, away team, home_goals and away_goals
"""
def readSeasonDataFrame(df, df_length, season_dict):
	for i in range(df_length):
		home_team = df.iat[i,1] #Get the name of the home team
		away_team = df.iat[i,2] #Get the name of the away team
		home_goals = df.iat[i,3] #Get the home team's # of goals scored, away team's # of goals conceded
		away_goals = df.iat[i,4] #Get the away team's # of goals, home team's # of goals conceded

		#Update home team's stats
		season_dict[home_team]["goals_scored"] += home_goals
		season_dict[home_team]["goals_conceded"] += away_goals
		season_dict[home_team]["games_played"] += 1

		#Update away team's stats
		season_dict[away_team]["goals_scored"] += away_goals
		season_dict[away_team]["goals_conceded"] += home_goals
		season_dict[away_team]["games_played"] += 1

	# Calculate each team's average goals per game (rounded) and actual
	# Calculate each team's goal difference 
	for key in season_dict.keys():
		season_dict[key]["goal_average_rounded"] = round((season_dict[key]["goals_scored"] / season_dict[key]["games_played"]), 2)
		season_dict[key]["goal_average_actual"] = season_dict[key]["goals_scored"] / season_dict[key]["games_played"]
		season_dict[key]["goal_difference"] = season_dict[key]["goals_scored"] - season_dict[key]["goals_conceded"]

	return season_dict

# Function to print the the stats of the teams that played in the season
def displaySeasonStats(season, season_dict):
	print("")
	print("-"*130)
	print("|" ," "*54, season, " " *54, "|")
	print("-"*130)
	print("| TEAM", " " * 10, "| GOALS SCORED | GOALS CONCEDED | GAMES PLAYED |", " " * 11, "AVG. GOALS PER GAME", " " * 11, "| GOAL DIFFERENCE |")
	print("|", " " * 15, "| G.S. ", " " * 6, "| G.C ", " " * 9, "| G.P ", " " * 7, "|", " " * 13, " AVG = G.S/G.P ", " " * 13, "| GD = G.S - G.C  |" )
	print("-"*130)
	for key in season_dict.keys():
		goals_scored = season_dict[key]["goals_scored"]
		goals_conceded = season_dict[key]["goals_conceded"]
		games_played = season_dict[key]["games_played"]
		goal_average_actual = season_dict[key]["goal_average_actual"]
		goal_average_rounded = season_dict[key]["goal_average_rounded"]
		goal_difference = season_dict[key]["goal_difference"]
		goal_difference_str = ""

		if goal_difference >= 0:
			goal_difference_str = "+" + str(goal_difference)
		else:
			goal_difference_str = str(goal_difference)
		print('| {0:15s} | {1:12d} |  {2:13d} | {3:12d} | Rounded: {4:.2f} - Actual: {5:.16f}  | {6:15s} |'.format(key, goals_scored, goals_conceded, games_played, goal_average_rounded, goal_average_actual, goal_difference_str))
		print("-"*130)


"""
Step 4
Fill each season dictionary with each team's 
Call the readSeasonDataFrame function to fill the dictionary with the appropriate data
(Optional, display a formatted table showing the data of each team in a particular season.
Add a fourth argument of True (Boolean) to the displaySeasonStats function call)
"""

# EPL Season 09-10
season_0910 = readSeasonDataFrame(df_0910, len(df_0910), season_0910) # Fill EPL Season 09-10 With Data of Each Team
# displaySeasonStats("EPL Season 09-10", season_0910) # Print the Data of the Teams that played in EPL Season 09-10
# EPL Season 10-11
season_1011 = readSeasonDataFrame(df_1011, len(df_1011), season_1011) # Fill EPL Season 10-11 With Data of Each Team
# displaySeasonStats("EPL Season 10-11", season_1011) # Print the Data of the Teams that played in EPL Season 10-11
# EPL Season 11-12
season_1112 = readSeasonDataFrame(df_1112, len(df_1112), season_1112) # Fill EPL Season 11-12 With Data of Each Team
# displaySeasonStats("EPL Season 11-12", season_1112) # Print the Data of the Teams that played in EPL Season 11-12
# EPL Season 12-13
season_1213 = readSeasonDataFrame(df_1213, len(df_1213), season_1213) # Fill EPL Season 12-13 With Data of Each Team
# displaySeasonStats("EPL Season 12-13", season_1213) # Print the Data of the Teams that played in EPL Season 12-13
# EPL Season 13-14
season_1314 = readSeasonDataFrame(df_1314, len(df_1314), season_1314) # Fill EPL Season 13-14 With Data of Each Team
# displaySeasonStats("EPL Season 13-14", season_1314) # Print the Data of the Teams that played in EPL Season 13-14
# EPL Season 14-15
season_1415 = readSeasonDataFrame(df_1415, len(df_1415), season_1415) # Fill EPL Season 14-15 With Data of Each Team
# displaySeasonStats("EPL Season 14-15", season_1415) # Print the Data of the Teams that played in EPL Season 14-15
# EPL Season 15-16
season_1516 = readSeasonDataFrame(df_1516, len(df_1516), season_1516) # Fill EPL Season 15-16 With Data of Each Team
# displaySeasonStats("EPL Season 15-16", season_1516) # Print the Data of the Teams that played in EPL Season 15-16
# EPL Season 16-17
season_1617 = readSeasonDataFrame(df_1617, len(df_1617), season_1617) # Fill EPL Season 16-17 With Data of Each Team
# displaySeasonStats("EPL Season 16-17", season_1617) # Print the Data of the Teams that played in EPL Season 16-17
# EPL Season 17-18
season_1718 = readSeasonDataFrame(df_1718, len(df_1718), season_1718) # Fill EPL Season 17-18 With Data of Each Team
# displaySeasonStats("EPL Season 17-18", season_1718) # Print the Data of the Teams that played in EPL Season 17-18
# EPL Season 18-19
season_1819 = readSeasonDataFrame(df_1819, len(df_1819), season_1819) # Fill EPL Season 18-19 With Data of Each Team
# displaySeasonStats("EPL Season 18-19", season_1819) # Print the Data of the Teams that played in EPL Season 18-19

# Function to sort the team's by avg. goals per game (descending order)
def sortByAvgGoalsPerGame(season_dict):
	# Create a deep copy of the season_dict
	copy_dict = copy.deepcopy(season_dict)

	# First, sort teams by avg. goals per game
	# Second, sort teams that have the same avg. goals per game by goal difference
	sorted_dict = dict(sorted(copy_dict.items(), key=lambda k: (k[1]["goal_average_actual"], k[1]["goal_difference"]), reverse=True))

	return sorted_dict

"""
Step 5
Declare dictionaries to store the sorted dictionaries of each season's team's stats
Call sortByAvgGoalsPerGame function to sort the team's by avg. goals per game
If two or more teams have the same stat for avg. goals per game, sort those teams by their goal difference
(Optional, display a formatted table showing the sorted team leaderboard.
Add a fourth argument of True (Boolean) to the displaySeasonStats function call)
"""
season_0910_sorted = sortByAvgGoalsPerGame(season_0910) # Sort EPL Season 09-10 Teams by avg. goal per game and goal difference
# displaySeasonStats("EPL Season 09-10", season_0910_sorted) # Print the Sorted EPL Season 09-10 Dictionary
season_1011_sorted = sortByAvgGoalsPerGame(season_1011) # Sort EPL Season 10-11 Teams by avg. goal per game and goal difference
# displaySeasonStats("EPL Season 10-11", season_1011_sorted) # Print the Sorted EPL Season 10-11 Dictionary
season_1112_sorted = sortByAvgGoalsPerGame(season_1112) # Sort EPL Season 11-12 Teams by avg. goal per game and goal difference
# displaySeasonStats("EPL Season 11-12", season_1112_sorted) # Print the Sorted EPL Season 11-12 Dictionary
season_1213_sorted = sortByAvgGoalsPerGame(season_1213) # Sort EPL Season 12-13 Teams by avg. goal per game and goal difference
# displaySeasonStats("EPL Season 12-13", season_1213_sorted) # Print the Sorted EPL Season 12-13 Dictionary
season_1314_sorted = sortByAvgGoalsPerGame(season_1314) # Sort EPL Season 13-14 Teams by avg. goal per game and goal difference
# displaySeasonStats("EPL Season 13-14", season_1314_sorted) # Print the Sorted EPL Season 13-14 Dictionary
season_1415_sorted = sortByAvgGoalsPerGame(season_1415) # Sort EPL Season 14-15 Teams by avg. goal per game and goal difference
# displaySeasonStats("EPL Season 14-15", season_1415_sorted) # Print the Sorted EPL Season 14-15 Dictionary
season_1516_sorted = sortByAvgGoalsPerGame(season_1516) # Sort EPL Season 15-16 Teams by avg. goal per game and goal difference
# displaySeasonStats("EPL Season 15-16", season_1516_sorted) # Print the Sorted EPL Season 15-16 Dictionary
season_1617_sorted = sortByAvgGoalsPerGame(season_1617) # Sort EPL Season 16-17 Teams by avg. goal per game and goal difference
# displaySeasonStats("EPL Season 16-17", season_1617_sorted) # Print the Sorted EPL Season 16-17 Dictionary
season_1718_sorted = sortByAvgGoalsPerGame(season_1718) # Sort EPL Season 17-18 Teams by avg. goal per game and goal difference
# displaySeasonStats("EPL Season 17-18", season_1718_sorted) # Print the Sorted EPL Season 17-18 Dictionary
season_1819_sorted = sortByAvgGoalsPerGame(season_1819) # Sort EPL Season 18-19 Teams by avg. goal per game and goal difference
# displaySeasonStats("EPL Season 18-19", season_1819_sorted) # Print the Sorted EPL Season 18-19 Dictionary




# Function to read the data in the E.O.S Leaderboard text files for Seasons 09-10 to 18-19
# and create dictionaries of the leaderboards
def createEOSSeasonDict(filename):
	eos_season_leaderboard = {}
	inFile = open(filename)
	for line in inFile:
		ranking, team = line.strip().split(" ")
		eos_season_leaderboard[ranking] = team

	#Remove '-' character from team name
	for key in eos_season_leaderboard.keys():
		team = eos_season_leaderboard[key]
		if "-" in team:
			eos_season_leaderboard[key] = team.replace("-", " ")

	return eos_season_leaderboard


# Function to compare each season's league winner to each season's
# team with the highest avg. goals per game
# Return the percent difference of the comparison between tables
def displayComparison(season_title, eos_season_dict, sorted_season_dict, display=False):
	count_same_ranking = 0
	count_different_ranking = 0

	# Get the keys of the passed season's dictionary
	# The order of the keys is also the ranking of the teams after sorted by 
	# Avg. goals per game and goal difference
	sorted_season_key_list = list(sorted_season_dict.keys())
	eos_season_key_list = list(eos_season_dict.keys())

	# COMPARISON TABLE HEADER
	if display:
		print("")
		print("-" * 57)
		print("|", " "*16, season_title, " "*19, "|")
		print("| COMPARISON OF EOS LEADERBOARD AND SORTED LEADERBOARD  |")
		print("-" * 57)
		print("| PLACE | EOS LEADERBOARD | SORTED LEADERBOARD | RESULT |")
		print("-" * 57)
	else:
		print(season_title)

	for i in range(20):
		eos_ranking = eos_season_dict[eos_season_key_list[i]]
		sorted_season_ranking = sorted_season_key_list[i]
		result = ""

		if eos_ranking == sorted_season_ranking:
			result = "SAME"
			count_same_ranking += 1
		else: 
			result = "DIFF"
			count_different_ranking += 1

		if display:
			#COMPARISON TABLE ROW
			print('| {0:5d} | {1:15s} | {2:18s} | {3:6s} |'.format(i+1, eos_ranking, sorted_season_ranking, result))
			print("-" * 57)

	difference_in_tables = (count_same_ranking / 20) * 100

	
	print("After comparing the E.O.S. Leaderboard and the Sorted Season Leaderboards")
	print("Only ", '{0:.2f}%'.format(difference_in_tables), " of teams had the same positioning on both leaderboards.")
	print("")

	return difference_in_tables

# Step 5 - Compare Actual Ranking of Teams in E.O.S Leaderboard 
# VS The Ranking of Teams at E.O.S Leaderboard (Sorted by Avg. GPG + G.D.)
# And save the percent difference of the comparison between tables
# EPL Season 09-10 

eos_season0910_leaderboard = createEOSSeasonDict("eos_season0910_leaderboard.txt")
eos_season0910_comparison = displayComparison("EPL SEASON 09-10", eos_season0910_leaderboard, season_0910_sorted)

# EPL Season 10-11
eos_season1011_leaderboard = createEOSSeasonDict("eos_season1011_leaderboard.txt")
eos_season1011_comparison = displayComparison("EPL SEASON 10-11", eos_season1011_leaderboard, season_1011_sorted)
# EPL Season 11-12
eos_season1112_leaderboard = createEOSSeasonDict("eos_season1112_leaderboard.txt")
eos_season1112_comparison = displayComparison("EPL SEASON 11-12", eos_season1112_leaderboard, season_1112_sorted)
# EPL Season 12-13
eos_season1213_leaderboard = createEOSSeasonDict("eos_season1213_leaderboard.txt")
eos_season1213_comparison = displayComparison("EPL SEASON 12-13", eos_season1213_leaderboard, season_1213_sorted)
# EPL Season 13-14
eos_season1314_leaderboard = createEOSSeasonDict("eos_season1314_leaderboard.txt")
eos_season1314_comparison = displayComparison("EPL SEASON 13-14", eos_season1314_leaderboard, season_1314_sorted)
# EPL Season 14-15
eos_season1415_leaderboard = createEOSSeasonDict("eos_season1415_leaderboard.txt")
eos_season1415_comparison = displayComparison("EPL SEASON 14-15", eos_season1415_leaderboard, season_1415_sorted)
# EPL Season 15-16
eos_season1516_leaderboard = createEOSSeasonDict("eos_season1516_leaderboard.txt")
eos_season1516_comparison = displayComparison("EPL SEASON 15-16", eos_season1516_leaderboard, season_1516_sorted)
# EPL Season 16-17
eos_season1617_leaderboard = createEOSSeasonDict("eos_season1617_leaderboard.txt")
eos_season1617_comparison = displayComparison("EPL SEASON 16-17", eos_season1617_leaderboard, season_1617_sorted)
# EPL Season 17-18
eos_season1718_leaderboard = createEOSSeasonDict("eos_season1718_leaderboard.txt")
eos_season1718_comparison = displayComparison("EPL SEASON 17-18", eos_season1718_leaderboard, season_1718_sorted)
# EPL Season 18-19
eos_season1819_leaderboard = createEOSSeasonDict("eos_season1819_leaderboard.txt")
eos_season1819_comparison = displayComparison("EPL SEASON 18-19", eos_season1819_leaderboard, season_1819_sorted)


# STEP 6 - FIND THE MEAN PERCENT DIFFERENCE
# List of all the percent differences
seasons_percent_difference = [
	eos_season0910_comparison,
	eos_season1011_comparison,
	eos_season1112_comparison,
	eos_season1213_comparison,
	eos_season1314_comparison,
	eos_season1415_comparison,
	eos_season1516_comparison,
	eos_season1617_comparison,
	eos_season1718_comparison,
	eos_season1819_comparison
]

sum_of_percents = 0
for i in range(len(seasons_percent_difference)):
	sum_of_percents += seasons_percent_difference[i]

mean_percent_difference = sum_of_percents / 10

print("FINAL RESULT")
print("After comparing the E.O.S Leaderboard and Sorted Season Leaderboard from Seasons")
print("09-10, 10-11, 11-12, 12-13, 13-14, 14-15, 15-16, 16-17, 17-18, and 18-19")
print("The mean percent difference is tables was ", '{0:.2f}%'.format(mean_percent_difference))

