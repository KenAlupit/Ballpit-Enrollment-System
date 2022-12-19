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

def ID_Number_Generator():
    #Creates the random enrollment reference number
    randomID = ''.join(random.choices(string.digits, k=2)) + "-" + ''.join(random.choices(string.digits, k=4))
    with open('StudentProfile.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
             if sum(1 for row in reader) > 0:
                if randomID == row[1]:
                    randomID = ''.join(random.choices(string.digits, k=2)) + "-" + ''.join(random.choices(string.digits, k=4))
    return randomID

def Semester_Picker(semesterFile, course):
    with open(semesterFile, 'r') as file:
        reader = csv.reader(file)
        totalTuition = 0
        for row in reader:
            if row[1] == "General" or row[1] == course:
                totalTuition += int(row[2])
                print(row[0], row[1], row[2])
    return totalTuition

def Search_Subjects(course, semester):
    match semester:
        case "1st Sem":
            tuitionFee = Semester_Picker('1stSemesterSubjects.csv', course)
        case "2nd Sem":
            tuitionFee = Semester_Picker('2ndSemesterSubjects.csv', course)
    print("Total tuiton fee: ", tuitionFee)
    return tuitionFee


def Backup():
    #Backs up every CSV file to a hidden backup folder
    shutil.copy('1stSemesterSubjects.csv', '.Backup')
    shutil.copy('2ndSemesterSubjects.csv', '.Backup')
    shutil.copy('EnrollmentReferenceNumbers.csv', '.Backup')
    shutil.copy('StudentProfile.csv', '.Backup')

def Recover(file):
    #Recovers CSV files from the hidden backup folder
    match file:
        case '1stSemesterSubjects.csv':
            shutil.copy('.Backup/1stSemesterSubjects.csv', os.getcwd())
        case '2ndSemesterSubjects.csv':
            shutil.copy('.Backup/2ndSemesterSubjects.csv', os.getcwd())
        case 'EnrollmentReferenceNumbers.csv':
            shutil.copy('.Backup/EnrollmentReferenceNumbers.csv', os.getcwd())
        case 'StudentProfile.csv':
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

def Save_To_CSV(CSVfile, data):
    with open(CSVfile, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)

def Payment(reference):
    invalidPayment = True
    with open('EnrollmentReferenceNumbers.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if reference == row[0]:
                while invalidPayment:
                    userPayment = int((input("Input your payment: ")))                            
                    if userPayment < int(row[1]):
                        invalidPayment = True
                        print("Payment error! Your payment ips insufficient!")     
                    elif userPayment > int(row[1]):
                        invalidPayment = False
                        print("Payment Successful! Here is your change: ", userPayment - int(row[1]))                            
                    else:
                        invalidPayment = False
                        print("Payment Successful! ")  
    return not invalidPayment 

def Overwrite(file, data):
    with open(file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

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
                studentProfile.append(input("First Name: "))
                userMiddleName = input("Middle Name (0 if not applicable): ")
                match userMiddleName:
                    case 0:
                        studentProfile.append("N/A")
                    case _:
                        studentProfile.append(userMiddleName)
                studentProfile.append(input("Last Name: "))
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
                tuitionFee = Search_Subjects(studentProfile[5], studentProfile[6])
                enrollmentReferenceNumber = [Reference_Number_Generator(), tuitionFee]
                studentProfile.append("Not Enrolled")
                studentProfile.append(enrollmentReferenceNumber[0])
                print("Your enrollment reference number to be presented for the payment: " + enrollmentReferenceNumber[0])

                Save_To_CSV('EnrollmentReferenceNumbers.csv', enrollmentReferenceNumber)
                Recover('StudentProfile.csv')
                Save_To_CSV('StudentProfile.csv', studentProfile)
                Backup()
                Main_Menu()
                
            case 'p' | 'P':
                invalidInput = False
                invalidReference = True
                with open('EnrollmentReferenceNumbers.csv', 'r') as file:
                    reader = csv.reader(file)
                    match sum(1 for row in reader):
                        case 0:
                            print("Data unavailable please enroll first")
                            Main_Menu()
                        case _:
                            while invalidReference:
                                userReference = (input("Input your reference number: "))
                                with open('EnrollmentReferenceNumbers.csv', 'r') as file:
                                    reader = csv.reader(file)
                                    for row in reader:                  
                                        if row[0] == userReference: 
                                            invalidReference = False
                                with open('StudentProfile.csv', 'r') as file:
                                    reader = csv.reader(file)
                                    for row in reader:                  
                                        if row[8] == userReference:
                                            if row[1] != "0":
                                                print ("Student Name: " + row[0] + " " + row[1] + " " + row[2])
                                            else:
                                                print ("Student Name: " + row[0] + " " + row[2])
                                            Search_Subjects(row[5], row[6])
                                            if Payment(userReference):
                                                print("You are now succesfully enrolled!")
                                                userId = ID_Number_Generator()
                                                print("Your student ID: " + userId)
                                                lines = list()
                                                with open('StudentProfile.csv', 'r') as file:
                                                    reader = csv.reader(file)
                                                    for row in reader:
                                                        lines.append(row)
                                                        if row[8] == userReference:
                                                            row[8] = userId
                                                            row[7] = "Enrolled"
                                                Overwrite('StudentProfile.csv', lines)
                                                lines = list()
                                                with open('EnrollmentReferenceNumbers.csv', 'r') as file:
                                                    reader = csv.reader(file)
                                                    for row in reader:
                                                        lines.append(row)
                                                        if row[0] == userReference:
                                                            lines.remove(row)
                                                Overwrite('EnrollmentReferenceNumbers.csv', lines)
                                                Backup()
                                        elif invalidReference:
                                            invalidReference = True
                                            print("Invalid reference number")            
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
