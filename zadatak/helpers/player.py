import uuid

class Player():
    def __init__(self, playerUrl):
        self.playerId = uuid.uuid4()
        self.playerUrl = playerUrl
        self.name = ''
        self.fullName = ''
        self.dateOfBirth = ''
        self.age = ''
        self.placeOfBirth = ''
        self.countryOfBirth = ''
        self.position = ''
        self.currentClub = ''
        self.nationalTeam = ''
        self.numOfAppsClub = ''
        self.numOfGoalsClub = ''
        self.numOfAppsNational = ''
        self.numOfGoalsNational = ''

    def __str__(self):
        return f"{self.playerId}, {self.playerUrl}, {self.name}, {self.fullName}, {self.dateOfBirth}, {self.age}, {self.placeOfBirth}, {self.countryOfBirth}, {self.position}, {self.currentClub}, {self.nationalTeam}, {self.numOfAppsClub}, {self.numOfGoalsClub}"
