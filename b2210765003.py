import sys

with open(sys.argv[1],"r",encoding="utf-8") as file:
    content = file.read().split("\n")
    mainDict = {}
    for i in content:
        person , school = i.split(":")
        mainDict[person] = str(school)
    for student in sys.argv[2].split(","):
        try:
            print("Name: {}\nUniversity:{}".format(student,mainDict[student]))
        except:
            print("No record of {} was found!".format(student))