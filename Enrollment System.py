import ctypes
import os
import csv
import re
import shutil
import random
import string

def Reference_Number_Generator():
    #Creates the random enrollment reference number
    randomReference = ''.join(random.choices(string.ascii_letters, k=8))
    with open('EnrollmentReferenceNumbers.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if sum(1 for row in reader) > 0:
                if randomReference == row[1]:
                    randomReference = ''.join(random.choices(string.ascii_letters, k=8))
    return randomReference

def Search_Subjects(subject, subjectFile):
    with open(subjectFile, 'r') as file:
        reader = csv.reader(file)
        totalTuition = 0
        for row in reader:
            if row[1] == "General" or row[1] == subject:
                totalTuition += int(row[2])
                print(row[0], row[1], row[2])
    print("Total tuiton fee: ", totalTuition)
    return totalTuition

def Backup():
    #Backs up every CSV file to a hidden backup folder
    shutil.copy('1stSemesterSubjects.csv', '.Backup')
    shutil.copy('2ndSemesterSubjects.csv', '.Backup')
    shutil.copy('EnrollmentReferenceNumbers.csv', '.Backup')
    shutil.copy('StudentProfile.csv', '.Backup')

def Recover(file):
    #Recovers CSV files from the hidden backup folder
    match file:
        case "1stSemesterSubjects.csv":
            shutil.copy('.Backup/1stSemesterSubjects.csv', os.getcwd())
        case "2ndSemesterSubjects.csv":
            shutil.copy('.Backup/2ndSemesterSubjects.csv', os.getcwd())
        case "EnrollmentReferenceNumbers.csv":
            shutil.copy('.Backup/EnrollmentReferenceNumbers.csv', os.getcwd())
        case "StudentProfile.csv":
            shutil.copy('.Backup/StudentProfile.csv', os.getcwd())
        case _:
            shutil.copy('.Backup/1stSemesterSubjects.csv', os.getcwd())
            shutil.copy('.Backup/EnrollmentReferenceNumbers.csv', os.getcwd())
            shutil.copy('.Backup/StudentProfile.csv', os.getcwd())

def File_Check_And_Recover(file):
    # Checks whether a file exist in the main directory if not it will check 
    # the hidden backup folder for the file if available it will restore 
    # the file to the main directory
    if not os.path.isfile(file):
        if not os.path.isfile('.Backup/' + file):
            open(file, 'a')
        else:
             Recover(file)

def Tamper_Check(newFile):
    # Checks if the file content has been tampered with and returns a boolean
    # 
    backupFile = '.Backup/' + newFile
    tampered = False
    with open(backupFile, 'r') as file:
        reader = csv.reader(file)
        backupFileRowCount = sum(1 for row in reader)
    with open(newFile, 'r') as file:
        reader = csv.reader(file)
        newFileRowCount = sum(1 for row in reader)
    if backupFileRowCount < newFileRowCount:
        tampered = True
        Recover(backupFile)
    return tampered

def Save_To_CSV(CSVfile, data):
    with open(CSVfile, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)
    

def Main_Menu():
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
    while invalidInput:
        print("Enrollment - E")
        print("Payment - P")
        match input("Input: "):
            case 'e' | 'E':
                invalidInput = False
                studentProfile.append(input("Name: "))
                while not correctDate:
                    userBirthdate = input("Birthdate (mm/dd/yyyy): ")
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
                            tuitionFee = Search_Subjects("BSCS", '1stSemesterSubjects.csv')
                        case "BSEMC":
                            tuitionFee = Search_Subjects("BSEMC", '1stSemesterSubjects.csv')
                        case "BMMA":
                            tuitionFee = Search_Subjects("BMMA", '1stSemesterSubjects.csv')
                if studentProfile[4] == "2nd Sem":
                    match studentProfile[3]:
                        case "BSCS":
                            tuitionFee = Search_Subjects("BSCS", '2ndSemesterSubjects.csv')
                        case "BSEMC":
                            tuitionFee = Search_Subjects("BSEMC", '2ndSemesterSubjects.csv')
                        case "BMMA":
                            tuitionFee = Search_Subjects("BMMA", '2ndSemesterSubjects.csv')
                enrollmentReferenceNumber = [Reference_Number_Generator(), tuitionFee]
                studentProfile.append("Not Enrolled")
                print("Your enrollment reference number to be presented for the payment: " + enrollmentReferenceNumber[0])

                Save_To_CSV('EnrollmentReferenceNumbers.csv', enrollmentReferenceNumber)
                if Tamper_Check('EnrollmentReferenceNumbers.csv'):
                    Save_To_CSV('EnrollmentReferenceNumbers.csv', enrollmentReferenceNumber)

                with open('StudentProfile.csv', 'w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(studentProfile)

                with open('StudentProfile.csv', 'r') as file:
                    reader = csv.reader(file)
                    for row in reader:
                        print(row)

                with open('EnrollmentReferenceNumbers.csv', 'r') as file:
                    reader = csv.reader(file)
                    for row in reader:
                        print(row)
                Backup()
                Main_Menu()
            case 'p' | 'P':
                invalidInput = False
                pass
            case _:
                invalidInput = True
                print("Invalid Input\n")

File_Check_And_Recover('StudentProfile.csv')
File_Check_And_Recover('1stSemesterSubjects.csv')
File_Check_And_Recover('2ndSemesterSubjects.csv')
File_Check_And_Recover('EnrollmentReferenceNumbers.csv')

if not os.path.isdir('.Backup'):
    os.mkdir(".Backup")
    FILE_ATTRIBUTE_HIDDEN = 0x02
    ret = ctypes.windll.kernel32.SetFileAttributesW(".Backup", FILE_ATTRIBUTE_HIDDEN)
    Backup()

Main_Menu()
