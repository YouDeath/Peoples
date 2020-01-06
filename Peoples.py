class Date():
    def __init__(self,year,month,day):
        self.day = day
        self.year = year
        self.month = month

class NameInfo():
    def __init__(self,name,surname,patronymic):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic

class People():
    def __init__(self,info_of_names,date_of_birth):
        self.date_of_birth = date_of_birth
        self.info_of_names = info_of_names

class Society():
    def __init__(self,peoples):
        self.peoples = peoples
    def EarlierThan(self,eyear):
        ch = 0
        for i in range(len(self.peoples)):
            if self.peoples[i].date_of_birth.year < eyear:
                ch+=1
                print(self.peoples[i].info_of_names.surname)
        print(ch)
    def InYearMedian(self,yearFrom,yearTo):
        for i in range(len(self.peoples)):
            if yearFrom < self.peoples[i].date_of_birth.year < yearTo:
                outString = self.peoples[i].info_of_names.surname + " " + self.peoples[i].info_of_names.name + " " + self.peoples[i].info_of_names.patronymic + " " + str(self.peoples[i].date_of_birth.year)
                print(outString)

file = open('Perepis.txt', 'r')

peopleArr = []

for line in file:
    inString = line[:len(line)-1]
    inArr = inString.split("  ")
    dateArr = inArr[3].split(".")
    readyArr = [inArr[0],inArr[1],inArr[2],int(dateArr[0]),int(dateArr[1]),int(dateArr[2])]
    print(readyArr)
    itrPeople = People(NameInfo(readyArr[1],readyArr[0],readyArr[2]),Date(readyArr[5],readyArr[4],readyArr[3]))
    peopleArr.append(itrPeople)
my_Society = Society(peopleArr)
my_Society.EarlierThan(1978)
my_Society.InYearMedian(1963,1980)




