import os
import csv
import re

studentProfile = []
correctDate = False

print(r""" 
██████╗  █████╗ ██╗     ██╗     ██████╗ ██╗████████╗
██╔══██╗██╔══██╗██║     ██║     ██╔══██╗██║╚══██╔══╝
██████╔╝███████║██║     ██║     ██████╔╝██║   ██║   
██╔══██╗██╔══██║██║     ██║     ██╔═══╝ ██║   ██║   
██████╔╝██║  ██║███████╗███████╗██║     ██║   ██║   
╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝╚═╝     ╚═╝   ╚═╝                                                     
                Enrollment System""")

if not os.path.isfile('StudentProfile.csv'):
   open('StudentProfile.csv')

userInput = input("Enrollment - E\nPayment - P\n")

if userInput == 'E' or 'e':
    studentProfile.append(input("Name: "))
    while not correctDate:
        userBirthdate = input("Birthdate (mm/dd/yyy): ")
        if re.match('^[0-1]{1}[0-9]{1}/[1-3]{1}[0-9]{1}/[0-9]{4}$', userBirthdate):
            studentProfile.append(userBirthdate)
            correctDate = True
        else:
            print("Incorrect formatting please try again")
            correctDate = False

    userSex = input("Sex: \nMale - M\nFemale - F\n")
    if userSex == 'M' or 'm':
        studentProfile.append("Male")
    elif userSex == 'F' or 'f':
        studentProfile.append("Female")

with open('StudentProfile.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(studentProfile)

with open('StudentProfile.csv', 'r',) as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)