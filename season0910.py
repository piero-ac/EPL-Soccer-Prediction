# Test of Data Import using Season 09-10 CSV

#Import Pandas Library
import pandas as pd

#Step 1 - Get The Data
df = pd.read_csv("season_0910.csv", index_col=0)
# df = df.head()
# print(df)

#Step 2 - Filter the 1st column
# df = df[df.columns[1:5]]
# df = df.head()
# print(df) 

teams = []
teams_dic = {}

#Step 3 - Print # of Unique Records in a column
# df = df[df.columns[2]] 
# print(df.nunique())

#Make a list of all the teams that played in that season
for i in range(380):
	team_name = df.iat[i,1] #Traverse the Home Team Column
	if team_name not in teams: #Add the name to the list (if not in list)
		teams.append(team_name)

# print(len(teams)) # prints 20
# print(teams)

#Make a dictionary with all teams and the number of goals
#they scored, beginning at 0
for i in range(len(teams)):
	teams_dic[teams[i]] = {"number_of_goals" : 0, "number_of_games" : 0, "goal_average" : 0}
# print(teams_dic)

#Traverse the csv, adding up the number of goals scored 
#by each team in a match
for i in range(len(df)):
	home_team = df.iat[i,1] #Get the name of the home team
	away_team = df.iat[i,2] #Get the name of the away team
	home_team_goals = df.iat[i,3] #Get the home team's # of goals
	away_team_goals = df.iat[i,4] #Get the away team's # of goals

	teams_dic[home_team]["number_of_goals"] += home_team_goals
	teams_dic[home_team]["number_of_games"] += 1
	teams_dic[away_team]["number_of_goals"] += away_team_goals
	teams_dic[away_team]["number_of_games"] += 1
	teams_dic[home_team]["goal_average"] = teams_dic[home_team]["number_of_goals"] / teams_dic[home_team]["number_of_games"]
	teams_dic[away_team]["goal_average"] = teams_dic[away_team]["number_of_goals"] / teams_dic[away_team]["number_of_games"]

#Output Each Teams Information
for i in teams_dic.keys():
	print(f"Team: {i}")
	print(f"Number of Goals: {teams_dic[i]['number_of_goals']}")
	print(f"Number of Games: {teams_dic[i]['number_of_games']}")
	print(f"Goal Average: {teams_dic[i]['goal_average']}")
	# print("")

#Find the Highest Goal Average
highest_team = ""
highest_goal_avg = 0
for team in teams_dic.keys():
	if teams_dic[team]['goal_average'] > highest_goal_avg:
		highest_goal_avg = teams_dic[team]['goal_average'] #Save the current highest goal average
		highest_team = team #Save the team with the current highest goal average

#
print(f"Team with the highest goal average for the 09-10 Season was {highest_team} with a goal average of {highest_goal_avg}")








