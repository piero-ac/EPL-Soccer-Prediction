# Project #1 
# EPL Seasons 09-10 to 18-19
# Goal Average - the number of goals scored divided by the number of goals conceded

import pandas as pd

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


# Function to create dictionaries of the teams that played in each season. 
# In addition, iniliaze four stats for each team: 
# goals conceded, goals scored, number of games, and goal average.
def createSeasonTeamsDict(team_list):
	season_dict = {}
	for i in range(20):
		season_dict[team_list[i]] = {"goals_conceded":0, "goals_scored":0, "number_of_games":0, "goal_average": 0}
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

# Function to traverse the passed season's dataframe
# Get each season's match stats for home team and away team
def readSeasonDataFrame(df, df_length, season_dict):

	for i in range(df_length):
		home_team = df.iat[i,1] #Get the name of the home team
		away_team = df.iat[i,2] #Get the name of the away team
		home_goals = df.iat[i,3] #home team's # of goals scored, away team's # of goals conceded
		away_goals = df.iat[i,4] #away team's # of goals scored, home team's # of goals conceded

		#Update home team's stats
		season_dict[home_team]["goals_conceded"] += away_goals
		season_dict[home_team]["goals_scored"] += home_goals
		season_dict[home_team]["number_of_games"] += 1
		season_dict[home_team]["goal_average"] = season_dict[home_team]["goals_scored"] / season_dict[home_team]["goals_conceded"]

		#Update away team's stats
		season_dict[away_team]["goals_conceded"] += home_goals
		season_dict[away_team]["goals_scored"] += away_goals
		season_dict[away_team]["number_of_games"] += 1

	#Calculate each team's goal average
	for key in season_dict.keys():
		season_dict[key]["goal_average"] = season_dict[key]["goals_scored"] / season_dict[key]["goals_conceded"]


# Function to print the number of goals, number of games, and goal average
# of each team in the season
def displaySeasonTeamStats(season, season_dict):
	print("")
	print("-"*110)
	print(" "*45, season)
	print("-"*110)
	for key in season_dict.keys():
		goals_scored = season_dict[key]["goals_scored"]
		goals_conceded = season_dict[key]["goals_conceded"]
		number_of_games = season_dict[key]['number_of_games']
		goal_average = season_dict[key]["goal_average"]
		print('Team: {0:15s} | Goals Scored: {1:5d} | Goals Conceded: {2:5d} | Games Played: {3:5d} | Goal Average: {4}'.format(key, goals_scored, goals_conceded, number_of_games, goal_average))
		print("-"*110)

# Step 4 - Fill the season dict with the each team's number of goals
# number of games, and goal average
readSeasonDataFrame(df_0910, len(df_0910), season_0910) # Season 09-10
displaySeasonTeamStats("EPL Season 09-10", season_0910)
readSeasonDataFrame(df_1011, len(df_1011), season_1011) # Season 10-11
displaySeasonTeamStats("EPL Season 10-11", season_1011) 
readSeasonDataFrame(df_1112, len(df_1112), season_1112) # Season 11-12
displaySeasonTeamStats("EPL Season 11-12", season_1112)
readSeasonDataFrame(df_1213, len(df_1213), season_1213) # Season 12-13
displaySeasonTeamStats("EPL Season 12-13", season_1213)
readSeasonDataFrame(df_1314, len(df_1314), season_1314) # Season 13-14
displaySeasonTeamStats("EPL Season 13-14", season_1314)
readSeasonDataFrame(df_1415, len(df_1415), season_1415) # Season 14-15
displaySeasonTeamStats("EPL Season 14-15", season_1415)
readSeasonDataFrame(df_1516, len(df_1516), season_1516) # Season 15-16
displaySeasonTeamStats("EPL Season 15-16", season_1516)
readSeasonDataFrame(df_1617, len(df_1617), season_1617) # Season 16-17
displaySeasonTeamStats("EPL Season 16-17", season_1617)
readSeasonDataFrame(df_1718, len(df_1718), season_1718) # Season 17-18
displaySeasonTeamStats("EPL Season 17-18", season_1718)
readSeasonDataFrame(df_1819, len(df_1819), season_1819) # Season 18-19
displaySeasonTeamStats("EPL Season 18-19", season_1819)

# Function to find team with the highest goal average in the season
# def findHighestGoalAverage(season, season_dict):
# 	highest_team = ""
# 	highest_goal_avg = 0
# 	for team in season_dict.keys():
# 		if season_dict[team]['goal_average'] > highest_goal_avg:
# 			highest_goal_avg = season_dict[team]['goal_average'] #Save the current highest goal average
# 			highest_team = team #Save the team with the current highest goal average
# 	return [season, highest_team, highest_goal_avg]

# Step 6 - Create a List of Each Season's Team that had the highest goal average
# seasons_top = []
# seasons_top.append(findHighestGoalAverage("EPL Season 09-10", season_0910))
# seasons_top.append(findHighestGoalAverage("EPL Season 10-11", season_1011))
# seasons_top.append(findHighestGoalAverage("EPL Season 11-12", season_1112))
# seasons_top.append(findHighestGoalAverage("EPL Season 12-13", season_1213))
# seasons_top.append(findHighestGoalAverage("EPL Season 13-14", season_1314))
# seasons_top.append(findHighestGoalAverage("EPL Season 14-15", season_1415))
# seasons_top.append(findHighestGoalAverage("EPL Season 15-16", season_1516))
# seasons_top.append(findHighestGoalAverage("EPL Season 16-17", season_1617))
# seasons_top.append(findHighestGoalAverage("EPL Season 17-18", season_1718))
# seasons_top.append(findHighestGoalAverage("EPL Season 18-19", season_1819))


# Function to display information of each season's team with the highest goal average
# def displaySeasonsTop(seasons_top):
# 	print("-"*55)
# 	print(" Each EPL Season's Team with the Highest Goal Average")
# 	print("-"*55)
# 	for i in range(len(seasons_top)):
# 		print(seasons_top[i][0], '| {0:15s} | {1}'.format(seasons_top[i][1], seasons_top[i][2]))
# 		print("-"*55)

# displaySeasonsTop(seasons_top)

# Function to compare each season's league winner to each season's team with the highest goal average

# def comparison(seasons_top):
# 	season_winners = { 
# 		"EPL Season 09-10" : "Chelsea",
# 		"EPL Season 10-11" : "Man United",
# 		"EPL Season 11-12" : "Man City",
# 		"EPL Season 12-13" : "Man United",
# 		"EPL Season 13-14" : "Man City",
# 		"EPL Season 14-15" : "Chelsea",
# 		"EPL Season 15-16" : "Leicester",
# 		"EPL Season 16-17" : "Chelsea",
# 		"EPL Season 17-18" : "Man City",
# 		"EPL Season 18-19" : "Man City",
# 	}

# 	key_list = list(season_winners.keys())
# 	for i in range(len(seasons_top)):
# 		season = key_list[i] # Store the season
# 		winning_team = season_winners[season] # Season's Winning Team
# 		seasons_team_highest = seasons_top[i][1] # Team with Season's Highest Goal Average
# 		seasons_team_highest_goalavg = seasons_top[i][2] # Team's Goal Average

# 		# The winning team of the season also had the highest goal average
# 		if winning_team == seasons_team_highest:
# 			print('{0:15s} won the {1:16s} and had the highest goal average of the season with {2} goals per game.'.format(winning_team, season, seasons_team_highest_goalavg))
# 		# The winning team of the season and the team with the highest goal average were different
# 		else:
# 			print('{0:15s} won the {1:16s} and {2:15s} had the highest goal average of the season with {3} goals per game.'.format(winning_team, season, seasons_team_highest, seasons_team_highest_goalavg))


# comparison(seasons_top)




