import pandas as pd
import os
import csv
import re

studentProfile = []
correctDate = False
invalidInput = True
invalidGender = True
invalidCourse = True
invalidSemester = True

print(r""" 
██████╗  █████╗ ██╗     ██╗     ██████╗ ██╗████████╗
██╔══██╗██╔══██╗██║     ██║     ██╔══██╗██║╚══██╔══╝
██████╔╝███████║██║     ██║     ██████╔╝██║   ██║   
██╔══██╗██╔══██║██║     ██║     ██╔═══╝ ██║   ██║   
██████╔╝██║  ██║███████╗███████╗██║     ██║   ██║   
╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝╚═╝     ╚═╝   ╚═╝                                                     
                Enrollment System""")

if not os.path.isfile('StudentProfile.csv'):
   open('StudentProfile.csv', 'a')

def searchSubjects(subject):
    with open('1stSemesterSubjects.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[1] == "General" or row[1] == subject:
                print(row)

while invalidInput:
    print("Enrollment - E")
    print("Payment - P")
    match input("Input: "):
        case 'e' | 'E':
            invalidInput = False
            studentProfile.append(input("Name: "))
            while not correctDate:
                userBirthdate = input("Birthdate (mm/dd/yyy): ")
                #Checks whether the input is the correct date format
                if re.match('^[0-1]{1}[0-9]{1}/[1-3]{1}[0-9]{1}/[0-9]{4}$', userBirthdate):
                    studentProfile.append(userBirthdate)
                    correctDate = True
                else:
                    print("Incorrect formatting please try again")
                    correctDate = False

            while invalidGender:
                print("Sex:")
                print("Male - M")
                print("Female - F")
                match input("Input: "):
                    case 'm' | 'M':
                        invalidGender = False
                        studentProfile.append("Male")
                    case 'f' | 'F':
                        invalidGender = False
                        studentProfile.append("Female")
                    case _:
                        invalidGender = True
                        print("Invalid Input\n")
            
            while invalidCourse:
                print("Course:")
                print("Bachelor of Science in Computer Science (BSCS) - A")
                print("Bachelor of Entertainment and Multimedia Computing (BSEMC) - B")
                print("Bachelor of Multimedia Arts (BMMA) - C")
                match input("Input: "):
                    case 'a' | 'A':
                        invalidCourse = False
                        studentProfile.append("BSCS")
                    case 'b' | 'B':
                        invalidCourse = False
                        studentProfile.append("BSEMC")
                    case 'c' | 'C':
                        invalidCourse = False
                        studentProfile.append("BMMA")
                    case _:
                        invalidCourse = True
                        print("Invalid Input\n")

            while invalidSemester:
                print("What semester are you enrolling in?")
                print("1st Semester - A")
                print("2nd Semester - B")
                match input("Input: "):
                    case 'a' | 'A':
                        invalidSemester = False
                        studentProfile.append("1st Sem")
                    case 'b' | 'B':
                        invalidSemester = False
                        studentProfile.append("2nd Sem")
                    case _:
                        invalidSemester = True
                        print("Invalid Input\n")
            if studentProfile[4] == "1st Sem":
                match studentProfile[3]:
                    case "BSCS":
                        searchSubjects("BSCS")
                    case "BSEMC":
                        searchSubjects("BSEMC")
                    case "BMMA":
                        searchSubjects("BMMA")
                
        case 'p' | 'P':
            invalidInput = False
            pass
        case _:
            invalidInput = True
            print("Invalid Input\n")

with open('StudentProfile.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(studentProfile)

with open('StudentProfile.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

