# SQL Database

U drugom dijelu zadatka unosim podatke u bazu podataka `PostgreSQL`. 

Glavni dio koda nalazi se u `connect.py`. Tu se povezujemo na bazu podataka pa prilikom pokretanja treba prilagoditi podatke:

    conn = psycopg2.connect(
            database = "players",
            user = "postgres",
            password = "postgresql123",
            host = "localhost",
            port = "5433"
        )

Osim toga napravila sam klasu `player.py` koja mi je pomogla prilikom unosa podataka iz .csv direktorija u bazu podataka. Imena stupaca u danom .csv direktoriju (`playersData.csv`) i .csv direktoriju dobivenom web scrapingom (`playersScraped.csv`) su različita, no zbog klase mi to nije predstavljalo problem.


## Pokretanje

Prilikom pokretanja bitno je da se u dokumentu `zadatak2` uz `connect.py` nalaze i `playersData.csv` i `playersScraped.csv` iz kojih se podaci učitavaju u bazu. Oni se sada tamo i nalaze, ali u slučaju promjena prilikom web scrapinga treba se dodati novi direktorij istog imena ili se treba promijeniti ime direktorija it kojeg se podaci čitaju što se može napraviti u sljedećim naredbama:

playerList = parsePlayerData("playersData.csv")
playerList.extend(parsePlayerScraped("playersScraped.csv"))



