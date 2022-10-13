import re

idRegexStr = r"^(\d{1,2})\-(\d{4,5})$"
idRegex = re.compile(idRegexStr)


class UniversityID:

    def __init__(self, ID: str):

        self.ID = ID

        if not self.isFormatted():
            raise ValueError('Invalid ID')

        self.components = {}
        self.getComponents()

        if not self.isValid():
            raise ValueError('Invalid ID')

        self.getEntranceYear()

    def isFormatted(self) -> bool:
        isMatched = re.match(idRegexStr, self.ID)
        return isMatched

    def getComponents(self):
        match = idRegex.search(self.ID)

        self.components['classID'] = int(match.group(1))
        self.components['studentID'] = match.group(2)

    def isValid(self) -> bool:
        classIDValid: bool = (self.components['classID'] - 1) % 3 == 0
        studentIDValid: bool = self.components['studentID'] != '0000' or '00000'

        return classIDValid and studentIDValid

    def getEntranceYear(self):
        self.components['classYear'] = int(
            (self.components['classID'] - 1) / 3 + 2003)
