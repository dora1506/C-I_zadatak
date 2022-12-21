# Web scraper

Prvi dio zadatka je web scraping kojim se uzimaju podaci o nogometašima sa stranica Wikipedije i upisuju u .csv dokument. Za web scraping koristila sam okvir [Scrapy](https://scrapy.org/). Također sam koristila distribucijsku platformu [Anaconda](https://www.anaconda.com/products/distribution) pomoću koje sam sve mogla instalirati i pokrenuti.

Glavni dio koda za web scraping nalazi se u `players_spider.py` koji se može pronaći u dokumentu `spiders`. Osim toga napravila sam i klasu `player.py` koja mi je pomogla prilikom spremanja podataka.

## Pokretanje
Sve sam pokretala naredbom:

scrapy crawl players -o playersScraped.csv -t csv

koja je pokretala program i po čijem završetku bi bio kreiran direktorij `playersScraped.csv` u kojem su se nalazile sve potrebne informacije o nogometašima. Taj sam direktorij (točno tog imena) kasnije koristila prilikom unosa podataka u bazu podataka.