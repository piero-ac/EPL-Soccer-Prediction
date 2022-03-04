# Project #1 
# EPL Seasons 09-10 to 18-1
# Hypothesis: A team's ranking in the season's leaderboard is determined by their ranking in a table of avg. goals per game
# Average Goals Per Game- the number of goals scored divided by the number of games played

import pandas as pd
from operator import getitem
import copy

# Step 1 - Get the data of all CSV files
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
	for i in range(df_length):
		team_name = df.iat[i, 1]
		if team_name not in team_list:
			team_list.append(team_name)
	return team_list

# Step 2 - Fill the lists of the the teams that played in each season
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


# Function to create dictionaries for each season of the teams that played
# in that season. In addition, iniliaze three stats for each team: number of goals,
# number of games, and goal average.
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

# Step 3 - Fill the dictionaries of the teams that played in each season
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

# Function to traverse the passed season's dataframe, getting each team's total number
# goals, number of games, and goal average for the season
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
	# Also each team's goal difference 
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

# Function to sort the team's by avg. goals per game (descending order)
def sortByAvgGoalsPerGame(season_dict):
	# Create a deep copy of the season_dict
	copy_dict = copy.deepcopy(season_dict)

	# First, sort teams by avg. goals per game
	# Second, sort teams that have the same avg. goals per game by goal difference
	sorted_dict = dict(sorted(copy_dict.items(), key=lambda k: (k[1]["goal_average_actual"], k[1]["goal_difference"]), reverse=True))

	return sorted_dict


# Step 4 - Fill each season dictionary with each team's number of goals, number of games, and goal average
# and then sort each season dictionary. (Optional) Display Both Unsorted and Sorted Dictionaries

# EPL Season 09-10
season_0910 = readSeasonDataFrame(df_0910, len(df_0910), season_0910) # Fill EPL Season 09-10 With Data of Each Team
# displaySeasonStats("EPL Season 09-10", season_0910) # Print the Data of the Teams that played in EPL Season 09-10
season_0910_sorted = sortByAvgGoalsPerGame(season_0910) # Sort EPL Season 09-10 Teams by avg. goal per game and goal difference
# displaySeasonStats("EPL Season 09-10", season_0910_sorted) # Print the Sorted EPL Season 09-10 Dictionary

# EPL Season 10-11
season_1011 = readSeasonDataFrame(df_1011, len(df_1011), season_1011) # Fill EPL Season 10-11 With Data of Each Team
# displaySeasonStats("EPL Season 10-11", season_1011) # Print the Data of the Teams that played in EPL Season 10-11
season_1011_sorted = sortByAvgGoalsPerGame(season_1011) # Sort EPL Season 10-11 Teams by avg. goal per game and goal difference
# displaySeasonStats("EPL Season 10-11", season_1011_sorted) # Print the Sorted EPL Season 10-11 Dictionary

# EPL Season 11-12
season_1112 = readSeasonDataFrame(df_1112, len(df_1112), season_1112) # Fill EPL Season 11-12 With Data of Each Team
# displaySeasonStats("EPL Season 11-12", season_1112) # Print the Data of the Teams that played in EPL Season 11-12
season_1112_sorted = sortByAvgGoalsPerGame(season_1112) # Sort EPL Season 11-12 Teams by avg. goal per game and goal difference
# displaySeasonStats("EPL Season 11-12", season_1112_sorted) # Print the Sorted EPL Season 11-12 Dictionary

# EPL Season 12-13
season_1213 = readSeasonDataFrame(df_1213, len(df_1213), season_1213) # Fill EPL Season 12-13 With Data of Each Team
# displaySeasonStats("EPL Season 12-13", season_1213) # Print the Data of the Teams that played in EPL Season 12-13
season_1213_sorted = sortByAvgGoalsPerGame(season_1213) # Sort EPL Season 12-13 Teams by avg. goal per game and goal difference
# displaySeasonStats("EPL Season 12-13", season_1213_sorted) # Print the Sorted EPL Season 12-13 Dictionary

# EPL Season 13-14
season_1314 = readSeasonDataFrame(df_1314, len(df_1314), season_1314) # Fill EPL Season 13-14 With Data of Each Team
# displaySeasonStats("EPL Season 13-14", season_1314) # Print the Data of the Teams that played in EPL Season 13-14
season_1314_sorted = sortByAvgGoalsPerGame(season_1314) # Sort EPL Season 13-14 Teams by avg. goal per game and goal difference
# displaySeasonStats("EPL Season 13-14", season_1314_sorted) # Print the Sorted EPL Season 13-14 Dictionary

# EPL Season 14-15
season_1415 = readSeasonDataFrame(df_1415, len(df_1415), season_1415) # Fill EPL Season 14-15 With Data of Each Team
# displaySeasonStats("EPL Season 14-15", season_1415) # Print the Data of the Teams that played in EPL Season 14-15
season_1415_sorted = sortByAvgGoalsPerGame(season_1415) # Sort EPL Season 14-15 Teams by avg. goal per game and goal difference
# displaySeasonStats("EPL Season 14-15", season_1415_sorted) # Print the Sorted EPL Season 14-15 Dictionary

# EPL Season 15-16
season_1516 = readSeasonDataFrame(df_1516, len(df_1516), season_1516) # Fill EPL Season 15-16 With Data of Each Team
# displaySeasonStats("EPL Season 15-16", season_1516) # Print the Data of the Teams that played in EPL Season 15-16
season_1516_sorted = sortByAvgGoalsPerGame(season_1516) # Sort EPL Season 15-16 Teams by avg. goal per game and goal difference
# displaySeasonStats("EPL Season 15-16", season_1516_sorted) # Print the Sorted EPL Season 15-16 Dictionary

# EPL Season 16-17
season_1617 = readSeasonDataFrame(df_1617, len(df_1617), season_1617) # Fill EPL Season 16-17 With Data of Each Team
# displaySeasonStats("EPL Season 16-17", season_1617) # Print the Data of the Teams that played in EPL Season 16-17
season_1617_sorted = sortByAvgGoalsPerGame(season_1617) # Sort EPL Season 16-17 Teams by avg. goal per game and goal difference
# displaySeasonStats("EPL Season 16-17", season_1617_sorted) # Print the Sorted EPL Season 16-17 Dictionary

# EPL Season 17-18
season_1718 = readSeasonDataFrame(df_1718, len(df_1718), season_1718) # Fill EPL Season 17-18 With Data of Each Team
# displaySeasonStats("EPL Season 17-18", season_1718) # Print the Data of the Teams that played in EPL Season 17-18
season_1718_sorted = sortByAvgGoalsPerGame(season_1718) # Sort EPL Season 17-18 Teams by avg. goal per game and goal difference
# displaySeasonStats("EPL Season 17-18", season_1718_sorted) # Print the Sorted EPL Season 17-18 Dictionary

# EPL Season 18-19
season_1819 = readSeasonDataFrame(df_1819, len(df_1819), season_1819) # Fill EPL Season 18-19 With Data of Each Team
# displaySeasonStats("EPL Season 18-19", season_1819) # Print the Data of the Teams that played in EPL Season 18-19
season_1819_sorted = sortByAvgGoalsPerGame(season_1819) # Sort EPL Season 18-19 Teams by avg. goal per game and goal difference
# displaySeasonStats("EPL Season 18-19", season_1819_sorted) # Print the Sorted EPL Season 18-19 Dictionary

# Function to find team with the highest avg. goals per game in the season
# def findHighestGoalAverage(season, season_dict):
# 	highest_team = ""
# 	highest_goal_avg_actual = 0
# 	highest_goal_avg_rounded = 0
# 	for key in season_dict.keys():
# 		if season_dict[key]["goal_average_actual"] > highest_goal_avg_actual:
# 			#Save the current highest avg. goals per game (actual)
# 			highest_goal_avg_actual = season_dict[key]["goal_average_actual"]
# 			#Save the current highest avg. goals per game (rounded) 
# 			highest_goal_avg_rounded = season_dict[key]["goal_average_rounded"] 
# 			#Save the team with the current highest avg. goals per game
# 			highest_team = key

# 	#Return a list with the each season's team with the highest avg. goals per game
# 	return [season, highest_team, highest_goal_avg_actual, highest_goal_avg_rounded]

# # Function to display information of each season's team with the highest avg. goals per game
# def displaySeasonsTop(seasons_top):
# 	print("")
# 	print("-"*56)
# 	print("| Each EPL Season's Team with the Highest Goal Average |")
# 	print("-"*56)
# 	print("| EPL SEASON | TEAM", " " * 10, "| AVG. GOALS PER GAME ", " |")
# 	print("-"*56)
# 	for i in range(len(seasons_top)):
# 		season = seasons_top[i][0]
# 		team = seasons_top[i][1]
# 		highest_goal_avg_rounded = seasons_top[i][3]
# 		print("|", season, " " * 4 , '| {0:15s} | {1:.2f}'.format(team, highest_goal_avg_rounded), " " * 16, "|")
# 		print("-"*56)

# # Step 5 - Create a List of Each Season's Team with the highest avg. goals per game
# seasons_top = []
# seasons_top.append(findHighestGoalAverage("09-10", season_0910))
# seasons_top.append(findHighestGoalAverage("10-11", season_1011))
# seasons_top.append(findHighestGoalAverage("11-12", season_1112))
# seasons_top.append(findHighestGoalAverage("12-13", season_1213))
# seasons_top.append(findHighestGoalAverage("13-14", season_1314))
# seasons_top.append(findHighestGoalAverage("14-15", season_1415))
# seasons_top.append(findHighestGoalAverage("15-16", season_1516))
# seasons_top.append(findHighestGoalAverage("16-17", season_1617))
# seasons_top.append(findHighestGoalAverage("17-18", season_1718))
# seasons_top.append(findHighestGoalAverage("18-19", season_1819))

# # displaySeasonsTop(seasons_top)

# # Function to compare each season's league winner to each season's
# # team with the highest avg. goals per game
# def displayComparison(seasons_top):
# 	season_winners = { 
# 		"09-10" : "Chelsea",
# 		"10-11" : "Man United",
# 		"11-12" : "Man City",
# 		"12-13" : "Man United",
# 		"13-14" : "Man City",
# 		"14-15" : "Chelsea",
# 		"15-16" : "Leicester",
# 		"16-17" : "Chelsea",
# 		"17-18" : "Man City",
# 		"18-19" : "Man City",
# 	}

# 	# Get a list of all seasons_winner keys
# 	key_list = list(season_winners.keys())

# 	winner_and_top_team_count = 0
# 	top_team_only_count = 0

# 	print("")
# 	print("-"*73)
# 	print("| Comparison of League Winner VS Team with Highest Avg. Goals Per Game  |")
# 	print("-"*73)
# 	print("| EPL Season | League Winner   |  Team with Highest Avg. Goals Per Game |")
# 	print("-"*73)
# 	for i in range(len(seasons_top)):
# 		season = key_list[i] # Store the season year
# 		winning_team = season_winners[season] # Season's Winning Team
# 		seasons_team_highest = seasons_top[i][1] # Team with Season's Highest Avg. Goal per Game
# 		seasons_team_highest_goal_avg_rounded = seasons_top[i][2] # Team's Avg. Goal per Game

# 		print("|", season, " " * 6 ,'| {0:14s}| {1:14s}'.format(winning_team, seasons_team_highest), " " * 23, "|")
# 		print("-"*73)

# 		# The winning team of the season also had the highest goal average
# 		if winning_team == seasons_team_highest:
# 			#print('{0:15s} won the {1:16s} and had the highest goal average of the season with {2} goals per game.'.format(winning_team, season, seasons_team_highest_goal_avg_rounded))
# 			winner_and_top_team_count += 1
# 		# The winning team of the season and the team with the highest avg. goal per game were different
# 		else:
# 			#print('{0:15s} won the {1:16s} and {2:15s} had the highest goal average of the season with {3} goals per game.'.format(winning_team, season, seasons_team_highest, seasons_team_highest_goal_avg_rounded))
# 			top_team_only_count += 1

# 	percentage = (winner_and_top_team_count / top_team_only_count) * 100
# 	return str(percentage) + "%"

# results = displayComparison(seasons_top)





