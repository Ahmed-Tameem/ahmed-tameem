"""
#Author: Ahmed Tameem
#Date: December 2, 2019
#Comments: This was my first experiment with webscarping. After this, I started learning how to use APIs to scrape data.
"""

import csv
import requests
from bs4 import BeautifulSoup

source = requests.get("https://www.skysports.com/premier-league-results").text  #Storing the webpage in text form.
soup = BeautifulSoup(source, 'lxml')    #Parsing the website.

excel_sheet = open("games_results.csv","w")     #Opening an excel sheet in write mode to store the scraped results in later.
writer = csv.writer(excel_sheet)
writer.writerow(["Team 1", "Score", "Team 2"])  #Writing the column titles to the excel sheet.

scores = soup.find_all("span",class_ = "matches__teamscores-side")      #Finding and storing the scores of the teams.
teams = soup.find_all("span", class_ = "swap-text--bp30")       #Finding and storing the team names.

for game in range(0,20,2):      #Writing the match results to the excel sheet after removing new line characters.
    score1 = scores[game].text.replace("\n","").replace("\r", "")
    score2 = scores[game+1].text.replace("\n","").replace("\r", "")
    team1 = teams[game].text.replace("\n","").replace("\r", "")
    team2 = teams[game+1].text.replace("\n","").replace("\r", "")
    writer.writerow([team1, score1 + " - " + score2, team2])

excel_sheet.close()
    