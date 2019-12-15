from bs4 import BeautifulSoup
import requests
import csv

source = requests.get("https://www.skysports.com/premier-league-results").text
soup = BeautifulSoup(source, 'lxml')

excel_sheet = open("games_results.csv","w")
writer = csv.writer(excel_sheet)
writer.writerow(["Team 1", "Score", "Team 2"])

scores = soup.find_all("span",class_ = "matches__teamscores-side")
teams = soup.find_all("span", class_ = "swap-text--bp30")

for game in range(0,20,2):
        score1 = scores[game].text.replace("\n","").replace("\r", "")
        score2 = scores[game+1].text.replace("\n","").replace("\r", "")
        team1 = teams[game].text.replace("\n","").replace("\r", "")
        team2 = teams[game+1].text.replace("\n","").replace("\r", "")
        writer.writerow([team1, score1 + " - " + score2, team2])

excel_sheet.close()

