#!/usr/bin/python
import datetime
import psycopg2
# from config import config
import csv
import player

def connect():
    conn = None
    try:
        conn = psycopg2.connect(
            database = "players",
            user = "postgres",
            password = "postgresql123",
            host = "localhost",
            port = "5433"
        )

        conn.autocommit = True
        cur = conn.cursor()

        cur.execute("""
            CREATE TABLE IF NOT EXISTS public."playerInfo"
(
    "playerId" text COLLATE pg_catalog."default" NOT NULL,
    "playerUrl" text COLLATE pg_catalog."default" NOT NULL,
    name text COLLATE pg_catalog."default",
    "fullName" text COLLATE pg_catalog."default",
    "dateOfBirth" date,
    age smallint,
    "paceOfBirth" text COLLATE pg_catalog."default",
    "countryOfBirth" text COLLATE pg_catalog."default",
    "position" text COLLATE pg_catalog."default",
    "currentClub" text COLLATE pg_catalog."default",
    "nationalTeam" text COLLATE pg_catalog."default",
    "numOfAppsClub" smallint,
    "numOfGoalsClub" smallint,
    "numOfAppsNational" smallint,
    "numOfGoalsNational" smallint,
    CONSTRAINT "playerInfo_pkey" PRIMARY KEY ("playerUrl")
)

        """)

        playerList = parsePlayerData("playersData.csv")
        playerList.extend(parsePlayerScraped("playersScraped.csv"))
        
        for plyr in playerList:
            cur = conn.cursor()

            try:
                cur.execute("""
                    INSERT INTO public."playerInfo"
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """, (plyr.playerId, plyr.playerUrl, plyr.name, plyr.fullName, plyr.dateOfBirth, plyr.age, plyr.placeOfBirth, plyr.countryOfBirth, plyr.position, plyr.currentClub, plyr.nationalTeam, plyr.numOfAppsClub, plyr.numOfGoalsClub, plyr.numOfAppsNational, plyr.numOfGoalsNational))
            except:
                cur.execute("""
                    UPDATE public."playerInfo"
	                SET 
                    "playerId"=%s, 
                    name=%s, 
                    "fullName"=%s, 
                    "dateOfBirth"=%s, 
                    age=%s, 
                    "paceOfBirth"=%s, 
                    "countryOfBirth"=%s, 
                    "position"=%s, 
                    "currentClub"=%s, 
                    "nationalTeam"=%s,
                    "numOfAppsClub" = %s,
                    "numOfGoalsClub" =%s,
                    "numOfAppsNational" =%s, 
                    "numOfGoalsNational" =%s 
	                WHERE "playerUrl" = %s;
                """, (plyr.playerId, plyr.name, plyr.fullName, plyr.dateOfBirth, plyr.age, plyr.placeOfBirth, plyr.countryOfBirth, plyr.position, plyr.currentClub, plyr.nationalTeam, plyr.numOfAppsClub, plyr.numOfGoalsClub, plyr.numOfAppsNational, plyr.numOfGoalsNational, plyr.playerUrl)) 
        cur.close()


    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


def parsePlayerData(filename):

    playerList = []

    with open(filename, 'r', encoding="utf-8-sig") as file:
        csvreader = csv.DictReader(file, delimiter=";")
        for row in csvreader:
            plyr = player.Player()
            plyr.playerId = row['PlayerID']
            plyr.playerUrl = row['URL']
            plyr.name = row['Name']
            plyr.fullName = row['Full name']
            try:
                plyr.dateOfBirth = datetime.datetime.strptime(row['Date of birth'], "%d.%m.%Y")
            except:
                plyr.dateOfBirth = None

            try:
                plyr.age = int(row['Age'])
            except:
                plyr.age = None

            plyr.placeOfBirth = row['City of birth']
            plyr.countryOfBirth = row['Country of birth']
            plyr.position = row['Position']
            plyr.currentClub = row['Current club']
            plyr.nationalTeam = row['National_team']

            playerList.append(plyr)

    return playerList


def parsePlayerScraped(filename):

    playerList = []

    with open(filename, 'r', encoding="utf-8-sig") as file:
        csvreader = csv.DictReader(file, delimiter=",")
        for row in csvreader:
            plyr = player.Player()
            plyr.playerId = row['playerId']
            plyr.playerUrl = row['playerUrl']
            plyr.name = row['name']
            plyr.fullName = row['fullName']
            try:
                plyr.dateOfBirth = datetime.datetime.strptime(row['dateOfBirth'], "%d.%m.%Y")
            except:
                plyr.dateOfBirth = None

            try:
                plyr.age = int(row['age'])
            except:
                plyr.age = None

            plyr.placeOfBirth = row['placeOfBirth']
            plyr.countryOfBirth = row['countryOfBirth']
            plyr.position = row['position']
            plyr.currentClub = row['currentClub']
            plyr.nationalTeam = row['nationalTeam']
            try:
                plyr.numOfAppsClub = int(row['numOfAppsClub'])
            except:
                plyr.numOfAppsClub = None
            
            try:
                plyr.numOfGoalsClub = int(row['numOfGoalsClub'])
            except:
                plyr.numOfGoalsClub = None
            
            try:
                plyr.numOfAppsNational = int(row['numOfAppsNational'])
            except:
                plyr.numOfAppsNational = None
            
            try:
                plyr.numOfGoalsNational = int(row['numOfGoalsNational'])
            except:
                plyr.numOfGoalsNational = None

            playerList.append(plyr)

    return playerList


if __name__ == '__main__':
    connect()


