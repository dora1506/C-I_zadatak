import scrapy
import csv
import time
from zadatak.helpers.player import Player

class PlayersSpider(scrapy.Spider):
    name = "players"


    def lastOne(self, row, rows):
        i = rows.index(row)
        lastRow = rows[i+1]
        lenRows = len(rows)


        while(len(lastRow.xpath("th").extract()) != 0 and
              len(lastRow.xpath("td").extract()) != 0 and
              i < lenRows):
            i += 1
            try:
                lastRow = rows[i]
            except:
                break
        return rows[i-1]
        

    def start_requests(self):
        
        urls = []
        with open("playersURLs.csv", 'r') as file:
            csvreader = csv.reader(file)
            for row in csvreader:
                urls.append(row[0])


        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)            

    def parse(self, response):

        playerUrl = response.url
        player = Player(playerUrl)

        caption = response.xpath('//*[@class="infobox-title fn"]')
        player.name = caption.xpath('text()').extract_first()

        if player.name == None:
            del player
            return


        rows = response.xpath('//*[@class="infobox vcard"]//tbody//tr')
        lenRows = len(rows)


        for row in rows:
            rowCategory = row.xpath('th//text()').extract_first()
            if rowCategory == 'Full name':
                 player.fullName = row.xpath('td//text()').extract_first()[1:]
            if rowCategory == 'Date of birth':
                player.dateOfBirth = row.xpath('td//span[@class="bday"]//text()').extract_first()
                try:
                    player.age = row.xpath('td//span[@class="noprint ForceAgeToShow"]//text()').extract_first()[6:-1]
                except:
                    continue
            if rowCategory == 'Place of birth':
                player.placeOfBirth = row.xpath('td//a//text()').extract_first()
                try:
                    player.countryOfBirth = row.xpath('td//text()')[2].extract()[2:]
                except:
                    player.countryOfBirth = player.placeOfBirth
            if rowCategory == 'Position(s)':
                player.position = row.xpath('td//a//text()').extract_first()
            if rowCategory == 'Current team':
                player.currentClub = row.xpath('td//a//text()').extract_first()
            if rowCategory == 'International career':
                lastRow = self.lastOne(row, rows)
                player.nationalTeam = lastRow.xpath('td//a//text()').extract_first()
                player.numOfAppsNational = lastRow.xpath('td[@class="infobox-data infobox-data-b"]//text()').extract_first()[1:]
                player.numOfGoalsNational = lastRow.xpath('td[@class="infobox-data infobox-data-c"]//text()').extract_first()[2:-1]
            if rowCategory == 'Senior career*':
                lastRow = self.lastOne(row, rows)
                player.numOfAppsClub = lastRow.xpath('td[@class="infobox-data infobox-data-b"]//text()').extract_first()[1:]
                player.numOfGoalsClub = lastRow.xpath('td[@class="infobox-data infobox-data-c"]//text()').extract_first()[2:-1]
        
        timestamp = time.time()

        playerdict = player.__dict__
        playerdict['Timestamp'] = timestamp
        yield playerdict
