SELECT "currentClub",
AVG(age) as "avgAge",
AVG("numOfAppsClub") as "avgNumOfAppsClub",
COUNT(*) as "numOfPlayers"
FROM public."playerInfo"
GROUP BY "currentClub"